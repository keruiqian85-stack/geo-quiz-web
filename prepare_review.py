"""Prepare a small validated batch on a review branch, never publish it."""

import argparse
import html
import re
from difflib import SequenceMatcher
from pathlib import Path

from ai_generate_questions import generate_with_ai
from import_questions import load_bank, sync_to_js, validate_question


def normalize(text):
    return re.sub(r'[\W_]+', '', text).casefold()


def validate_candidates(incoming, existing, count):
    if not isinstance(incoming, list) or len(incoming) != count:
        raise ValueError(f'AI 必须返回恰好 {count} 道题，题库未更新')
    known = [normalize(q['question']) for q in existing]
    clean = []
    for index, question in enumerate(incoming, 1):
        validate_question(question, f'候选题 {index}')
        normalized = normalize(question['question'])
        if not normalized or any(SequenceMatcher(None, normalized, old).ratio() >= 0.9 for old in known):
            raise ValueError('发现重复或高度相似的题干，请重新生成')
        known.append(normalized)
        clean.append({key: question[key] for key in ('category', 'book', 'question', 'options', 'answer', 'explanation')})
        clean[-1]['image'] = question.get('image')
    return clean


def review_body(questions):
    def safe(value):
        return html.escape(str(value)).replace('@', '&#64;')
    lines = ['# 地理新题待审核', '',
             '本批题目由 AI 生成，尚未上线。格式检查不能保证知识准确，请人工核对。', '',
             '- [ ] 题干准确、条件充分，与现有题库不重复',
             '- [ ] 四个选项中只有一个正确答案',
             '- [ ] 答案、解析、教材归属及素材使用均已核实', '',
             '通过：点击 Merge pull request 并确认，网站随后自动发布。',
             '不通过：点击 Close pull request；不会改变线上题库。',
             '如需修改，请同时同步 questions_data.json 和 questions.js，并重新检查。', '']
    for index, q in enumerate(questions, 1):
        lines += [f'## 第 {index} 题', '', '<pre>',
                  safe(q['category'] + ' / ' + q['book']), safe(q['question'])]
        lines += [safe(f'{"ABCD"[i]}. {option}') for i, option in enumerate(q['options'])]
        lines += [safe('答案：' + 'ABCD'[q['answer']]), safe('解析：' + q['explanation']), '</pre>', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', required=True)
    parser.add_argument('--count', type=int, choices=(1, 2), default=2)
    parser.add_argument('--body', type=Path, required=True)
    args = parser.parse_args()
    existing = load_bank()
    additions = validate_candidates(generate_with_ai(args.topic, args.count), existing, args.count)
    args.body.write_text(review_body(additions), encoding='utf-8')
    sync_to_js(existing + additions)


if __name__ == '__main__':
    main()
