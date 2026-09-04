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
git add .github .gitignore LICENSE README.md GITHUB_DEPLOY_AND_UPDATE_GUIDE.md HOW_TO_UPDATE_QUESTIONS.md ai_config.example.json ai_generate_questions.py app.js favicon.svg generate_diagrams.py generate_diagrams_ext.py generate_questions.py images import_questions.py index.html new_questions_template.txt questions.js questions_data.json style.css test_quiz.py prepare_review.py test_review.py
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

默认使用 DeepSeek 接口（`https://api.deepseek.com/v1`、`deepseek-chat`）。Key 只填在 Secrets，不要发到聊天或写入文件。

在 **Settings → Actions → General → Workflow permissions** 勾选 **Allow GitHub Actions to create and approve pull requests** 并保存。虽然开关名称包括 approve，本工作流不执行批准或合并，只创建待审核请求。

### 运行时间与审核

- 以 2026-09-04 为起点，每 3 天生成 2 道题，计划北京时间 09:17 执行。每天启动一次轻量检查，只有符合日期才调用 AI，因此跨月也保持三天间隔。
- GitHub 定时任务可能延迟或漏跑；公开仓库长时间（60 天）无活动可能停用定时任务，届时到 Actions 重新启用。并非严格计时服务。
- 有尚未关闭或合并的 `codex/quiz-review-` 待审核批次时暂停生成，不覆盖你正在审核的题。
- 首次配置好后，可在 **Actions → Generate questions for review → Run workflow** 手动测试，选择 `main`，数量为 1 或 2。手动运行不受三天日期限制，但仍等待上一批审核完成。
- 生成失败、数量不符、结构错误或题干高度相似时，流程报错，不改线上题库；不自动重试收费 API。

在仓库 **Pull requests** 中打开“待审核：新增地理题目”，正文会显示题干、四个选项、答案和解析。请核对事实、唯一正确答案及重复内容，并在 **Files changed** 查看实际改动。

- 通过：你点击 **Merge pull request → Confirm merge**；合并进入 `main` 后，由 GitHub Pages 发布。仅勾选审核清单或发表评论不会发布。
- 不通过：点击 **Close pull request**，网站不变；下一轮再生成。
- 需修改：在候选分支修改 JSON，运行 `python import_questions.py --sync-only` 和 `python test_quiz.py`，同步提交 JSON 与 JS，复核后再合并。若发生合并冲突，不要强行合并，可关闭旧批次重新生成。

工作流不会自动合并，也不会推送到 `main`。人工合并后才发布，因此不依赖机器人提交触发 Pages 的行为。审核内容公开可见，不是私密草稿。这里是流程层面的人工闸门，不替代仓库分支保护。

如要暂停自动出题，在 Actions 中选择该工作流，再选择 **Disable workflow**。AI 输出仍可能含事实错误，格式检查和相似题干检测不能替代人工审核。
