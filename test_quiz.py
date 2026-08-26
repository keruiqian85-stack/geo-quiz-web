# -*- coding: utf-8 -*-
"""
测试与验证高中地理题库及前端文件
"""
import json
import os
import re

def test_questions_json():
    json_path = os.path.join(os.path.dirname(__file__), "questions_data.json")
    assert os.path.exists(json_path), "questions_data.json 不存在！"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"[TEST 1] 题库总量测试: 读取到 {len(data)} 道题")
    assert len(data) >= 120, f"预期至少 120 题，实际读取到 {len(data)} 题！"

    js_path = os.path.join(os.path.dirname(__file__), "questions.js")
    with open(js_path, "r", encoding="utf-8") as f:
        js_content = f.read().strip()
    prefix = "const GEO_QUESTIONS = "
    assert js_content.startswith(prefix) and js_content.endswith(";"), "questions.js 格式无效"
    js_data = json.loads(js_content[len(prefix):-1])
    assert js_data == data, "questions.js 与 questions_data.json 不同步"

    # 检验每道题结构
    ids = set()
    categories = {}
    books = {}

    for i, q in enumerate(data):
        assert "id" in q, f"第 {i+1} 题缺失 id"
        assert "question" in q and len(q["question"].strip()) > 0, f"第 {i+1} 题题干为空"
        assert "options" in q and len(q["options"]) == 4, f"第 {i+1} 题选项数量不为4 (实际: {len(q.get('options', []))})"
        assert "answer" in q and q["answer"] in [0, 1, 2, 3], f"第 {i+1} 题答案索引无效: {q.get('answer')}"
        assert "explanation" in q and len(q["explanation"].strip()) > 0, f"第 {i+1} 题解析为空"
        assert q["id"] not in ids, f"发现重复ID: {q['id']}"
        ids.add(q["id"])

        cat = q.get("category", "未分类")
        bk = q.get("book", "未分册")
        categories[cat] = categories.get(cat, 0) + 1
        books[bk] = books.get(bk, 0) + 1

        # 选项不应有重复
        assert len(set(q["options"])) == 4, f"第 {i+1} 题选项存在重复项: {q['options']}"

    print("[TEST 2] 题库教材分布统计:")
    for b, c in sorted(books.items()):
        print(f"   - {b}: {c} 题")
    print("[TEST 3] 题库学科分类统计:")
    for cat, c in sorted(categories.items()):
        print(f"   - {cat}: {c} 题")

    # 检查配图题目
    img_questions = [q for q in data if q.get("image")]
    print(f"[TEST 4] 带图试题数量: {len(img_questions)} 道")
    assert len(img_questions) >= 10, f"带图试题少于10道: {len(img_questions)}"
    for q in img_questions:
        img_rel = q["image"]
        img_full = os.path.join(os.path.dirname(__file__), img_rel)
        assert os.path.exists(img_full), f"试题 #{q['id']} 配图文件不存在: {img_rel}"

    print("[PASS] Question bank and images validation passed completely!")

def test_frontend_files():
    base_dir = os.path.dirname(__file__)
    files = ["index.html", "style.css", "questions.js", "app.js"]
    for fname in files:
        fpath = os.path.join(base_dir, fname)
        assert os.path.exists(fpath), f"{fname} not found!"
        sz = os.path.getsize(fpath)
        assert sz > 0, f"{fname} is empty!"
        print(f"[TEST FILE] {fname}: {sz} bytes")

    # 检查 index.html 关键元素与 ID
    with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()

    required_ids = [
        "setupView", "quizView", "resultView", "quizFooter",
        "timerDisplay", "nextBtn", "analysisBox", "optionsContainer",
        "questionText", "finalScorePercent", "resTime", "retryBtn", "backHomeBtn",
        "homeHistorySection", "histTotalRounds", "histAvgAccuracy"
    ]
    for el_id in required_ids:
        assert f'id="{el_id}"' in html, f"index.html missing key element ID: {el_id}"

    print("[PASS] Frontend files and DOM structure validated!")

if __name__ == "__main__":
    test_questions_json()
    test_frontend_files()
    print("\n[ALL TESTS SUCCESS] High school geography quiz system fully verified!")
