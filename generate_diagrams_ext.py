# -*- coding: utf-8 -*-
"""
生成高质量的高中地理示意矢量图 (扩充至40+张，支持60+道试题图文配对)
"""

import os

images_dir = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(images_dir, exist_ok=True)

def save_svg(filename, content):
    filepath = os.path.join(images_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

# 26. 暖锋天气系统示意图
save_svg("warm_front.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">暖锋天气系统结构与连续性降水区域示意图</text>
  <line x1="0" y1="240" x2="600" y2="240" stroke="#334155" stroke-width="2.5"/>
  <rect x="0" y="240" width="600" height="60" fill="#e2e8f0"/>
  <!-- 锋面平缓爬升 -->
  <path d="M 120 240 L 480 80" fill="none" stroke="#dc2626" stroke-width="3.5"/>
  <!-- 暖气团主动爬升 -->
  <path d="M 0 240 L 120 240 L 480 80 L 0 80 Z" fill="#fee2e2" opacity="0.7"/>
  <text x="140" y="160" font-size="15" font-weight="bold" fill="#dc2626">暖气团 (主动爬升)</text>
  <!-- 冷气团后退回流 -->
  <text x="440" y="200" font-size="14" font-weight="bold" fill="#1e40af">冷气团 (被迫后退)</text>
  <!-- 锋前雨区 -->
  <rect x="330" y="250" width="150" height="24" rx="4" fill="#0284c7"/>
  <text x="405" y="267" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">🌧️ 降水主要在【锋前】(连续性阴雨)</text>
</svg>""")

# 27. 准静止锋天气示意图 (江淮梅雨)
save_svg("stationary_front.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">准静止锋（江淮梅雨 / 华南准静止锋）示意图</text>
  <!-- 冷暖气团势力相当相持不下 -->
  <g transform="translate(60, 60)">
    <rect x="0" y="40" width="200" height="120" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
    <text x="100" y="90" font-size="15" font-weight="bold" fill="#1e40af" text-anchor="middle">北方南下冷气团</text>
    <path d="M 120 120 L 220 120" fill="none" stroke="#2563eb" stroke-width="4"/>
    <polygon points="220,120 208,114 208,126" fill="#2563eb"/>

    <rect x="280" y="40" width="200" height="120" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="380" y="90" font-size="15" font-weight="bold" fill="#dc2626" text-anchor="middle">南方北上暖湿气团</text>
    <path d="M 360 120 L 260 120" fill="none" stroke="#dc2626" stroke-width="4"/>
    <polygon points="260,120 272,114 272,126" fill="#dc2626"/>

    <rect x="180" y="170" width="120" height="30" rx="4" fill="#0284c7"/>
    <text x="240" y="190" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">持续连绵阴雨</text>
  </g>
  <rect x="50" y="250" width="500" height="26" rx="4" fill="#f1f5f9"/>
  <text x="300" y="268" font-size="11" fill="#334155" text-anchor="middle">势均力敌、移动缓慢，带来初夏江淮梅雨（6-7月长达月余阴雨）</text>
</svg>""")

# 28. 北半球气旋（低压）水平辐合与上升示意图
save_svg("cyclone.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">北半球气旋（低压中心）气流运动与降水示意图</text>
  <circle cx="300" cy="150" r="40" fill="#bae6fd" stroke="#0284c7" stroke-width="2"/>
  <text x="300" y="156" font-size="20" font-weight="bold" fill="#0369a1" text-anchor="middle">低 (L)</text>
  <circle cx="300" cy="150" r="80" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
  <circle cx="300" cy="150" r="120" fill="none" stroke="#94a3b8" stroke-width="1.5"/>

  <!-- 逆时针向中心辐合 -->
  <path d="M 380 60 Q 320 80 320 110" fill="none" stroke="#dc2626" stroke-width="3"/>
  <polygon points="320,110 325,98 315,100" fill="#dc2626"/>

  <path d="M 420 180 Q 380 200 340 180" fill="none" stroke="#dc2626" stroke-width="3"/>
  <polygon points="340,180 352,185 348,175" fill="#dc2626"/>

  <text x="300" y="280" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">水平方向：逆时针辐合；垂直方向：中心强上升气流 ➔ 阴雨/台风天气</text>
</svg>""")

# 29. 资源跨区域调配（西气东输 / 南水北调 / 西电东送）战略图
save_svg("resource_transfer.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">我国重大资源跨区域调配战略工程示意图</text>
  <g transform="translate(60, 50)">
    <!-- 西部输出区 -->
    <rect x="0" y="30" width="160" height="120" rx="8" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
    <text x="80" y="70" font-size="14" font-weight="bold" fill="#854d0e" text-anchor="middle">西部资源富集区</text>
    <text x="80" y="95" font-size="11" fill="#a16207" text-anchor="middle">(能源/水电/天然气充足)</text>
    <text x="80" y="125" font-size="11" font-weight="bold" fill="#16a34a" text-anchor="middle">资源优势 ➔ 经济优势</text>

    <!-- 东部受水/受电区 -->
    <rect x="320" y="30" width="160" height="120" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
    <text x="400" y="70" font-size="14" font-weight="bold" fill="#1e40af" text-anchor="middle">东部经济发达区</text>
    <text x="400" y="95" font-size="11" fill="#1d4ed8" text-anchor="middle">(能源/水资源需求缺口大)</text>
    <text x="400" y="125" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">缓解能源紧张/改善环境</text>

    <!-- 输送箭头 -->
    <path d="M 160 80 L 320 80" fill="none" stroke="#dc2626" stroke-width="5"/>
    <polygon points="320,80 308,73 308,87" fill="#dc2626"/>
    <text x="240" y="70" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">西气东输 / 西电东送</text>
  </g>
</svg>""")

# 30. 碳循环与碳达峰碳中和路径图
save_svg("carbon_neutral.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#15803d" text-anchor="middle">碳达峰与碳中和（双碳战略）目标与路径示意图</text>
  <g transform="translate(60, 50)">
    <!-- 碳排放源 -->
    <rect x="0" y="40" width="180" height="80" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
    <text x="90" y="70" font-size="13" font-weight="bold" fill="#991b1b" text-anchor="middle">化石能源排放源</text>
    <text x="90" y="95" font-size="11" fill="#b91c1c" text-anchor="middle">(煤炭/石油燃烧 CO2)</text>

    <!-- 碳吸收汇 -->
    <rect x="300" y="40" width="180" height="80" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
    <text x="390" y="70" font-size="13" font-weight="bold" fill="#166534" text-anchor="middle">生态系统碳汇</text>
    <text x="390" y="95" font-size="11" fill="#15803d" text-anchor="middle">(森林植被/海洋碳汇/CCUS)</text>

    <!-- 动态平衡 -->
    <rect x="120" y="150" width="240" height="36" rx="6" fill="#15803d"/>
    <text x="240" y="173" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">碳中和：人为排放量 ＝ 人为吸收量</text>
  </g>
</svg>""")

# 31. 世界交通咽喉马六甲海峡位置图
save_svg("strait_of_malacca.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f0f9ff" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0369a1" text-anchor="middle">马六甲海峡——世界航运“十字路口”示意图</text>
  <!-- 马来半岛 (上) 与 苏门答腊岛 (下) -->
  <polygon points="120,45 380,45 340,110 180,110" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="260" y="80" font-size="13" font-weight="bold" fill="#9a3412">马来半岛</text>

  <polygon points="160,180 440,180 400,245 120,245" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>
  <text x="280" y="215" font-size="13" font-weight="bold" fill="#166534">苏门答腊岛</text>

  <!-- 中间狭长海峡 -->
  <rect x="180" y="125" width="200" height="40" rx="4" fill="#38bdf8"/>
  <text x="280" y="150" font-size="13" font-weight="bold" fill="#0c4a6e" text-anchor="middle">【马六甲海峡】</text>

  <text x="70" y="150" font-size="13" font-weight="bold" fill="#2563eb">太平洋 ➔</text>
  <text x="470" y="150" font-size="13" font-weight="bold" fill="#2563eb">➔ 印度洋</text>
</svg>""")

# 32. 中东波斯湾石油外运航线图
save_svg("persian_gulf_oil.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#fffbeb" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#78350f" text-anchor="middle">中东波斯湾石油产区与霍尔木兹海峡输出示意图</text>
  <rect x="140" y="60" width="220" height="120" rx="8" fill="#fed7aa" stroke="#ea580c" stroke-width="2"/>
  <text x="250" y="110" font-size="15" font-weight="bold" fill="#9a3412" text-anchor="middle">波斯湾石油集聚区</text>
  <text x="250" y="135" font-size="11" fill="#c2410c" text-anchor="middle">世界石油储量/产量最大</text>

  <!-- 霍尔木兹海峡 -->
  <path d="M 360 120 L 450 120" fill="none" stroke="#dc2626" stroke-width="5"/>
  <polygon points="450,120 438,114 438,126" fill="#dc2626"/>
  <text x="410" y="105" font-size="12" font-weight="bold" fill="#dc2626">霍尔木兹海峡 (世界油阀)</text>

  <rect x="420" y="160" width="120" height="70" rx="6" fill="#bae6fd"/>
  <text x="480" y="195" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">外运至东亚</text>
  <text x="480" y="215" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">西欧与北美</text>
</svg>""")

# 33. 水体富营养化与赤潮发生机制图
save_svg("eutrophication_red_tide.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#dc2626" text-anchor="middle">水体富营养化与赤潮（水华）发生机制示意图</text>
  <g transform="translate(60, 50)" font-size="12">
    <!-- 步骤1 -->
    <rect x="0" y="30" width="140" height="60" rx="6" fill="#fee2e2" stroke="#dc2626"/>
    <text x="70" y="55" font-weight="bold" fill="#991b1b" text-anchor="middle">工农业与生活污水</text>
    <text x="70" y="75" fill="#b91c1c" text-anchor="middle">大量含【氮、磷】营养物</text>

    <!-- 步骤2 -->
    <rect x="170" y="30" width="140" height="60" rx="6" fill="#fef08a" stroke="#ca8a04"/>
    <text x="240" y="55" font-weight="bold" fill="#854d0e" text-anchor="middle">适宜水温与光照</text>
    <text x="240" y="75" fill="#a16207" text-anchor="middle">藻类暴发性疯狂繁殖</text>

    <!-- 步骤3 -->
    <rect x="340" y="30" width="140" height="60" rx="6" fill="#dbeafe" stroke="#2563eb"/>
    <text x="410" y="55" font-weight="bold" fill="#1e40af" text-anchor="middle">耗尽水中溶解氧</text>
    <text x="410" y="75" fill="#1d4ed8" text-anchor="middle">水生生物窒息死亡</text>
  </g>
  <rect x="60" y="160" width="480" height="80" rx="8" fill="#f87171" opacity="0.3"/>
  <text x="300" y="205" font-size="14" font-weight="bold" fill="#991b1b" text-anchor="middle">🌊 赤潮（海洋） / 水华（淡水湖泊）生态危机</text>
</svg>""")

# 34. 酸雨形成与降落示意图
save_svg("acid_rain.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#f8fafc" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#0f172a" text-anchor="middle">酸雨（pH &lt; 5.6）形成过程与环境危害示意图</text>
  <g transform="translate(60, 50)">
    <!-- 工业排放 -->
    <rect x="0" y="40" width="150" height="70" rx="6" fill="#fed7aa" stroke="#ea580c"/>
    <text x="75" y="70" font-size="13" font-weight="bold" fill="#9a3412" text-anchor="middle">煤炭燃油排放</text>
    <text x="75" y="92" font-size="12" font-weight="bold" fill="#dc2626" text-anchor="middle">SO2 与 NOx 气体</text>

    <!-- 云层转化 -->
    <ellipse cx="270" cy="50" rx="55" ry="25" fill="#94a3b8"/>
    <text x="270" y="55" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">氧化结合水汽</text>
    <text x="270" y="90" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">生成硫酸/硝酸</text>

    <!-- 酸雨降落 -->
    <line x1="270" y1="105" x2="270" y2="180" stroke="#dc2626" stroke-width="3" stroke-dasharray="4,4"/>
    <rect x="200" y="190" width="140" height="30" rx="4" fill="#fee2e2"/>
    <text x="270" y="210" font-size="12" font-weight="bold" fill="#991b1b" text-anchor="middle">🌧️ 酸雨 (pH &lt; 5.6)</text>
  </g>
</svg>""")

# 35. 臭氧层破坏与紫外线辐射增强图
save_svg("ozone_depletion.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" width="100%" height="100%">
  <rect width="600" height="300" fill="#090d16" rx="12"/>
  <text x="300" y="26" font-size="15" font-weight="bold" fill="#f8fafc" text-anchor="middle">平流层臭氧层破坏与紫外线吸收减弱示意图</text>
  <!-- 太阳紫外线 -->
  <circle cx="60" cy="80" r="30" fill="#f59e0b"/>
  <text x="60" y="85" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">太阳</text>
  <!-- 臭氧层 -->
  <rect x="140" y="90" width="400" height="40" rx="4" fill="#38bdf8" opacity="0.6"/>
  <text x="340" y="115" font-size="13" font-weight="bold" fill="#0369a1" text-anchor="middle">平流层臭氧层 (吸收大部分紫外线)</text>

  <!-- 氟氯烃破坏孔洞 -->
  <ellipse cx="440" cy="110" rx="40" ry="20" fill="#090d16" stroke="#ef4444" stroke-width="2"/>
  <text x="440" y="115" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">臭氧空洞</text>
  <text x="440" y="145" font-size="10" fill="#f87171">氟氯烃(CFCs)破坏</text>

  <!-- 紫外线直达地面 -->
  <path d="M 440 120 L 440 230" fill="none" stroke="#fbbf24" stroke-width="4"/>
  <polygon points="440,230 434,218 446,218" fill="#fbbf24"/>
  <text x="440" y="250" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">过量有害紫外线直射地表</text>
</svg>""")

print("Successfully generated additional 10 high-school geography SVGs (total 35 SVGs).")
