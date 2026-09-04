# -*- coding: utf-8 -*-
"""从中文文本导入新题，或将 JSON 题库同步到网页数据文件。"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / "questions_data.json"
JS_PATH = BASE_DIR / "questions.js"
DEFAULT_INPUT_PATH = BASE_DIR / "new_questions.txt"
TEMPLATE_PATH = BASE_DIR / "new_questions_template.txt"
ALLOWED_IMAGE_SUFFIXES = {".svg", ".png", ".jpg", ".jpeg", ".webp"}


def validate_question(question: dict[str, Any], label: str) -> None:
    """严格检查一条题目的结构和本地图片路径。"""

    if not isinstance(question, dict):
        raise ValueError(f"{label}不是对象")
    for field in ("category", "book", "question", "explanation"):
        if not isinstance(question.get(field), str) or not question[field].strip():
            raise ValueError(f"{label}缺少非空字段：{field}")

    options = question.get("options")
    if (
        not isinstance(options, list)
        or len(options) != 4
        or any(not isinstance(option, str) or not option.strip() for option in options)
    ):
        raise ValueError(f"{label}必须包含 4 个非空文本选项")
    if len({option.strip() for option in options}) != 4:
        raise ValueError(f"{label}的 4 个选项不能重复")
    if type(question.get("answer")) is not int or question["answer"] not in (0, 1, 2, 3):
        raise ValueError(f"{label}的答案索引必须是 0、1、2 或 3")

    image = question.get("image")
    if image is not None:
        if not isinstance(image, str):
            raise ValueError(f"{label}的 image 必须是字符串或 null")
        image_path = Path(image.replace("\\", "/"))
        if (
            image_path.is_absolute()
            or ".." in image_path.parts
            or not image_path.parts
            or image_path.parts[0] != "images"
            or image_path.suffix.lower() not in ALLOWED_IMAGE_SUFFIXES
        ):
            raise ValueError(f"{label}的图片必须位于 images/ 目录中")
        if not (BASE_DIR / image_path).is_file():
            raise ValueError(f"{label}引用的图片不存在：{image}")


def parse_txt_questions(txt_content: str) -> list[dict[str, Any]]:
    """解析使用【字段】标记的中文题目文本。"""

    blocks = re.split(r"\n\s*={3,}\s*\n|\n\s*-{3,}\s*\n|\n\s*\n\s*\n", txt_content)
    parsed: list[dict[str, Any]] = []
    letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}

    for block_number, block in enumerate(blocks, start=1):
        lines = [
            line.strip()
            for line in block.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if not lines:
            continue

        item: dict[str, Any] = {
            "category": "自然地理",
            "book": "必修一",
            "question": "",
            "options": ["", "", "", ""],
            "answer": None,
            "explanation": "",
            "image": None,
        }
        field_map = {
            "【分类】": ("category", None),
            "【分册】": ("book", None),
            "【题干】": ("question", None),
            "【配图】": ("image", None),
            "【选项A】": ("options", 0),
            "【选项B】": ("options", 1),
            "【选项C】": ("options", 2),
            "【选项D】": ("options", 3),
            "【解析】": ("explanation", None),
        }

        for line in lines:
            if line.startswith("【答案】"):
                answer_text = line.removeprefix("【答案】").strip().upper()
                if answer_text not in letter_map:
                    raise ValueError(f"第 {block_number} 个题目块的答案必须是 A、B、C 或 D")
                item["answer"] = letter_map[answer_text]
                continue
            for prefix, (field, option_index) in field_map.items():
                if not line.startswith(prefix):
                    continue
                value = line.removeprefix(prefix).strip()
                if option_index is None:
                    item[field] = (value or None) if field == "image" else value
                else:
                    item[field][option_index] = value
                break

        validate_question(item, f"第 {block_number} 个题目块")
        parsed.append(item)

    return parsed


def load_bank() -> list[dict[str, Any]]:
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("questions_data.json 顶层必须是数组")
    for index, question in enumerate(data, start=1):
        validate_question(question, f"题库第 {index} 题")
    return data


def sync_to_js(questions: list[dict[str, Any]]) -> None:
    """规范化 ID，并同时写入 JSON 与浏览器使用的 JS 文件。"""

    for index, question in enumerate(questions, start=1):
        question["id"] = index
    serialized = json.dumps(questions, ensure_ascii=False, indent=2)
    JSON_PATH.write_text(serialized + "\n", encoding="utf-8")
    JS_PATH.write_text(f"const GEO_QUESTIONS = {serialized};\n", encoding="utf-8")
    image_count = sum(1 for question in questions if question.get("image"))
    print(f"同步完成：共 {len(questions)} 道题，其中带图题 {image_count} 道。")


def import_questions(input_path: Path) -> int:
    if not input_path.is_file():
        raise FileNotFoundError(
            f"找不到 {input_path.name}。请复制 {TEMPLATE_PATH.name} 为 {input_path.name} 后填写新题。"
        )

    existing = load_bank()
    incoming = parse_txt_questions(input_path.read_text(encoding="utf-8"))
    known_questions = {re.sub(r"\s+", "", item["question"]) for item in existing}
    additions = []
    for question in incoming:
        normalized_text = re.sub(r"\s+", "", question["question"])
        if normalized_text in known_questions:
            print(f"跳过重复题目：{question['question'][:40]}")
            continue
        known_questions.add(normalized_text)
        additions.append(question)

    if not additions:
        print("没有发现可新增的非重复题目，题库未改动。")
        return 0

    sync_to_js(existing + additions)
    print(f"本次新增 {len(additions)} 道题。")
    return len(additions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="待导入的中文题目文本，默认 new_questions.txt",
    )
    parser.add_argument(
        "--sync-only",
        action="store_true",
        help="只校验 questions_data.json 并重新生成 questions.js",
    )
    args = parser.parse_args()

    if args.sync_only:
        sync_to_js(load_bank())
        return 0
    import_questions(args.input.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
