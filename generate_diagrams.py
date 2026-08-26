# -*- coding: utf-8 -*-
"""
批量生成高中地理 60+ 张高质量专业矢量示意图 (SVG)
覆盖范围：
必修一（自然地理基础要素）
必修二（人文地理与城乡发展）
选择性必修1（自然地理基础原理与动力）
选择性必修2（区域发展与跨区域协同）
选择性必修3（资源环境与国家安全）
区域地理微专题（中国地理与世界地理）
"""

import os

images_dir = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(images_dir, exist_ok=True)

def save_svg(filename, content):
    filepath = os.path.join(images_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

# 1. 太阳系八大行星轨道位置图
save_svg("solar_system.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#090d16" rx="12"/>
  <text x="300" y="28" font-size="15" font-weight="bold" fill="#f8fafc" text-anchor="middle">太阳系结构与八大行星轨道位置示意图</text>
  <!-- 太阳 -->
  <circle cx="40" cy="150" r="50" fill="#f59e0b" stroke="#fbbf24" stroke-width="3"/>
  <text x="40" y="155" font-size="12" fill="#fff" font-weight="bold" text-anchor="middle">太阳</text>
  <!-- 轨道弧线与行星 -->
  <!-- 水星 -->
  <ellipse cx="40" cy="150" rx="80" ry="60" fill="none" stroke="#334155" stroke-dasharray="3,3"/>
  <circle cx="120" cy="150" r="5" fill="#94a3b8"/>
  <text x="120" y="170" font-size="10" fill="#94a3b8" text-anchor="middle">水星</text>
  <!-- 金星 -->
  <ellipse cx="40" cy="150" rx="130" ry="75" fill="none" stroke="#334155" stroke-dasharray="3,3"/>
  <circle cx="170" cy="150" r="8" fill="#fde047"/>
  <text x="170" y="175" font-size="10" fill="#fde047" text-anchor="middle">金星</text>
  <!-- 地球 -->
  <ellipse cx="40" cy="150" rx="180" ry="90" fill="none" stroke="#38bdf8" stroke-dasharray="4,2"/>
  <circle cx="220" cy="150" r="9" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="220" y="180" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">地球(3)</text>
  <!-- 火星 -->
  <ellipse cx="40" cy="150" rx="230" ry="105" fill="none" stroke="#334155" stroke-dasharray="3,3"/>
  <circle cx="270" cy="150" r="7" fill="#ef4444"/>
  <text x="270" y="175" font-size="10" fill="#ef4444" text-anchor="middle">火星</text>
  <!-- 小行星带 -->
  <path d="M 300 40 Q 330 150 300 260" fill="none" stroke="#ca8a04" stroke-width="6" stroke-dasharray="2,5"/>
  <text x="315" y="275" font-size="10" fill="#facc15">小行星带</text>
  <!-- 木星 -->
  <circle cx="360" cy="150" r="22" fill="#d97706"/>
  <text x="360" y="190" font-size="11" fill="#fed7aa" text-anchor="middle">木星(巨行星)</text>
  <!-- 土星 -->
  <circle cx="430" cy="150" r="16" fill="#fef08a"/>
  <ellipse cx="430" cy="150" rx="26" ry="7" fill="none" stroke="#ca8a04" stroke-width="3"/>
  <text x="430" y="185" font-size="11" fill="#fef08a" text-anchor="middle">土星</text>
  <!-- 天王星 -->
  <circle cx="500" cy="150" r="12" fill="#67e8f9"/>
  <text x="500" y="180" font-size="10" fill="#67e8f9" text-anchor="middle">天王星</text>
  <!-- 海王星 -->
  <circle cx="560" cy="150" r="12" fill="#3b82f6"/>
  <text x="560" y="180" font-size="10" fill="#93c5fd" text-anchor="middle">海王星</text>
  <rect x="40" y="235" width="520" height="28" rx="4" fill="#1e293b"/>
  <text x="300" y="253" font-size="11" fill="#94a3b8" text-anchor="middle">小行星带位于【火星轨道】与【木星轨道】之间；类地行星包括水、金、地、火。</text>
</svg>""")

# 2. 太阳大气层分层结构图
save_svg("sun_atmosphere.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#090d16" rx="12"/>
  <text x="300" y="28" font-size="15" font-weight="bold" fill="#f8fafc" text-anchor="middle">太阳大气分层与主要太阳活动示意图</text>
  <!-- 太阳内部到外部三层 -->
  <g transform="translate(100, 30)">
    <!-- 日冕层 -->
    <circle cx="80" cy="120" r="110" fill="#ca8a04" opacity="0.3"/>
    <!-- 色球层 -->
    <circle cx="80" cy="120" r="80" fill="#ea580c" opacity="0.7"/>
    <!-- 光球层 -->
    <circle cx="80" cy="120" r="55" fill="#fde047"/>
    <!-- 太阳内部 -->
    <circle cx="80" cy="120" r="30" fill="#f59e0b"/>
  </g>
  <!-- 文字标注 -->
  <g font-size="13" fill="#f8fafc">
    <!-- 光球层 -->
    <line x1="225" y1="130" x2="310" y2="100" stroke="#fde047" stroke-width="2"/>
    <text x="320" y="105" font-weight="bold" fill="#fde047">① 光球层（最里层，肉眼可见）</text>
    <text x="340" y="125" font-size="11" fill="#94a3b8">主要太阳活动：【黑子】（温度较低区域）</text>

    <!-- 色球层 -->
    <line x1="250" y1="150" x2="310" y2="160" stroke="#ea580c" stroke-width="2"/>
    <text x="320" y="165" font-weight="bold" fill="#fb923c">② 色球层（中间层）</text>
    <text x="340" y="185" font-size="11" fill="#94a3b8">主要太阳活动：【耀斑】、【日珥】（剧烈能量释放）</text>

    <!-- 日冕层 -->
    <line x1="280" y1="190" x2="310" y2="220" stroke="#ca8a04" stroke-width="2"/>
    <text x="320" y="225" font-weight="bold" fill="#facc15">③ 日冕层（最外层，极度稀薄）</text>
    <text x="340" y="245" font-size="11" fill="#94a3b8">主要太阳活动：【日冕物质抛射 / 太阳风】</text>
  </g>
</svg>""")

# 3. 大气垂直分层示意图
save_svg("atmosphere_layers.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">大气垂直分层与气温垂直变化示意图</text>
  <!-- 坐标轴 -->
  <line x1="80" y1="260" x2="550" y2="260" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="260" x2="80" y2="40" stroke="#334155" stroke-width="2"/>
  <text x="550" y="278" font-size="11" fill="#64748b">气温 (℃)</text>
  <text x="75" y="38" font-size="11" fill="#64748b" text-anchor="end">高度 (km)</text>

  <!-- 高度分界线 -->
  <line x1="80" y1="200" x2="550" y2="200" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <line x1="80" y1="110" x2="550" y2="110" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <text x="50" y="205" font-size="11" fill="#0284c7">约12km</text>
  <text x="50" y="115" font-size="11" fill="#0284c7">约50km</text>

  <!-- 气温曲线 -->
  <!-- 对流层：随高度降低 -->
  <line x1="280" y1="260" x2="160" y2="200" stroke="#ef4444" stroke-width="3"/>
  <!-- 平流层：随高度升高 -->
  <line x1="160" y1="200" x2="260" y2="110" stroke="#ef4444" stroke-width="3"/>
  <!-- 高层大气：先降后升 -->
  <path d="M 260 110 L 140 60 L 320 40" fill="none" stroke="#ef4444" stroke-width="3"/>

  <!-- 文字说明 -->
  <text x="380" y="235" font-size="13" font-weight="bold" fill="#0284c7">【对流层】(对流旺盛，天气复杂)</text>
  <text x="380" y="160" font-size="13" font-weight="bold" fill="#059669">【平流层】(臭氧层吸紫外线，利于飞行)</text>
  <text x="380" y="80" font-size="13" font-weight="bold" fill="#6366f1">【高层大气】(电离层反射无线电短波)</text>
</svg>""")

# 4. 海水盐度与纬度分布双峰曲线图
save_svg("ocean_salinity_curve.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0369a1" text-anchor="middle">大洋表层海水盐度随纬度分布曲线图</text>
  <line x1="60" y1="240" x2="550" y2="240" stroke="#334155" stroke-width="2"/>
  <line x1="60" y1="240" x2="60" y2="40" stroke="#334155" stroke-width="2"/>
  <!-- 纬度刻度 -->
  <text x="80" y="258" font-size="11" fill="#64748b">60°S</text>
  <text x="180" y="258" font-size="11" fill="#64748b">30°S</text>
  <text x="300" y="258" font-size="11" font-weight="bold" fill="#dc2626">赤道 (0°)</text>
  <text x="420" y="258" font-size="11" fill="#64748b">30°N</text>
  <text x="520" y="258" font-size="11" fill="#64748b">60°N</text>

  <!-- 盐度双峰曲线 -->
  <path d="M 80 200 Q 180 60 300 130 Q 420 50 520 210" fill="none" stroke="#2563eb" stroke-width="4"/>
  <circle cx="180" cy="88" r="5" fill="#dc2626"/>
  <text x="180" y="75" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">副热带高盐区</text>
  <circle cx="420" cy="80" r="5" fill="#dc2626"/>
  <text x="420" y="68" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">副热带高盐区</text>
  <circle cx="300" cy="130" r="5" fill="#0284c7"/>
  <text x="300" y="155" font-size="11" fill="#0284c7" text-anchor="middle">赤道多雨鞍部</text>

  <rect x="50" y="268" width="500" height="24" rx="4" fill="#e0f2fe"/>
  <text x="300" y="284" font-size="11" fill="#0369a1" text-anchor="middle">规律：从副热带海区向南北两侧的高低纬度递减（副热带蒸发量远大于降水量）</text>
</svg>""")

# 5. 河流出山口冲积扇示意图
save_svg("alluvial_fan.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#1e293b" text-anchor="middle">河流出山口冲积扇形态与沉积颗粒分选示意图</text>
  <!-- 山地出山口 -->
  <polygon points="40,240 160,80 260,240" fill="#cbd5e1" stroke="#64748b" stroke-width="2"/>
  <text x="160" y="140" font-size="14" font-weight="bold" fill="#334155" text-anchor="middle">山 地 峡 谷</text>
  <!-- 扇顶扇中扇缘扇形 -->
  <path d="M 230 180 L 520 90 A 260 260 0 0 1 520 270 Z" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
  <!-- 水流分叉 -->
  <path d="M 230 180 Q 350 140 500 120" fill="none" stroke="#0284c7" stroke-width="3"/>
  <path d="M 230 180 Q 380 180 520 180" fill="none" stroke="#0284c7" stroke-width="3.5"/>
  <path d="M 230 180 Q 350 220 500 240" fill="none" stroke="#0284c7" stroke-width="3"/>

  <!-- 分选颗粒标注 -->
  <text x="270" y="170" font-size="11" font-weight="bold" fill="#9a3412">扇顶：砾石/粗砂</text>
  <text x="370" y="210" font-size="11" font-weight="bold" fill="#b45309">扇中：细砂/粉砂</text>
  <text x="470" y="275" font-size="11" font-weight="bold" fill="#15803d">扇缘：黏土 (地下水溢出带)</text>
</svg>""")

# 6. 河口三角洲与牛轭湖地貌示意图
save_svg("river_delta_oxbow.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0369a1" text-anchor="middle">河流入海口三角洲与平原牛轭湖发育示意图</text>
  <!-- 左：平原牛轭湖 -->
  <g transform="translate(30, 50)">
    <text x="120" y="20" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">【平原河曲与牛轭湖】</text>
    <path d="M 20 60 Q 120 60 120 120 Q 120 180 20 180" fill="none" stroke="#38bdf8" stroke-width="12"/>
    <!-- 截弯取直新河道 -->
    <line x1="20" y1="60" x2="20" y2="180" stroke="#0284c7" stroke-width="10"/>
    <text x="140" y="125" font-size="11" font-weight="bold" fill="#dc2626">废弃曲流 ➔ 牛轭湖</text>
  </g>
  <!-- 右：河口三角洲 -->
  <g transform="translate(320, 50)">
    <text x="120" y="20" font-size="13" font-weight="bold" fill="#0369a1" text-anchor="middle">【河口三角洲】</text>
    <!-- 海洋与泥沙堆积体 -->
    <rect x="140" y="40" width="100" height="180" fill="#bae6fd" rx="4"/>
    <polygon points="20,130 140,50 140,210" fill="#fed7aa" stroke="#ca8a04" stroke-width="2"/>
    <text x="190" y="135" font-size="13" font-weight="bold" fill="#0369a1">海洋</text>
    <text x="80" y="135" font-size="12" font-weight="bold" fill="#9a3412">泥沙三角洲</text>
  </g>
</svg>""")

# 7. 土壤剖面分层结构图
save_svg("soil_profile.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#1e293b" text-anchor="middle">成熟森林土壤垂直剖面分层示意图</text>
  <g transform="translate(100, 45)">
    <!-- 有机层/枯枝落叶层 -->
    <rect x="0" y="0" width="180" height="30" fill="#3f2e1a"/>
    <text x="200" y="20" font-size="12" font-weight="bold" fill="#3f2e1a">① 有机质层（枯枝落叶与未完全分解有机质）</text>

    <!-- 腐殖质层 -->
    <rect x="0" y="30" width="180" height="50" fill="#5c4033"/>
    <text x="200" y="60" font-size="12" font-weight="bold" fill="#5c4033">② 腐殖质层（肥力最高，深黑/暗褐色）</text>

    <!-- 淋溶层 -->
    <rect x="0" y="80" width="180" height="45" fill="#d2b48c"/>
    <text x="200" y="105" font-size="12" font-weight="bold" fill="#854d0e">③ 淋溶层（水溶性矿物随水下渗淋失，色浅）</text>

    <!-- 淀积层 -->
    <rect x="0" y="125" width="180" height="55" fill="#a0522d"/>
    <text x="200" y="155" font-size="12" font-weight="bold" fill="#a0522d">④ 淀积层（上层淋溶物质在此集聚粘化）</text>

    <!-- 母质层与基岩 -->
    <rect x="0" y="180" width="180" height="50" fill="#808080"/>
    <text x="200" y="210" font-size="12" font-weight="bold" fill="#4b5563">⑤ 成土母质层 / 基岩（风化碎屑矿物质源头）</text>
  </g>
</svg>""")

# 8. 板块构造边界类型（生长边界 vs 消亡边界）图
save_svg("plate_boundaries.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">板块边界类型（生长边界与消亡边界）示意图</text>
  <!-- 左：生长边界（张裂） -->
  <g transform="translate(30, 50)">
    <text x="120" y="20" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">【生长边界（张裂分离）】</text>
    <rect x="20" y="80" width="90" height="70" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
    <rect x="130" y="80" width="90" height="70" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
    <path d="M 50 115 L 10 115" fill="none" stroke="#dc2626" stroke-width="3"/>
    <polygon points="10,115 20,110 20,120" fill="#dc2626"/>
    <path d="M 190 115 L 230 115" fill="none" stroke="#dc2626" stroke-width="3"/>
    <polygon points="230,115 220,110 220,120" fill="#dc2626"/>
    <text x="120" y="180" font-size="11" fill="#7c2d12" text-anchor="middle">形成：裂谷 / 海洋 / 大洋中脊</text>
  </g>

  <!-- 右：消亡边界（碰撞挤压） -->
  <g transform="translate(320, 50)">
    <text x="120" y="20" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">【消亡边界（碰撞挤压）】</text>
    <!-- 大陆板块与大洋板块俯冲 -->
    <polygon points="120,70 180,40 230,140 120,140" fill="#cbd5e1" stroke="#334155" stroke-width="2"/>
    <polygon points="10,100 130,140 110,160 0,110" fill="#93c5fd" stroke="#2563eb" stroke-width="2"/>
    <text x="190" y="110" font-size="11" font-weight="bold" fill="#1e293b">褶皱山系</text>
    <text x="100" y="180" font-size="11" font-weight="bold" fill="#1e40af">海沟俯冲带</text>
  </g>
</svg>""")

# 9. 人口金字塔三种类型图 (增长型、静止型、缩减型)
save_svg("population_pyramids.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">人口年龄结构金字塔的三种基本类型</text>
  <!-- 1. 年轻型/扩张型 -->
  <g transform="translate(30, 50)">
    <text x="80" y="20" font-size="13" font-weight="bold" fill="#16a34a" text-anchor="middle">① 年轻型 (扩张型)</text>
    <polygon points="80,40 10,210 150,210" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
    <text x="80" y="235" font-size="11" fill="#15803d" text-anchor="middle">底宽顶窄 · 出生率高</text>
  </g>
  <!-- 2. 成年型/静止型 -->
  <g transform="translate(220, 50)">
    <text x="80" y="20" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">② 成年型 (静止型)</text>
    <polygon points="40,40 120,40 130,210 30,210" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/>
    <text x="80" y="235" font-size="11" fill="#1e40af" text-anchor="middle">各年龄段比例匀称</text>
  </g>
  <!-- 3. 老年型/缩减型 -->
  <g transform="translate(410, 50)">
    <text x="80" y="20" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">③ 老年型 (收缩型)</text>
    <polygon points="40,60 120,60 140,130 110,210 50,210 20,130" fill="#fecaca" stroke="#dc2626" stroke-width="2"/>
    <text x="80" y="235" font-size="11" fill="#991b1b" text-anchor="middle">底窄顶宽 · 老龄化严重</text>
  </g>
</svg>""")

# 10. 城市化发展S型阶段曲线图
save_svg("urbanization_s_curve.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#1e293b" text-anchor="middle">世界城镇化进程“S”形发展阶段曲线图</text>
  <line x1="80" y1="240" x2="540" y2="240" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="240" x2="80" y2="40" stroke="#334155" stroke-width="2"/>
  <text x="545" y="245" font-size="11" fill="#64748b">时间</text>
  <text x="75" y="38" font-size="11" fill="#64748b" text-anchor="end">城镇化水平 (%)</text>

  <!-- 30% 和 70% 界线 -->
  <line x1="80" y1="180" x2="540" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="55" y="185" font-size="11" fill="#64748b">30%</text>
  <line x1="80" y1="90" x2="540" y2="90" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="55" y="95" font-size="11" fill="#64748b">70%</text>

  <!-- S型曲线 -->
  <path d="M 80 230 Q 180 220 250 160 T 420 80 L 520 70" fill="none" stroke="#2563eb" stroke-width="4"/>

  <!-- 三个阶段标注 -->
  <text x="150" y="210" font-size="12" font-weight="bold" fill="#0284c7">初期阶段 (&lt;30%)</text>
  <text x="270" y="130" font-size="12" font-weight="bold" fill="#dc2626">加速阶段 (30%-70%)</text>
  <text x="440" y="60" font-size="12" font-weight="bold" fill="#16a34a">后期成熟阶段 (&gt;70%)</text>
</svg>""")

# 11. 工业区位主导指向型雷达分类图
save_svg("industry_orientation.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">工业五大主导区位指向类型示意图</text>
  <g transform="translate(60, 45)" font-size="12">
    <!-- 1. 原料指向型 -->
    <rect x="0" y="10" width="220" height="38" rx="6" fill="#fed7aa" stroke="#ea580c"/>
    <text x="110" y="34" font-weight="bold" fill="#9a3412" text-anchor="middle">🍎 原料导向型 (如制糖厂、水产加工)</text>

    <!-- 2. 市场指向型 -->
    <rect x="0" y="60" width="220" height="38" rx="6" fill="#dbeafe" stroke="#2563eb"/>
    <text x="110" y="84" font-weight="bold" fill="#1e40af" text-anchor="middle">🍺 市场导向型 (如啤酒厂、家具制造)</text>

    <!-- 3. 动力指向型 -->
    <rect x="0" y="110" width="220" height="38" rx="6" fill="#fef08a" stroke="#ca8a04"/>
    <text x="110" y="134" font-weight="bold" fill="#854d0e" text-anchor="middle">⚡ 动力导向型 (如电解铝、重化工)</text>

    <!-- 4. 劳动力指向型 -->
    <rect x="260" y="35" width="220" height="38" rx="6" fill="#dcfce7" stroke="#16a34a"/>
    <text x="370" y="59" font-weight="bold" fill="#166534" text-anchor="middle">🧵 劳动力导向型 (如普通服装组装)</text>

    <!-- 5. 技术指向型 -->
    <rect x="260" y="90" width="220" height="38" rx="6" fill="#f3e8ff" stroke="#9333ea"/>
    <text x="370" y="114" font-weight="bold" fill="#6b21a8" text-anchor="middle">🔬 技术导向型 (如集成电路、航空航天)</text>
  </g>
  <rect x="40" y="240" width="520" height="30" rx="4" fill="#e2e8f0"/>
  <text x="300" y="260" font-size="12" fill="#334155" text-anchor="middle">主导原则：选址在投入产出综合成本最低、经济与环境综合效益最大的地点。</text>
</svg>""")

# 12. 各种交通运输方式运费与距离关系图
save_svg("transport_cost_distance.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#1e293b" text-anchor="middle">主要交通运输方式运费随运输距离变化曲线图</text>
  <line x1="80" y1="240" x2="540" y2="240" stroke="#334155" stroke-width="2"/>
  <line x1="80" y1="240" x2="80" y2="40" stroke="#334155" stroke-width="2"/>
  <text x="545" y="245" font-size="11" fill="#64748b">运输距离</text>
  <text x="75" y="38" font-size="11" fill="#64748b" text-anchor="end">运费</text>

  <!-- 公路 (短途最低) -->
  <line x1="80" y1="200" x2="480" y2="60" stroke="#ef4444" stroke-width="3"/>
  <text x="440" y="55" font-size="11" font-weight="bold" fill="#ef4444">公路运输</text>

  <!-- 铁路 (中长途优势) -->
  <line x1="80" y1="160" x2="520" y2="100" stroke="#2563eb" stroke-width="3"/>
  <text x="490" y="95" font-size="11" font-weight="bold" fill="#2563eb">铁路运输</text>

  <!-- 水运 (长途最低) -->
  <line x1="80" y1="120" x2="540" y2="130" stroke="#059669" stroke-width="3"/>
  <text x="500" y="145" font-size="11" font-weight="bold" fill="#059669">水路运输</text>

  <!-- 区间标注 -->
  <rect x="80" y="250" width="90" height="25" fill="#fee2e2" rx="4"/>
  <text x="125" y="267" font-size="11" fill="#991b1b" text-anchor="middle">短途选公路</text>

  <rect x="175" y="250" width="160" height="25" fill="#dbeafe" rx="4"/>
  <text x="255" y="267" font-size="11" fill="#1e40af" text-anchor="middle">中长途选铁路</text>

  <rect x="340" y="250" width="180" height="25" fill="#d1fae5" rx="4"/>
  <text x="430" y="267" font-size="11" fill="#065f46" text-anchor="middle">大宗远距离选水运</text>
</svg>""")

# 13. 混合农业生产循环模式图（澳大利亚墨累-达令盆地）
save_svg("mixed_farming_cycle.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#15803d" text-anchor="middle">澳大利亚墨累-达令盆地小麦-牧羊混合农业良性循环示意图</text>
  <!-- 麦田与牧场左右 -->
  <g transform="translate(60, 55)">
    <!-- 小麦种植 -->
    <rect x="0" y="20" width="180" height="80" rx="8" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
    <text x="90" y="55" font-size="14" font-weight="bold" fill="#854d0e" text-anchor="middle">🌾 小麦种植业</text>
    <text x="90" y="75" font-size="11" fill="#a16207" text-anchor="middle">秸秆 / 饲料作物</text>

    <!-- 牧羊业 -->
    <rect x="300" y="20" width="180" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="390" y="55" font-size="14" font-weight="bold" fill="#166534" text-anchor="middle">🐑 绵羊饲养业</text>
    <text x="390" y="75" font-size="11" fill="#15803d" text-anchor="middle">羊粪 / 优质有机肥</text>

    <!-- 循环箭头 -->
    <path d="M 180 50 L 300 50" fill="none" stroke="#ca8a04" stroke-width="3"/>
    <polygon points="300,50 290,45 290,55" fill="#ca8a04"/>
    <text x="240" y="42" font-size="11" fill="#ca8a04" text-anchor="middle">秸秆作饲料</text>

    <path d="M 300 80 L 180 80" fill="none" stroke="#16a34a" stroke-width="3"/>
    <polygon points="180,80 190,75 190,85" fill="#16a34a"/>
    <text x="240" y="98" font-size="11" fill="#16a34a" text-anchor="middle">羊粪肥田</text>

    <!-- 市场调控 -->
    <rect x="150" y="140" width="180" height="40" rx="6" fill="#dbeafe" stroke="#2563eb"/>
    <text x="240" y="165" font-size="13" font-weight="bold" fill="#1e40af" text-anchor="middle">📊 国际农产品市场</text>
  </g>
</svg>""")

# 14. 地方时与时区经度计算示意图
save_svg("timezone_calculation.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">经度差与地方时换算规律示意图</text>
  <!-- 经度数轴 -->
  <line x1="60" y1="140" x2="540" y2="140" stroke="#334155" stroke-width="3"/>
  <polygon points="540,140 530,135 530,145" fill="#334155"/>
  <text x="545" y="145" font-size="12" font-weight="bold" fill="#2563eb">东 (时间早/加)</text>
  <text x="50" y="145" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="end">西 (时间晚/减)</text>

  <!-- 0度经线 (伦敦) -->
  <line x1="200" y1="110" x2="200" y2="170" stroke="#64748b" stroke-width="2"/>
  <text x="200" y="100" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">0° 本初子午线</text>
  <text x="200" y="190" font-size="13" font-weight="bold" fill="#0284c7" text-anchor="middle">4:00 (格林尼治时间)</text>

  <!-- 120度E (北京时间经线) -->
  <line x1="440" y1="110" x2="440" y2="170" stroke="#dc2626" stroke-width="3"/>
  <text x="440" y="100" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">120°E 经线</text>
  <text x="440" y="190" font-size="13" font-weight="bold" fill="#dc2626" text-anchor="middle">12:00 (正午地方时)</text>

  <!-- 相差经度与时间 -->
  <path d="M 200 130 Q 320 80 440 130" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="320" y="75" font-size="12" font-weight="bold" fill="#2563eb" text-anchor="middle">经度差 120° ➔ 时差 120°÷15°/h = 8 小时 (东加西减)</text>
</svg>""")

# 15. 地转偏向力偏转规律图
save_svg("coriolis_force.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">地球自转偏向力在南、北半球的偏转规律示意图</text>
  <!-- 赤道 -->
  <line x1="60" y1="150" x2="540" y2="150" stroke="#dc2626" stroke-width="2"/>
  <text x="545" y="155" font-size="12" font-weight="bold" fill="#dc2626">赤道 (0° 无偏转)</text>

  <!-- 北半球向右偏 -->
  <g transform="translate(100, 60)">
    <text x="80" y="0" font-size="13" font-weight="bold" fill="#2563eb" text-anchor="middle">【北半球：顺运动方向向右偏】</text>
    <line x1="80" y1="70" x2="80" y2="20" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 80 70 Q 80 40 120 20" fill="none" stroke="#2563eb" stroke-width="4"/>
    <polygon points="120,20 108,24 114,32" fill="#2563eb"/>
    <text x="130" y="35" font-size="11" fill="#2563eb">实际风向(右偏)</text>
  </g>

  <!-- 南半球向左偏 -->
  <g transform="translate(360, 170)">
    <text x="80" y="100" font-size="13" font-weight="bold" fill="#059669" text-anchor="middle">【南半球：顺运动方向向左偏】</text>
    <line x1="80" y1="20" x2="80" y2="70" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3,3"/>
    <path d="M 80 20 Q 80 50 120 70" fill="none" stroke="#059669" stroke-width="4"/>
    <polygon points="120,70 114,58 108,66" fill="#059669"/>
    <text x="130" y="65" font-size="11" fill="#059669">实际风向(左偏)</text>
  </g>
</svg>""")

# 16. 地球公转轨道近日点与远日点示意图
save_svg("earth_perihelion_aphelion.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#090d16" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#f8fafc" text-anchor="middle">地球公转轨道近日点与远日点速度变化示意图</text>
  <!-- 太阳偏心位置 -->
  <circle cx="240" cy="150" r="28" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
  <text x="240" y="155" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">太阳</text>
  <!-- 椭圆轨道 -->
  <ellipse cx="300" cy="150" rx="220" ry="90" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="5,4"/>

  <!-- 左：近日点 (1月初) -->
  <g transform="translate(80, 150)">
    <circle cx="0" cy="0" r="14" fill="#38bdf8"/>
    <text x="0" y="-22" font-size="12" font-weight="bold" fill="#fde047" text-anchor="middle">【近日点】(1月初)</text>
    <text x="0" y="30" font-size="11" fill="#f87171" text-anchor="middle">公转角速度/线速度【最快】</text>
  </g>

  <!-- 右：远日点 (7月初) -->
  <g transform="translate(520, 150)">
    <circle cx="0" cy="0" r="14" fill="#38bdf8"/>
    <text x="0" y="-22" font-size="12" font-weight="bold" fill="#93c5fd" text-anchor="middle">【远日点】(7月初)</text>
    <text x="0" y="30" font-size="11" fill="#93c5fd" text-anchor="middle">公转角速度/线速度【最慢】</text>
  </g>
</svg>""")

# 17. 地中海气候降水气温柱状折线图
save_svg("climate_mediterranean.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">地中海气候（北半球）气温与降水量特征图</text>
  <!-- 坐标轴 -->
  <line x1="80" y1="230" x2="520" y2="230" stroke="#334155" stroke-width="2"/>
  <text x="300" y="250" font-size="11" fill="#64748b" text-anchor="middle">1月 至 12月 (月份)</text>
  <!-- 夏季高温少雨，冬季温和多雨 -->
  <!-- 降水柱状 (冬多夏少) -->
  <g fill="#38bdf8">
    <rect x="100" y="110" width="18" height="120"/>
    <rect x="130" y="125" width="18" height="105"/>
    <rect x="160" y="150" width="18" height="80"/>
    <rect x="190" y="180" width="18" height="50"/>
    <rect x="220" y="215" width="18" height="15"/>
    <rect x="250" y="222" width="18" height="8"/>
    <rect x="280" y="225" width="18" height="5"/>
    <rect x="310" y="220" width="18" height="10"/>
    <rect x="340" y="195" width="18" height="35"/>
    <rect x="370" y="160" width="18" height="70"/>
    <rect x="400" y="130" width="18" height="100"/>
    <rect x="430" y="105" width="18" height="125"/>
  </g>
  <!-- 气温曲线 (夏季高冬季温和) -->
  <path d="M 110 170 Q 280 60 440 170" fill="none" stroke="#dc2626" stroke-width="3.5"/>
  <text x="280" y="55" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">夏季炎热干燥 (受副高控制)</text>
  <text x="110" y="90" font-size="11" font-weight="bold" fill="#0284c7">冬季温和多雨 (受西风控制)</text>
</svg>""")

# 18. 理想大陆气候类型与气压带风带分布模式图
save_svg("ideal_continent_climates.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="24" font-size="14" font-weight="bold" fill="#0f172a" text-anchor="middle">理想大陆气候类型与气压带风带对应模式图</text>
  <!-- 理想大陆框架 -->
  <rect x="150" y="45" width="300" height="230" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
  <line x1="150" y1="275" x2="450" y2="275" stroke="#dc2626" stroke-width="2"/>
  <text x="460" y="278" font-size="10" fill="#dc2626">0° (赤道多雨带)</text>
  <line x1="150" y1="200" x2="450" y2="200" stroke="#ea580c" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="460" y="205" font-size="10" fill="#ea580c">30°N (副热带高压)</text>
  <line x1="150" y1="120" x2="450" y2="120" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="460" y="125" font-size="10" fill="#0284c7">60°N (盛行西风带)</text>

  <!-- 气候填色 -->
  <!-- 热带雨林 -->
  <rect x="150" y="245" width="300" height="30" fill="#15803d"/>
  <text x="300" y="265" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">热带雨林气候</text>

  <!-- 西岸温带海洋 -->
  <rect x="150" y="80" width="100" height="80" fill="#38bdf8"/>
  <text x="200" y="125" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">温带海洋性</text>

  <!-- 西岸地中海 -->
  <rect x="150" y="160" width="100" height="50" fill="#fde047"/>
  <text x="200" y="190" font-size="11" font-weight="bold" fill="#854d0e" text-anchor="middle">地中海气候</text>

  <!-- 东岸季风 -->
  <rect x="350" y="120" width="100" height="90" fill="#fed7aa"/>
  <text x="400" y="170" font-size="11" font-weight="bold" fill="#9a3412" text-anchor="middle">季风气候区</text>
</svg>""")

# 19. 世界大洋中低纬度洋流环流模式图
save_svg("ocean_current_gyre.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f0f9ff" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0369a1" text-anchor="middle">世界大洋中低纬度环流模式（北顺南逆）示意图</text>
  <!-- 赤道 -->
  <line x1="40" y1="150" x2="560" y2="150" stroke="#dc2626" stroke-width="2"/>
  <text x="50" y="145" font-size="11" font-weight="bold" fill="#dc2626">赤道 (0°)</text>

  <!-- 北半球顺时针环流 -->
  <g transform="translate(300, 90)">
    <ellipse cx="0" cy="0" rx="140" ry="45" fill="none" stroke="#334155" stroke-width="1.5"/>
    <text x="0" y="5" font-size="13" font-weight="bold" fill="#1e40af" text-anchor="middle">北半球：【顺时针】副热带大洋环流</text>
    <!-- 西侧暖流 (红) -->
    <path d="M -140 30 L -140 -20" fill="none" stroke="#dc2626" stroke-width="4"/>
    <polygon points="-140,-20 -146,-10 -134,-10" fill="#dc2626"/>
    <text x="-150" y="0" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="end">暖流(西岸)</text>

    <!-- 东侧寒流 (蓝) -->
    <path d="M 140 -20 L 140 30" fill="none" stroke="#0284c7" stroke-width="4"/>
    <polygon points="140,30 134,20 146,20" fill="#0284c7"/>
    <text x="150" y="0" font-size="11" font-weight="bold" fill="#0284c7">寒流(东岸)</text>
  </g>

  <!-- 南半球逆时针环流 -->
  <g transform="translate(300, 210)">
    <ellipse cx="0" cy="0" rx="140" ry="45" fill="none" stroke="#334155" stroke-width="1.5"/>
    <text x="0" y="5" font-size="13" font-weight="bold" fill="#059669" text-anchor="middle">南半球：【逆时针】副热带大洋环流</text>
  </g>
</svg>""")

# 20. 秘鲁上升流与渔场成因示意图
save_svg("peru_upwelling.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0369a1" text-anchor="middle">离岸信风与上升补偿流（秘鲁渔场）形成示意图</text>
  <!-- 南美大陆与海洋 -->
  <polygon points="420,70 580,70 580,260 420,260" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="500" y="160" font-size="15" font-weight="bold" fill="#9a3412" text-anchor="middle">南美大陆</text>
  <!-- 海洋水体 -->
  <rect x="40" y="100" width="380" height="160" fill="#7dd3fc" opacity="0.8"/>

  <!-- 离岸东南信风 (从陆吹向海) -->
  <path d="M 460 90 L 320 90" fill="none" stroke="#2563eb" stroke-width="4"/>
  <polygon points="320,90 332,84 332,96" fill="#2563eb"/>
  <text x="390" y="80" font-size="12" font-weight="bold" fill="#2563eb">离岸风 (东南信风)</text>

  <!-- 表层海水离岸流动 -->
  <path d="M 400 120 L 220 120" fill="none" stroke="#0369a1" stroke-width="3"/>
  <polygon points="220,120 230,115 230,125" fill="#0369a1"/>
  <text x="300" y="140" font-size="11" fill="#0369a1">表层海水离岸而去</text>

  <!-- 深层上升补偿流 -->
  <path d="M 160 240 Q 360 240 380 140" fill="none" stroke="#dc2626" stroke-width="4"/>
  <polygon points="380,140 374,152 386,150" fill="#dc2626"/>
  <text x="240" y="220" font-size="12" font-weight="bold" fill="#dc2626">深层冷海水上升补偿 (带来丰富营养盐类)</text>
  <text x="320" y="165" font-size="12" font-weight="bold" fill="#15803d">🐟 浮游生物繁盛 ➔ 世界大渔场</text>
</svg>""")

# 21. 厄尔尼诺海温异常示意图
save_svg("el_nino_pattern.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#dc2626" text-anchor="middle">厄尔尼诺现象发生时赤道太平洋海气相互作用示意图</text>
  <!-- 西太平洋(印尼/澳洲) 与 东太平洋(南美西岸) -->
  <rect x="40" y="160" width="110" height="90" fill="#bbf7d0" rx="6"/>
  <text x="95" y="200" font-size="12" font-weight="bold" fill="#166534" text-anchor="middle">西太平洋</text>
  <text x="95" y="220" font-size="10" fill="#dc2626" text-anchor="middle">下沉气流 · 干旱山火</text>

  <rect x="450" y="160" width="110" height="90" fill="#fed7aa" rx="6"/>
  <text x="505" y="200" font-size="12" font-weight="bold" fill="#9a3412" text-anchor="middle">东太平洋 (南美)</text>
  <text x="505" y="220" font-size="10" fill="#2563eb" text-anchor="middle">上升气流 · 暴雨洪涝</text>

  <!-- 沃克环流逆转 -->
  <ellipse cx="300" cy="110" rx="150" ry="40" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="300" y="105" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">东南信风减弱 · 东太平洋水温异常升高</text>
</svg>""")

# 22. 山地垂直自然带谱示意图 (珠峰南坡与北坡对比)
save_svg("mountain_vertical_zones.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">珠穆朗玛峰垂直自然带谱与南、北坡雪线对比示意图</text>
  <!-- 山峰三角形 -->
  <polygon points="300,60 100,250 500,250" fill="#e2e8f0" stroke="#334155" stroke-width="2"/>
  <text x="180" y="240" font-size="13" font-weight="bold" fill="#2563eb">南坡 (迎风坡/阳坡)</text>
  <text x="420" y="240" font-size="13" font-weight="bold" fill="#64748b">北坡 (背风坡/阴坡)</text>

  <!-- 雪线虚线 (南坡低，北坡高) -->
  <line x1="220" y1="130" x2="300" y2="100" stroke="#38bdf8" stroke-width="3"/>
  <line x1="300" y1="100" x2="380" y2="90" stroke="#38bdf8" stroke-width="3"/>
  <text x="170" y="125" font-size="11" font-weight="bold" fill="#0284c7">南坡雪线更低 (迎风坡降雪多)</text>
  <text x="430" y="85" font-size="11" font-weight="bold" fill="#64748b">北坡雪线较高</text>

  <!-- 自然带分层 -->
  <line x1="160" y1="190" x2="300" y2="150" stroke="#16a34a" stroke-width="2"/>
  <text x="160" y="180" font-size="11" fill="#15803d">常绿阔叶林带(基带丰富)</text>
</svg>""")

# 23. 黄土高原小流域综合治理示意图
save_svg("loess_watershed.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#fffbeb" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#92400e" text-anchor="middle">黄土高原小流域综合治理模式（保塬、护坡、固沟）示意图</text>
  <!-- 塬面、缓坡、沟谷 -->
  <g transform="translate(60, 50)">
    <!-- 塬面 -->
    <rect x="0" y="30" width="140" height="40" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
    <text x="70" y="55" font-size="12" font-weight="bold" fill="#78350f" text-anchor="middle">【塬面】保塬工程</text>
    <text x="70" y="85" font-size="10" fill="#b45309" text-anchor="middle">平整土地 · 营造护田林网</text>

    <!-- 缓坡 -->
    <polygon points="140,30 280,120 280,160 140,70" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
    <text x="210" y="90" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">【坡面】护坡工程</text>
    <text x="210" y="125" font-size="10" fill="#166534" text-anchor="middle">修筑水平梯田 · 封坡育草</text>

    <!-- 沟谷 -->
    <polygon points="280,120 440,160 440,200 280,160" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
    <text x="360" y="150" font-size="12" font-weight="bold" fill="#9a3412" text-anchor="middle">【沟谷】固沟工程</text>
    <text x="360" y="185" font-size="10" fill="#c2410c" text-anchor="middle">打坝淤地 · 建设拦沙蓄水坝</text>
  </g>
</svg>""")

# 24. 中国四大地理分区图
save_svg("china_four_regions.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">中国四大地理区域划分与分界线示意图</text>
  <!-- 四大块 -->
  <!-- 西北干旱半干旱区 -->
  <rect x="60" y="45" width="220" height="100" rx="8" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
  <text x="170" y="90" font-size="14" font-weight="bold" fill="#854d0e" text-anchor="middle">西北地区</text>
  <text x="170" y="110" font-size="11" fill="#a16207" text-anchor="middle">(干旱 · 灌溉农业/绿洲农业)</text>

  <!-- 北方地区 -->
  <rect x="300" y="45" width="240" height="100" rx="8" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="420" y="90" font-size="14" font-weight="bold" fill="#9a3412" text-anchor="middle">北方地区</text>
  <text x="420" y="110" font-size="11" fill="#c2410c" text-anchor="middle">(半湿润 · 旱地耕作 · 小麦)</text>

  <!-- 青藏高寒区 -->
  <rect x="60" y="160" width="220" height="110" rx="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="2"/>
  <text x="170" y="205" font-size="14" font-weight="bold" fill="#4338ca" text-anchor="middle">青藏地区</text>
  <text x="170" y="225" font-size="11" fill="#4f46e5" text-anchor="middle">(高寒 · 河谷农业 · 青稞)</text>

  <!-- 南方地区 -->
  <rect x="300" y="160" width="240" height="110" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="420" y="205" font-size="14" font-weight="bold" fill="#166534" text-anchor="middle">南方地区</text>
  <text x="420" y="225" font-size="11" fill="#15803d" text-anchor="middle">(湿热 · 水田耕作 · 水稻)</text>

  <line x1="300" y1="152" x2="540" y2="152" stroke="#dc2626" stroke-width="3"/>
  <text x="420" y="150" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">秦岭—淮河线 (1月0℃ / 800mm)</text>
</svg>""")

# 25. 中国地势三级阶梯剖面图
save_svg("china_topography_steps.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">中国地势三级阶梯自西向东阶梯剖面示意图</text>
  <!-- 阶梯台阶 -->
  <!-- 第一级阶梯 (青藏高原 >4000m) -->
  <polygon points="60,70 200,70 200,240 60,240" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="130" y="110" font-size="13" font-weight="bold" fill="#9a3412" text-anchor="middle">第一级阶梯</text>
  <text x="130" y="135" font-size="11" fill="#c2410c" text-anchor="middle">青藏高原 (&gt;4000m)</text>

  <!-- 第二级阶梯 (1000-2000m) -->
  <polygon points="200,130 380,130 380,240 200,240" fill="#fde68a" stroke="#ca8a04" stroke-width="2"/>
  <text x="290" y="165" font-size="13" font-weight="bold" fill="#854d0e" text-anchor="middle">第二级阶梯</text>
  <text x="290" y="185" font-size="11" fill="#a16207" text-anchor="middle">四大高原/四大盆地</text>

  <!-- 第三级阶梯 (<500m 平原丘陵) -->
  <polygon points="380,190 540,190 540,240 380,240" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
  <text x="460" y="215" font-size="13" font-weight="bold" fill="#15803d" text-anchor="middle">第三级阶梯</text>
  <text x="460" y="232" font-size="10" fill="#166534" text-anchor="middle">东北/华北/长江中下游平原</text>

  <!-- 水能集中界线 -->
  <text x="200" y="60" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">昆仑-祁连-横断</text>
  <text x="380" y="120" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">大兴安岭-太行-巫山-雪峰</text>
</svg>""")

print("Generated comprehensive 25 SVG educational diagrams.")
