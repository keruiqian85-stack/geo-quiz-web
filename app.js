/**
 * 高中地理全教材网页刷题与自测交互逻辑
 */

(function () {
  // --- 状态定义 ---
  let allQuestions = typeof GEO_QUESTIONS !== 'undefined' ? GEO_QUESTIONS : [];
  let selectedCategory = 'all';
  let selectedCount = 20;

  let currentQuizList = []; // 当前轮次抽出的随机题目列表（包含打乱后的选项）
  let currentIndex = 0;
  let score = 0;
  let answeredCount = 0;
  let userHistory = []; // 记录每道题的用户作答: { questionObj, userSelected, isCorrect, timeSpent }

  // 计时器状态
  let timerInterval = null;
  let totalSeconds = 0;

  // DOM 元素引用
  const setupView = document.getElementById('setupView');
  const quizView = document.getElementById('quizView');
  const resultView = document.getElementById('resultView');
  const quizFooter = document.getElementById('quizFooter');
  const restartNavBtn = document.getElementById('restartNavBtn');
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const backHomeBtn = document.getElementById('backHomeBtn');

  // 做题区元素
  const currentQNum = document.getElementById('currentQNum');
  const totalQNum = document.getElementById('totalQNum');
  const liveCorrectCount = document.getElementById('liveCorrectCount');
  const liveAnsweredCount = document.getElementById('liveAnsweredCount');
  const progressFill = document.getElementById('progressFill');

  const questionTagCategory = document.getElementById('questionTagCategory');
  const questionTagBook = document.getElementById('questionTagBook');
  const questionOriginalId = document.getElementById('questionOriginalId');
  const questionText = document.getElementById('questionText');
  const questionImageWrap = document.getElementById('questionImageWrap');
  const questionImage = document.getElementById('questionImage');
  const optionsContainer = document.getElementById('optionsContainer');

  const analysisBox = document.getElementById('analysisBox');
  const analysisHeader = document.getElementById('analysisHeader');
  const statusIcon = document.getElementById('statusIcon');
  const statusText = document.getElementById('statusText');
  const correctHint = document.getElementById('correctHint');
  const analysisText = document.getElementById('analysisText');

  // 底部栏
  const timerDisplay = document.getElementById('timerDisplay');
  const footerHint = document.getElementById('footerHint');
  const nextBtn = document.getElementById('nextBtn');

  // 结果区元素
  const finalScorePercent = document.getElementById('finalScorePercent');
  const resCorrect = document.getElementById('resCorrect');
  const resWrong = document.getElementById('resWrong');
  const resTotal = document.getElementById('resTotal');
  const resTime = document.getElementById('resTime');
  const resultEvaluation = document.getElementById('resultEvaluation');
  const toggleReviewBtn = document.getElementById('toggleReviewBtn');
  const reviewSection = document.getElementById('reviewSection');
  const reviewList = document.getElementById('reviewList');
  const tabCountAll = document.getElementById('tabCountAll');
  const tabCountWrong = document.getElementById('tabCountWrong');
  const tabCountCorrect = document.getElementById('tabCountCorrect');

  // 主页历史记录元素
  const homeHistorySection = document.getElementById('homeHistorySection');
  const histTotalRounds = document.getElementById('histTotalRounds');
  const histTotalAnswered = document.getElementById('histTotalAnswered');
  const histAvgAccuracy = document.getElementById('histAvgAccuracy');
  const histTotalWrongPool = document.getElementById('histTotalWrongPool');
  const historyLogList = document.getElementById('historyLogList');
  const clearHistoryBtn = document.getElementById('clearHistoryBtn');

  // 辅助函数：Fisher-Yates 数组洗牌算法
  function shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // 只允许题库 images 目录中的本地图片，避免导入数据注入任意 URL。
  function sanitizeImagePath(value) {
    if (typeof value !== 'string' || !value.trim()) return null;
    const normalized = value.trim().replace(/\\/g, '/');
    if (
      normalized.includes('..') ||
      !/^images\/[a-zA-Z0-9._/-]+\.(svg|png|jpe?g|webp)$/i.test(normalized)
    ) {
      return null;
    }
    return normalized;
  }

  function escapeHtml(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function updateQuestionCounts() {
    const total = allQuestions.length;
    document.querySelectorAll('[data-question-total]').forEach((el) => {
      el.textContent = total;
    });
    document.title = `高中地理全套教材 ${total} 题智能刷题与自测系统`;
  }

  // 格式化秒数为 MM:SS 或 HH:MM:SS
  function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    const pad = (n) => (n < 10 ? '0' + n : n);
    if (mins >= 60) {
      const hrs = Math.floor(mins / 60);
      const remainMins = mins % 60;
      return `${pad(hrs)}:${pad(remainMins)}:${pad(secs)}`;
    }
    return `${pad(mins)}:${pad(secs)}`;
  }

  // 初始化主题（支持深色模式持久化）
  function initTheme() {
    const saved = localStorage.getItem('geo_quiz_theme');
    if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.setAttribute('data-theme', 'dark');
      themeToggleBtn.textContent = '☀️';
    } else {
      document.documentElement.removeAttribute('data-theme');
      themeToggleBtn.textContent = '🌓';
    }
  }

  themeToggleBtn.addEventListener('click', () => {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDark) {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('geo_quiz_theme', 'light');
      themeToggleBtn.textContent = '🌓';
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('geo_quiz_theme', 'dark');
      themeToggleBtn.textContent = '☀️';
    }
  });

  // 分类选择点击
  const categoryFilterGroup = document.getElementById('categoryFilterGroup');
  categoryFilterGroup.addEventListener('click', (e) => {
    const btn = e.target.closest('.chip');
    if (!btn) return;
    categoryFilterGroup.querySelectorAll('.chip').forEach((c) => c.classList.remove('active'));
    btn.classList.add('active');
    selectedCategory = btn.dataset.cat;
  });

  // 开始刷题
  document.getElementById('startQuizBtn').addEventListener('click', startQuiz);
  restartNavBtn.addEventListener('click', () => {
    if (confirm('确定要退出当前正在进行的作答吗？当前进度将不会被保存。')) {
      resetToSetup();
    }
  });
  document.getElementById('retryBtn').addEventListener('click', () => {
    startQuiz(); // 立即按上一轮设置开启新一轮随机题
  });
  if (backHomeBtn) {
    backHomeBtn.addEventListener('click', resetToSetup);
  }

  function resetToSetup() {
    stopTimer();
    setupView.classList.add('active');
    quizView.classList.remove('active');
    resultView.classList.remove('active');
    quizFooter.style.display = 'none';
    restartNavBtn.style.display = 'none';
    reviewSection.style.display = 'none';
    renderHomeHistory(); // 刷新主页的历史记录与错题统计
  }

  function startQuiz() {
    // 获取选中的题量
    const checkedRadio = document.querySelector('input[name="quizCount"]:checked');
    const countValue = checkedRadio ? checkedRadio.value : '20';
    selectedCount = countValue === 'all' ? Number.POSITIVE_INFINITY : parseInt(countValue, 10);

    // 过滤题库
    let pool = [...allQuestions];
    if (selectedCategory !== 'all') {
      if (selectedCategory === '区域地理') {
        pool = pool.filter((q) => q.category === '中国地理' || q.category === '世界地理');
      } else {
        pool = pool.filter((q) => q.category === selectedCategory);
      }
    }

    if (pool.length === 0) {
      alert('所选题库范围内没有题目，请重新选择！');
      return;
    }

    // 题目随机打乱
    pool = shuffleArray(pool);

    // 截取指定数量
    const takeCount = Math.min(selectedCount, pool.length);
    const rawSelected = pool.slice(0, takeCount);

    // 处理每道题：同时把选项随机打乱，并重新映射正确答案索引
    currentQuizList = rawSelected.map((q) => {
      const originalOptions = q.options;
      const originalAnswerText = originalOptions[q.answer];

      // 打乱选项
      const shuffledOptions = shuffleArray(originalOptions);
      const newAnswerIndex = shuffledOptions.indexOf(originalAnswerText);

      return {
        id: q.id,
        category: q.category,
        book: q.book,
        question: q.question,
        options: shuffledOptions,
        answer: newAnswerIndex,
        answerText: originalAnswerText,
        explanation: q.explanation,
        image: sanitizeImagePath(q.image),
      };
    });

    currentIndex = 0;
    score = 0;
    answeredCount = 0;
    userHistory = [];

    // 切换视图
    setupView.classList.remove('active');
    resultView.classList.remove('active');
    quizView.classList.add('active');
    quizFooter.style.display = 'flex';
    restartNavBtn.style.display = 'inline-block';

    // 启动计时器
    startTimer();

    // 渲染第一题
    renderQuestion(0);
  }

  // 计时器控制
  function startTimer() {
    stopTimer();
    totalSeconds = 0;
    timerDisplay.textContent = '00:00';
    timerInterval = setInterval(() => {
      totalSeconds++;
      timerDisplay.textContent = formatTime(totalSeconds);
    }, 1000);
  }

  function stopTimer() {
    if (timerInterval) {
      clearInterval(timerInterval);
      timerInterval = null;
    }
  }

  // 渲染单道题
  function renderQuestion(index) {
    const q = currentQuizList[index];
    if (!q) return;

    // 顶部进度更新
    currentQNum.textContent = index + 1;
    totalQNum.textContent = currentQuizList.length;
    liveCorrectCount.textContent = score;
    liveAnsweredCount.textContent = answeredCount;
    const progressPercent = ((index + 1) / currentQuizList.length) * 100;
    progressFill.style.width = `${progressPercent}%`;

    // 标签与题干
    questionTagCategory.textContent = q.category;
    questionTagBook.textContent = q.book;
    questionOriginalId.textContent = `原题库 #${q.id}`;
    questionText.textContent = `${index + 1}. ${q.question}`;

    // 处理示意图片展示
    if (q.image) {
      questionImage.src = q.image;
      questionImageWrap.style.display = 'flex';
    } else {
      questionImageWrap.style.display = 'none';
      questionImage.src = '';
    }

    // 重置解析区
    analysisBox.style.display = 'none';
    footerHint.textContent = '请点击选项进行作答';
    nextBtn.disabled = true;

    // 如果是最后一题，下一题按钮显示为“查看最终成绩”
    if (index === currentQuizList.length - 1) {
      nextBtn.textContent = '完成测试 & 结算 🏁';
    } else {
      nextBtn.textContent = '下一题 ➔';
    }

    // 渲染4个选项按钮
    optionsContainer.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];

    q.options.forEach((optText, optIdx) => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      btn.dataset.index = optIdx;

      const keySpan = document.createElement('span');
      keySpan.className = 'opt-key';
      keySpan.textContent = letters[optIdx];
      const textSpan = document.createElement('span');
      textSpan.className = 'opt-text';
      textSpan.textContent = optText;
      btn.append(keySpan, textSpan);

      btn.addEventListener('click', () => handleOptionSelect(optIdx));
      optionsContainer.appendChild(btn);
    });
  }

  // 处理选项点击
  function handleOptionSelect(selectedIndex) {
    const q = currentQuizList[currentIndex];
    const optionButtons = optionsContainer.querySelectorAll('.option-btn');
    const letters = ['A', 'B', 'C', 'D'];

    // 禁用所有选项，防止重复点击
    optionButtons.forEach((btn) => (btn.disabled = true));

    const isCorrect = selectedIndex === q.answer;
    answeredCount++;
    if (isCorrect) score++;

    // 记录作答历史
    userHistory.push({
      questionIndex: currentIndex + 1,
      question: q.question,
      category: q.category,
      book: q.book,
      options: q.options,
      correctIndex: q.answer,
      selectedIndex: selectedIndex,
      isCorrect: isCorrect,
      explanation: q.explanation,
      image: q.image || null,
    });

    // 实时更新顶部统计
    liveCorrectCount.textContent = score;
    liveAnsweredCount.textContent = answeredCount;

    // 渲染选项高亮反馈
    optionButtons.forEach((btn, idx) => {
      if (idx === q.answer) {
        btn.classList.add('correct-ans');
      } else if (idx === selectedIndex) {
        btn.classList.add('wrong-ans');
      } else {
        btn.classList.add('dimmed');
      }
    });

    // 渲染即时解析框
    analysisBox.style.display = 'block';
    if (isCorrect) {
      analysisHeader.className = 'analysis-header correct';
      statusIcon.textContent = '✓';
      statusText.textContent = '回答正确！太棒了！';
      correctHint.textContent = `正确选项：${letters[q.answer]}`;
    } else {
      analysisHeader.className = 'analysis-header wrong';
      statusIcon.textContent = '✕';
      statusText.textContent = `回答错误！你选了 ${letters[selectedIndex]}`;
      correctHint.textContent = `正确选项为：${letters[q.answer]}`;
    }
    analysisText.textContent = q.explanation;

    // 激活右下角下一题按钮
    nextBtn.disabled = false;
    footerHint.textContent = '已展示深度解析，请点击右下角按钮继续 ➔';

    // 滚动使解析可见（若屏幕较小）
    analysisBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // 下一题按钮绑定
  nextBtn.addEventListener('click', () => {
    if (currentIndex < currentQuizList.length - 1) {
      currentIndex++;
      renderQuestion(currentIndex);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      // 最后一题结束，结算
      finishQuiz();
    }
  });

  // 键盘快捷键支持 (A/B/C/D 选答案, Enter/Space/N 下一题)
  document.addEventListener('keydown', (e) => {
    if (!quizView.classList.contains('active')) return;

    const key = e.key.toUpperCase();
    if (['A', 'B', 'C', 'D'].includes(key)) {
      const idx = ['A', 'B', 'C', 'D'].indexOf(key);
      const optionButtons = optionsContainer.querySelectorAll('.option-btn');
      if (optionButtons[idx] && !optionButtons[idx].disabled) {
        handleOptionSelect(idx);
      }
    } else if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowRight') {
      if (!nextBtn.disabled) {
        nextBtn.click();
      }
    }
  });

  // 结算成绩与报告
  function finishQuiz() {
    stopTimer();

    quizView.classList.remove('active');
    quizFooter.style.display = 'none';
    restartNavBtn.style.display = 'none';
    resultView.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });

    const total = currentQuizList.length;
    const accuracy = total > 0 ? Math.round((score / total) * 100) : 0;
    const wrongCount = total - score;

    finalScorePercent.textContent = `${accuracy}%`;
    resCorrect.textContent = score;
    resWrong.textContent = wrongCount;
    resTotal.textContent = total;
    resTime.textContent = formatTime(totalSeconds);

    // 智能评语
    let titleText = '测试完成！';
    let evaluationHtml = '';

    if (accuracy === 100) {
      titleText = '🏆 满分通关！地理全能学霸！';
      evaluationHtml = `<strong>太强了！全卷满分通关！</strong><br>你对高中地理全教材的自然地理原理、人文区位、区域协同与国家安全资源战略掌握得极其扎实通透，保持这种敏锐的题感，高考地理必拔头筹！`;
    } else if (accuracy >= 85) {
      titleText = '🌟 卓越优异！基础非常扎实！';
      evaluationHtml = `<strong>成绩非常优秀！</strong><br>绝大多数高考重难点核心知识已熟练掌握。建议重点回顾错题解析，扫清边缘易混淆考点，冲刺更高分！`;
    } else if (accuracy >= 70) {
      titleText = '👍 表现良好！稳中向好！';
      evaluationHtml = `<strong>整体基础良好！</strong><br>对大部分核心地理概念与区位原理理解到位。对于错题中涉及的自然规律综合推理（如气候、洋流、地质构造）可重点重温强化。`;
    } else {
      titleText = '💪 仍有很大提升空间！加油！';
      evaluationHtml = `<strong>完成了完整训练，收获颇丰！</strong><br>建议充分利用下方的错题回顾功能，仔细阅读每一道错题的深度解析，回归高中地理必修与选必教材的核心知识网络。`;
    }

    document.getElementById('resultTitle').textContent = titleText;
    resultEvaluation.innerHTML = evaluationHtml;

    // 保存本轮记录到 LocalStorage
    saveQuizHistoryRecord({
      date: new Date().toLocaleString('zh-CN', { hour12: false }),
      category: selectedCategory,
      total: total,
      score: score,
      wrongCount: wrongCount,
      accuracy: accuracy,
      timeSpent: formatTime(totalSeconds),
      seconds: totalSeconds,
      details: userHistory,
    });

    // 更新错题回顾标签数量
    tabCountAll.textContent = total;
    tabCountWrong.textContent = wrongCount;
    tabCountCorrect.textContent = score;

    renderReviewList('all');
  }

  // 错题回顾模块交互
  toggleReviewBtn.addEventListener('click', () => {
    const isShown = reviewSection.style.display === 'block';
    reviewSection.style.display = isShown ? 'none' : 'block';
    toggleReviewBtn.textContent = isShown
      ? '📖 查看全部做题记录与错题解析'
      : '🔼 收起试题详情与错题解析';
    if (!isShown) {
      reviewSection.scrollIntoView({ behavior: 'smooth' });
    }
  });

  const reviewFilterTabs = document.querySelectorAll('.review-filter-tabs .tab');
  reviewFilterTabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      reviewFilterTabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');
      renderReviewList(tab.dataset.filter);
    });
  });

  function renderReviewList(filter) {
    reviewList.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];

    let items = userHistory;
    if (filter === 'wrong') {
      items = userHistory.filter((item) => !item.isCorrect);
    } else if (filter === 'correct') {
      items = userHistory.filter((item) => item.isCorrect);
    }

    if (items.length === 0) {
      reviewList.innerHTML = `<div style="text-align:center; padding: 30px; color: var(--text-muted);">暂无符合筛选条件的试题记录</div>`;
      return;
    }

    items.forEach((item) => {
      const card = document.createElement('div');
      card.className = `review-item ${item.isCorrect ? 'is-correct' : 'is-wrong'}`;

      const statusTag = item.isCorrect
        ? '<span style="color: var(--success-color); font-weight: 700;">✓ 回答正确</span>'
        : '<span style="color: var(--danger-color); font-weight: 700;">✕ 回答错误</span>';

      const safeImage = sanitizeImagePath(item.image);
      const imageHtml = safeImage
        ? `<div class="review-q-img"><img src="${escapeHtml(safeImage)}" alt="试题示意图" /></div>`
        : '';

      card.innerHTML = `
        <div class="review-item-header">
          <span><strong>第 ${Number(item.questionIndex) || 0} 题</strong> [${escapeHtml(item.category)} · ${escapeHtml(item.book)}]</span>
          ${statusTag}
        </div>
        <div class="review-q-text">${escapeHtml(item.question)}</div>
        ${imageHtml}
        <div class="review-user-ans">
          <span>你的选择：<b>${letters[item.selectedIndex]}. ${escapeHtml(item.options[item.selectedIndex])}</b></span>
          ${
            !item.isCorrect
              ? `<span style="margin-left: 16px; color: var(--success-color);">标准答案：<b>${letters[item.correctIndex]}. ${escapeHtml(item.options[item.correctIndex])}</b></span>`
              : ''
          }
        </div>
        <div class="review-explanation">
          <strong>【官方深度解析】</strong><br>
          ${escapeHtml(item.explanation)}
        </div>
      `;

      reviewList.appendChild(card);
    });
  }

  // --- 本地持久化历史做题记录与错题本逻辑 ---
  const STORAGE_KEY = 'geo_quiz_history_logs';

  function getHistoryLogs() {
    try {
      const data = localStorage.getItem(STORAGE_KEY);
      const parsed = data ? JSON.parse(data) : [];
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function saveQuizHistoryRecord(record) {
    try {
      const logs = getHistoryLogs();
      logs.unshift(record); // 最新记录放最前面
      if (logs.length > 50) logs.pop(); // 保留最近50次
      localStorage.setItem(STORAGE_KEY, JSON.stringify(logs));
    } catch (e) {
      console.warn('LocalStorage save failed:', e);
    }
  }

  function renderHomeHistory() {
    if (!homeHistorySection) return;
    const logs = getHistoryLogs();

    homeHistorySection.style.display = 'block';

    const totalRounds = logs.length;
    const totalAnswered = logs.reduce((sum, r) => sum + (r.total || 0), 0);
    const totalCorrect = logs.reduce((sum, r) => sum + (r.score || 0), 0);
    const avgAcc = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;

    // 统计累计错题总数
    let allWrongItems = [];
    logs.forEach((log) => {
      if (log.details) {
        const wrongs = log.details.filter((d) => !d.isCorrect);
        allWrongItems.push(...wrongs);
      }
    });

    histTotalRounds.textContent = totalRounds;
    histTotalAnswered.textContent = totalAnswered;
    histAvgAccuracy.textContent = `${avgAcc}%`;
    histTotalWrongPool.textContent = allWrongItems.length;

    historyLogList.innerHTML = '';
    logs.slice(0, 10).forEach((log, idx) => {
      const item = document.createElement('div');
      item.className = 'history-item-card';

      const catText = log.category === 'all' ? '全部模块' : log.category;
      item.innerHTML = `
        <div class="hist-item-header">
          <span class="hist-date">🕒 ${escapeHtml(log.date)}</span>
          <span class="hist-tag">${escapeHtml(catText)} · ${Number(log.total) || 0}题</span>
        </div>
        <div class="hist-item-body">
          <div class="hist-stat-block">
            <span class="hist-acc-badge ${Number(log.accuracy) >= 80 ? 'good' : ''}">${Number(log.accuracy) || 0}% 正确率</span>
            <span class="hist-counts">${Number(log.score) || 0} 正确 / ${Number(log.wrongCount) || 0} 错误</span>
          </div>
          <div class="hist-time">⏱️ 耗时：${escapeHtml(log.timeSpent || '00:00')}</div>
        </div>
      `;
      historyLogList.appendChild(item);
    });
  }

  if (clearHistoryBtn) {
    clearHistoryBtn.addEventListener('click', () => {
      if (confirm('确定要清空所有的历史做题战绩与记录吗？')) {
        localStorage.removeItem(STORAGE_KEY);
        renderHomeHistory();
      }
    });
  }

  // --- 快速粘贴导入弹窗逻辑 ---
  const importModal = document.getElementById('importModal');
  const importPasteBtn = document.getElementById('importPasteBtn');
  const closeModalBtn = document.getElementById('closeModalBtn');
  const cancelModalBtn = document.getElementById('cancelModalBtn');
  const confirmImportBtn = document.getElementById('confirmImportBtn');
  const importTextarea = document.getElementById('importTextarea');

  if (importPasteBtn) {
    importPasteBtn.addEventListener('click', () => {
      importModal.style.display = 'flex';
      importTextarea.value = '';
      importTextarea.focus();
    });
  }

  function hideModal() {
    if (importModal) importModal.style.display = 'none';
  }

  if (closeModalBtn) closeModalBtn.addEventListener('click', hideModal);
  if (cancelModalBtn) cancelModalBtn.addEventListener('click', hideModal);

  if (confirmImportBtn) {
    confirmImportBtn.addEventListener('click', () => {
      const raw = importTextarea.value.trim();
      if (!raw) {
        alert('请先在文本框中粘贴试题数据！');
        return;
      }

      try {
        let imported = [];
        if (raw.startsWith('[') || raw.startsWith('{')) {
          const parsed = JSON.parse(raw);
          imported = Array.isArray(parsed) ? parsed : [parsed];
        } else {
          alert('请粘贴合法的 JSON 格式试题数组！');
          return;
        }

        if (imported.length === 0) {
          alert('未能识别到有效试题！');
          return;
        }

        const maxId = allQuestions.reduce((max, q) => Math.max(max, Number(q.id) || 0), 0);
        const normalized = imported.map((q, i) => {
          if (!q || typeof q !== 'object' || Array.isArray(q)) {
            throw new Error(`第 ${i + 1} 项不是题目对象`);
          }
          if (typeof q.question !== 'string' || !q.question.trim()) {
            throw new Error(`第 ${i + 1} 题缺少题干`);
          }
          if (
            !Array.isArray(q.options) ||
            q.options.length !== 4 ||
            q.options.some((option) => typeof option !== 'string' || !option.trim()) ||
            new Set(q.options.map((option) => option.trim())).size !== 4
          ) {
            throw new Error(`第 ${i + 1} 题必须有 4 个互不重复的非空选项`);
          }
          if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer > 3) {
            throw new Error(`第 ${i + 1} 题答案必须是 0、1、2 或 3`);
          }
          if (typeof q.explanation !== 'string' || !q.explanation.trim()) {
            throw new Error(`第 ${i + 1} 题缺少解析`);
          }
          if (q.image && !sanitizeImagePath(q.image)) {
            throw new Error(`第 ${i + 1} 题图片路径无效，只允许 images/ 下的本地图片`);
          }
          return {
            id: maxId + i + 1,
            category: typeof q.category === 'string' && q.category.trim() ? q.category.trim() : '自然地理',
            book: typeof q.book === 'string' && q.book.trim() ? q.book.trim() : '综合',
            question: q.question.trim(),
            options: q.options.map((option) => option.trim()),
            answer: q.answer,
            explanation: q.explanation.trim(),
            image: sanitizeImagePath(q.image),
          };
        });
        allQuestions.push(...normalized);
        updateQuestionCounts();

        alert(`🎉 成功导入了 ${imported.length} 道新试题！当前题库已达 ${allQuestions.length} 道！`);
        hideModal();
        resetToSetup();
      } catch (err) {
        alert(`解析失败，请检查 JSON 格式是否正确：\n${err.message}`);
      }
    });
  }

  // 页面加载完成后初始化
  updateQuestionCounts();
  initTheme();
  renderHomeHistory();
})();
