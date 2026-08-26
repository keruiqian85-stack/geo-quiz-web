# -*- coding: utf-8 -*-
"""
高中地理大模型自动出题与一键导入工具 (ai_generate_questions.py)

功能：
1. 支持通过 OpenAI 兼容 API 接口（包括 DeepSeek, 通义千问, GPT, 智谱等大模型）
2. 按照高中地理最新课程标准和教材模块，全自动生成符合高考要求的选择题、4选项、答案和深度解析
3. 自动生成或匹配 SVG 矢量示意图
4. 一键自动追加合并入题库 (questions_data.json & questions.js) 并运行测试
"""

import os
import sys
import json
import re

try:
    from .import_questions import load_bank, sync_to_js, validate_question
except ImportError:
    from import_questions import load_bank, sync_to_js, validate_question

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "questions_data.json")
JS_PATH = os.path.join(BASE_DIR, "questions.js")
CONFIG_PATH = os.path.join(BASE_DIR, "ai_config.json")

DEFAULT_CONFIG = {
    "api_key": "YOUR_API_KEY_HERE",
    "base_url": "https://api.deepseek.com/v1",
    "model": "deepseek-chat"
}

def load_config():
    """读取可选本地配置，并优先使用环境变量中的敏感信息。"""
    config = dict(DEFAULT_CONFIG)
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config.update(json.load(f))
    config["api_key"] = os.environ.get("AI_API_KEY") or config.get("api_key")
    config["base_url"] = os.environ.get("AI_BASE_URL") or config.get("base_url")
    config["model"] = os.environ.get("AI_MODEL") or config.get("model")
    return config

def build_prompt(topic, count=5):
    return f"""你是一位国家级高中地理特级教师与高考命题专家。
请结合中国现行高中地理新课标教材（必修第一册、必修第二册、选择性必修1、选择性必修2、选择性必修3及区域地理），围绕专题【{topic}】，生成 {count} 道高质量的高中地理单项选择题（四选一）。

必须严格按照以下 JSON 数组格式返回，不要包含任何额外的 markdown 格式或问候语：
[
  {{
    "category": "自然地理",
    "book": "选择性必修1",
    "question": "题干内容...",
    "options": [
      "选项A内容",
      "选项B内容",
      "选项C内容",
      "选项D内容"
    ],
    "answer": 1,
    "explanation": "深度考点解析及各选项辨析..."
  }}
]

注意：
1. answer 是正确答案对应的数字索引：0代表A，1代表B，2代表C，3代表D。
2. 试题要贴合高考真实情境与地理核心素养（区域认知、综合思维、人地协调观、地理实践力）。
3. 解析要详尽准确，具有启发性。
"""

def generate_with_ai(topic, count=5):
    cfg = load_config()
    api_key = cfg.get("api_key")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("\n⚠️ 未配置 AI_API_KEY 环境变量或有效的本地 ai_config.json。")
        return []

    try:
        import urllib.request

        url = cfg.get("base_url", "https://api.deepseek.com/v1").rstrip("/") + "/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        prompt = build_prompt(topic, count)
        payload = {
            "model": cfg.get("model", "deepseek-chat"),
            "messages": [
                {"role": "system", "content": "你是一位专业的高中地理命题专家。必须且仅输出合法的 JSON 格式。"},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=60) as resp:
            res_data = json.loads(resp.read().decode("utf-8"))
            content = res_data["choices"][0]["message"]["content"].strip()

            # 清除可能带有的 markdown 标记 ```json ... ```
            clean_json = re.sub(r"^```(json)?", "", content, flags=re.MULTILINE)
            clean_json = re.sub(r"```$", "", clean_json, flags=re.MULTILINE).strip()

            parsed_questions = json.loads(clean_json)
            return parsed_questions

    except Exception as e:
        print(f"调用大模型出题失败: {e}")
        return []

def append_to_bank(new_questions):
    if not new_questions:
        print("没有新题目可追加。")
        return

    existing = load_bank()
    start_id = len(existing) + 1
    for i, q in enumerate(new_questions):
        validate_question(q, f"AI 返回的第 {i + 1} 题")
        q["id"] = start_id + i
        if "image" not in q:
            q["image"] = None
        existing.append(q)
    sync_to_js(existing)
    print(f"\n[AI SUCCESS] Added {len(new_questions)} new questions!")
    print(f"Total questions in bank: {len(existing)}")

if __name__ == "__main__":
    cfg = load_config()
    print("大模型自动命题系统已准备完毕。")
    print(f"当前配置的模型为: {cfg.get('model')}")

    # 支持命令行参数快速生成新题目
    import sys
    if len(sys.argv) > 1:
        topic = sys.argv[1]
        count = 5
        if len(sys.argv) > 2:
            try:
                count = max(1, min(20, int(sys.argv[2])))
            except ValueError:
                pass
        print(f"开始围绕专题【{topic}】生成 {count} 道新题目...")
        qs = generate_with_ai(topic, count)
        if qs:
            append_to_bank(qs)
            print("题库更新并同步成功！")
        else:
            print("生成失败，请检查配置或API key。")
    else:
        print("\n您可以使用以下方式直接出题：")
        print("  python ai_generate_questions.py \"宇宙与地球关系\" 5")
