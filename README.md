# 🌍 高中地理网页刷题与自测系统

一个无需后端的静态高中地理题库。目前包含 **124 道四选一单选题**，覆盖自然地理、人文地理、选择性必修课程及区域地理专题，其中 74 道题带有本地示意图。

> 题目由项目维护者整理，发布前仍建议由任课教师复核。项目不宣称替代教材、课程标准或正式考试资料。

## 功能

- 20 题、30 题或全量练习；全量题数会根据题库自动更新
- 按教材模块筛选，题目和选项分别随机排列
- 即时判分、答案解析、计时与键盘快捷键
- 浏览器本地保存最近 50 次成绩与错题记录
- 支持粘贴 JSON 临时导入题目，输入内容会经过结构与路径校验
- 明亮/暗色主题，适配桌面与移动设备

## 本地运行

直接打开 `index.html` 即可使用。为了获得与 GitHub Pages 更接近的效果，也可以启动本地静态服务器：

```powershell
python -m http.server 8000
```

然后访问 `http://localhost:8000/`。

## 主要文件

- `index.html`、`style.css`、`app.js`：页面与交互
- `questions_data.json`：便于编辑的题库源文件
- `questions.js`：网页实际加载的题库文件
- `images/`：题目配图
- `import_questions.py`：文本导入与 JSON → JS 同步工具
- `test_quiz.py`：题库和页面结构校验
- `.github/workflows/sync_questions.yml`：可选的人工触发式 AI 出题流程

更新题库时必须保持 `questions_data.json` 与 `questions.js` 同步。具体操作见 [HOW_TO_UPDATE_QUESTIONS.md](HOW_TO_UPDATE_QUESTIONS.md)，发布步骤见 [GITHUB_DEPLOY_AND_UPDATE_GUIDE.md](GITHUB_DEPLOY_AND_UPDATE_GUIDE.md)。

## API Key 安全

推荐使用环境变量 `AI_API_KEY`。如需本地配置，可复制 `ai_config.example.json` 为 `ai_config.json`；后者已被 `.gitignore` 排除，绝不能提交到 GitHub。

如果某个 Key 曾经出现在聊天记录、日志或公开提交中，请立即前往对应服务商后台撤销并重新创建。

## 许可与内容来源

如果将本目录发布为独立开源仓库，请在创建仓库时明确选择许可证。不要提交没有转载或再发布权利的教材扫描图、真题原文或第三方插图。
