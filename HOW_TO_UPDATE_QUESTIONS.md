# 📚 更新题库

网页实际读取 `questions.js`。无论采用哪种编辑方式，最终都要运行校验，确保它与 `questions_data.json` 同步。

## 方式一：从中文文本导入

1. 复制 `new_questions_template.txt` 为 `new_questions.txt`。
2. 删除示例题并按模板填写新题；多道题之间用至少三个等号或空行分隔。
3. 在本目录运行：

```powershell
python import_questions.py new_questions.txt
python test_quiz.py
```

导入器会检查题干、四个非重复选项、答案、解析和图片路径，跳过与现有题干完全重复的题目，并同时更新两个题库文件。`new_questions.txt` 是本地工作文件，不会被 Git 提交。

## 方式二：直接编辑 JSON

在 `questions_data.json` 数组中修改或追加对象：

```json
{
  "id": 125,
  "category": "自然地理",
  "book": "必修一",
  "question": "题目内容……",
  "options": ["选项A", "选项B", "选项C", "选项D"],
  "answer": 0,
  "explanation": "考点解析……",
  "image": null
}
```

`answer` 使用从 0 开始的索引：0=A、1=B、2=C、3=D。编辑后运行：

```powershell
python import_questions.py --sync-only
python test_quiz.py
```

`--sync-only` 会校验全部题目、重新连续编号，并生成新的 `questions.js`。

## 添加图片

支持 `.svg`、`.png`、`.jpg`、`.jpeg` 和 `.webp`。图片必须放在 `images/` 内，并使用相对路径，例如：

```json
"image": "images/my_map.svg"
```

导入器会拒绝外部 URL、上级目录路径以及不存在的图片。

## AI 辅助生成（可选）

线上已提供“每 3 天 2 题 → Pull Request 人工审核 → 合并后发布”的流程，配置及审核操作见 [发布指南](GITHUB_DEPLOY_AND_UPDATE_GUIDE.md#可选github-actions-生成题目)。下面的命令只用于本地生成，运行后也须自行审核再上传。

在 PowerShell 中临时设置环境变量后运行：

```powershell
$env:AI_API_KEY = "你的新Key"
python ai_generate_questions.py "地质构造" 5
python test_quiz.py
Remove-Item Env:AI_API_KEY
```

也可复制 `ai_config.example.json` 为本地 `ai_config.json`。不要把真实 Key 写入代码、README、工作流或 Git 提交。AI 生成内容必须经过人工复核后再发布。
