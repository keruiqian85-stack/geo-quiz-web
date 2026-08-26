# 🌐 GitHub 发布与更新指南

## 推荐：发布为独立仓库

当前目录位于一个更大的项目仓库中。若题库需要独立维护，建议新建 `geo-quiz-web` 仓库，并把本目录的**内容**作为新仓库根目录；不要在现有大仓库中执行 `git add .`。

上传前请确认：

- `ai_config.json` 未出现在 `git status` 或暂存区中
- `python test_quiz.py` 通过
- `questions_data.json` 与 `questions.js` 已同步
- `LICENSE` 文件存在，并确认题目和图片具有发布权

首次提交时只添加本项目文件：

```bash
git init
git branch -M main
git add .github .gitignore LICENSE README.md GITHUB_DEPLOY_AND_UPDATE_GUIDE.md HOW_TO_UPDATE_QUESTIONS.md ai_config.example.json ai_generate_questions.py app.js favicon.svg generate_diagrams.py generate_diagrams_ext.py generate_questions.py images import_questions.py index.html new_questions_template.txt questions.js questions_data.json style.css test_quiz.py
git commit -m "feat: publish geography quiz"
git remote add origin https://github.com/YOUR_NAME/geo-quiz-web.git
git push -u origin main
```

## 开启 GitHub Pages

1. 打开仓库的 **Settings → Pages**。
2. 在 **Build and deployment** 中选择 **Deploy from a branch**。
3. 选择 `main` 分支和 `/ (root)`，保存。
4. 等待部署后访问 `https://YOUR_NAME.github.io/geo-quiz-web/`。

## 日常手动更新

本地编辑或导入后先执行：

```bash
python import_questions.py --sync-only
python test_quiz.py
git add questions_data.json questions.js images
git commit -m "content: update geography questions"
git push
```

如果使用中文文本导入，把第一条命令替换为：

```bash
python import_questions.py new_questions.txt
```

不要只在 GitHub 网页上修改 `questions_data.json`，否则线上页面加载的 `questions.js` 不会更新。

## 可选：GitHub Actions 生成题目

仓库包含 `.github/workflows/sync_questions.yml`。在 **Settings → Secrets and variables → Actions** 添加：

- `AI_API_KEY`：必填
- `AI_BASE_URL`：可选，默认由脚本配置决定
- `AI_MODEL`：可选

之后可在 **Actions → Sync and Update Geography Questions → Run workflow** 中输入专题和数量。工作流会生成题目、执行校验，并在成功后提交两个题库文件。

AI 输出可能含事实错误、过时材料或低质量干扰项。建议在启用自动提交前增加人工审核分支或 Pull Request 流程，不要把自动生成结果直接当作正式考试资料。
