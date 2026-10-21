# 產生「西拉雅建築探險」可列印圖卡 HTML（A4，含裁切線）
B, R, K, Y, G, D = "#2f5aa8", "#e8452c", "#1f2a2a", "#f4b223", "#d9b44a", "#1f4a3e"
GR = "#5aa05a"

def svg(body):
    return f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def flower(cx, cy, r, fill, hole="none"):
    petals = "".join(
        f'<ellipse cx="{cx}" cy="{cy - r*0.55}" rx="{r*0.22}" ry="{r*0.45}" fill="{fill}" transform="rotate({i*45} {cx} {cy})"/>'
        for i in range(8))
    return petals + f'<circle cx="{cx}" cy="{cy}" r="{r*0.18}" fill="{hole if hole != "none" else "#fff"}"/>'

def jar(x, y, s, fill):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-9,-30 h18 v6 q16,8 16,28 q0,24 -25,26 q-25,-2 -25,-26 q0,-20 16,-28 z" fill="{fill}" stroke="{K}" stroke-width="2"/>'
            f'<rect x="-11" y="-34" width="22" height="6" rx="2" fill="{K}"/>'
            f'<path d="M-18,4 h36" stroke="#fff" stroke-width="3"/></g>')

ICON = {
"sun": svg(f'<circle cx="50" cy="50" r="20" fill="{R}"/>' + "".join(
    f'<line x1="50" y1="14" x2="50" y2="24" stroke="{R}" stroke-width="5" stroke-linecap="round" transform="rotate({i*30} 50 50)"/>' for i in range(12))),
"wind": svg("".join(
    f'<path d="M12,{y} h{w} q14,0 14,-10 q0,-9 -9,-9 q-8,0 -8,8" fill="none" stroke="{B}" stroke-width="6" stroke-linecap="round"/>'
    for y, w in ((38, 50), (58, 64), (78, 40)))),
"water": svg(f'<path d="M50,10 q30,40 30,58 a30,30 0 0 1 -60,0 q0,-18 30,-58z" fill="{B}"/><path d="M36,66 a14,14 0 0 0 12,14" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/>'),
"jar": svg(jar(50, 58, 1.35, R)),
"flower": svg(flower(50, 50, 40, R)),
"rest": svg(f'<rect x="18" y="30" width="64" height="44" rx="8" fill="{GR}"/><rect x="26" y="20" width="48" height="16" rx="6" fill="{GR}"/><text x="50" y="62" font-size="18" text-anchor="middle" fill="#fff">Z z z</text>'),
# 關卡
"m1": svg(f'<path d="M10,62 q40,-34 80,0 z" fill="{GR}"/><rect x="18" y="62" width="64" height="26" fill="#ddd" stroke="{K}" stroke-width="2"/><rect x="30" y="68" width="12" height="20" fill="{B}"/><rect x="56" y="68" width="16" height="10" fill="{Y}"/>' + "".join(f'<path d="M{x},50 l3,-8 l3,8" stroke="#2d7a2d" stroke-width="2" fill="none"/>' for x in (30, 44, 58, 70))),
"m2": svg(jar(22, 62, .8, B) + jar(50, 58, .95, R) + jar(78, 62, .8, K)),
"m3": svg(f'<path d="M6,30 l22,-14 l22,14 l22,-14 l22,14" fill="none" stroke="{K}" stroke-width="4"/><path d="M42,30 l-14,52 h44 l-14,-52z" fill="{Y}" opacity=".45"/>' + flower(50, 84, 16, Y)),
"m4": svg(f'<path d="M6,40 l22,-16 l22,16 l22,-16 l22,16" fill="none" stroke="{K}" stroke-width="4"/><line x1="16" y1="40" x2="16" y2="90" stroke="{K}" stroke-width="4"/><line x1="84" y1="40" x2="84" y2="90" stroke="{K}" stroke-width="4"/>' + "".join(
    f'<path d="M24,{y} h40 q10,0 10,-7" fill="none" stroke="{B}" stroke-width="4" stroke-linecap="round"/>' for y in (60, 74))),
"m5": svg(f'<rect x="8" y="20" width="40" height="12" fill="{K}"/><rect x="8" y="32" width="40" height="58" fill="#ccc"/><rect x="48" y="78" width="46" height="12" fill="{B}"/><path d="M44,24 q16,4 14,54" stroke="{B}" stroke-width="7" fill="none"/><path d="M14,26 h30" stroke="{B}" stroke-width="5"/>'),
"m6": svg("".join(f'<rect x="{10+(i%3)*28}" y="{12+(i//3)*28}" width="24" height="24" rx="4" fill="{c}" stroke="{K}" stroke-width="1.5"/>'
    for i, c in enumerate((B, "#fff", R, K, Y, G, GR, "#8cc6ee", "#b07a45")))),
# 路線底卡
"bike": svg(f'<circle cx="26" cy="68" r="16" fill="none" stroke="{R}" stroke-width="4"/><circle cx="76" cy="68" r="16" fill="none" stroke="{R}" stroke-width="4"/><path d="M26,68 l18,-26 h26 l6,26 M44,42 l12,26 l14,-26" fill="none" stroke="{K}" stroke-width="4"/><circle cx="52" cy="22" r="7" fill="{R}"/><path d="M52,29 l-4,14 l10,8" stroke="{B}" stroke-width="5" fill="none"/>'),
"hills": svg(f'<path d="M0,70 q20,-40 40,-10 q20,-40 60,0 v30 h-100z" fill="{GR}"/><path d="M0,80 h100 v20 h-100z" fill="{B}"/><circle cx="80" cy="22" r="10" fill="{R}"/>'),
"clouds": svg(f'<path d="M0,60 l30,-30 l25,22 l20,-14 l25,22 v40 h-100z" fill="{D}"/><path d="M0,80 h100 v20 h-100z" fill="{B}"/><g fill="#fff" stroke="#bbb"><ellipse cx="30" cy="48" rx="22" ry="8"/><ellipse cx="72" cy="40" rx="18" ry="7"/></g>'),
# 小圖卡
"cypress": svg("".join(f'<path d="M{x},55 l8,-40 l8,40z" fill="{c}"/><path d="M{x},62 l8,32 l8,-32z" fill="{c}" opacity=".45"/>' for x, c in ((12, R), (32, B), (52, R), (72, B))) + f'<line x1="0" y1="58" x2="100" y2="58" stroke="{B}" stroke-width="2"/>'),
"caltrop": svg(f'<path d="M50,40 q-20,0 -40,-14 q12,20 6,34 q20,0 34,-6 q14,6 34,6 q-6,-14 6,-34 q-20,14 -40,14z" fill="{K}"/><rect x="0" y="74" width="100" height="26" fill="{B}" opacity=".5"/>'),
"statue": svg(f'<rect x="22" y="76" width="56" height="16" fill="#999"/><circle cx="50" cy="24" r="10" fill="{K}"/><path d="M38,38 h24 l4,22 h10 v16 h-52 v-16 h10z" fill="{R}"/><path d="M40,60 l-6,16 M60,60 l6,16" stroke="{K}" stroke-width="5"/>'),
"fossil": svg(f'<ellipse cx="50" cy="82" rx="38" ry="8" fill="{K}"/><path d="M20,70 q10,-36 34,-36 q16,0 26,-14" fill="none" stroke="{R}" stroke-width="5"/>' + "".join(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+14}" stroke="{R}" stroke-width="3"/>' for x, y in ((30, 46), (38, 40), (46, 36), (54, 36))) + f'<path d="M30,58 v20 M58,40 v38" stroke="{R}" stroke-width="4"/>'),
"ice": svg(f'<path d="M14,52 h72 q-6,30 -36,32 q-30,-2 -36,-32z" fill="{B}"/>' + "".join(f'<rect x="{x}" y="{y}" width="14" height="14" fill="{Y}" stroke="{R}" stroke-width="1.5" transform="rotate(15 {x} {y})"/>' for x, y in ((24, 32), (42, 26), (58, 34), (36, 40), (52, 42))) + f'<circle cx="50" cy="20" r="9" fill="{R}"/>'),
"bridge": svg(f'<rect x="0" y="74" width="100" height="26" fill="{B}"/><line x1="22" y1="20" x2="22" y2="74" stroke="{K}" stroke-width="5"/><line x1="78" y1="20" x2="78" y2="74" stroke="{K}" stroke-width="5"/><path d="M0,40 q22,-20 22,-20 q28,40 56,0 q22,20 22,20" fill="none" stroke="{R}" stroke-width="3"/><line x1="0" y1="60" x2="100" y2="60" stroke="{K}" stroke-width="4"/>' + "".join(f'<line x1="{x}" y1="{36+abs(50-x)/2.2 if 22<x<78 else 40}" x2="{x}" y2="60" stroke="{R}" stroke-width="1.5"/>' for x in range(30, 76, 8))),
"horse": svg(f'<path d="M24,40 h40 l10,-20 l12,6 l-6,10 l-6,4 v20 h-58z" fill="{R}"/>' + "".join(f'<rect x="{x}" y="60" width="7" height="28" fill="{K}"/>' for x in (24, 34, 50, 60)) + "".join(f'<rect x="{x}" y="{y}" width="8" height="8" fill="{c}"/>' for x, y, c in ((30, 44, B), (46, 44, K), (38, 52, B), (56, 50, B), (70, 28, K)))),
"gate": svg(f'<rect x="8" y="22" width="84" height="12" fill="{R}"/><path d="M4,22 l10,-10 h72 l10,10z" fill="{K}"/><rect x="16" y="34" width="10" height="56" fill="{R}"/><rect x="74" y="34" width="10" height="56" fill="{R}"/><ellipse cx="50" cy="72" rx="22" ry="14" fill="{B}"/><text x="50" y="80" font-size="22" text-anchor="middle" fill="#fff" font-weight="bold">佛</text>'),
"hotspring": svg(f'<ellipse cx="50" cy="72" rx="40" ry="16" fill="{K}"/><ellipse cx="50" cy="72" rx="30" ry="10" fill="#8cc6ee"/>' + "".join(f'<path d="M{x},54 q-8,-10 0,-20 q8,-10 0,-22" fill="none" stroke="{R}" stroke-width="4" stroke-linecap="round"/>' for x in (36, 50, 64))),
"dam": svg(f'<path d="M0,40 l30,-20 l20,14 l20,-10 l30,16 v20 h-100z" fill="{D}"/><rect x="0" y="54" width="100" height="16" fill="{B}"/><path d="M0,70 h100 l-14,26 h-72z" fill="#bbb" stroke="{K}" stroke-width="2"/>'),
"bingo": "",
}

def card(icon, title, sub="", cls=""):
    return f'<div class="card {cls}"><div class="ic">{ICON[icon]}</div><div class="t">{title}</div><div class="s">{sub}</div></div>'

def color_card(color, name, sub=""):
    border = f"border:1.5px solid {K};" if color == "#fff" else ""
    return f'<div class="card"><div class="sw" style="background:{color};{border}"></div><div class="t">{name}</div><div class="s">{sub}</div></div>'

def page(title, grid, cards, note=""):
    return f'<section class="page"><h1>{title}</h1><div class="grid {grid}">{"".join(cards)}</div><p class="note">{note}</p></section>'

pages = [
 page("三個好朋友｜行前課 + 現場使用", "g2", [
   card("sun", "光", "太陽照進來，地上有花的影子<br>動作：雙手張開像太陽", "big"),
   card("wind", "風", "大屋頂下面是空的，風跑來跑去<br>動作：手在臉前扇一扇", "big"),
   card("water", "水", "水從二樓流下來，變成瀑布<br>動作：手指由上往下晃", "big"),
   card("rest", "休息卡", "我需要休息一下", "big"),
 ], "建議護貝；休息卡可多印幾張，每位學生一張。"),
 page("西拉雅符號 + 顏色卡", "g3", [
   card("jar", "壺", "入口有三個圓圓的壺"),
   card("flower", "八葉花", "8 片葉子的花，數一數"),
   color_card(B, "藍色"), color_card("#fff", "白色"), color_card(R, "紅色"), color_card(K, "黑色"),
   color_card(Y, "芒果黃", "玉井芒果"), color_card(G, "稻穗黃", "嘉南平原的稻子"),
   color_card(GR, "草綠", "屋頂上的草"),
 ], "顏色卡用於「西拉雅顏色盒」分類與第 6 關；藍、白、紅、黑是西拉雅服飾的顏色。"),
 page("關卡任務卡", "g2", [
   card("m1", "第 1 關　房子戴草帽", "找一找：哪裡的草蓋在房子上？"),
   card("m2", "第 2 關　找三個壺", "數一數：入口有幾個壺？"),
   card("m3", "第 3 關　光的花", "踩一踩：地上的光影花"),
   card("m4", "第 4 關　抱風", "感覺看看：大屋頂下涼不涼？"),
   card("m5", "第 5 關　跟著水走", "水池 → 瀑布 → 水圳"),
   card("m6", "第 6 關　顏色賓果", "找到建築上的顏色"),
 ], "可貼在集合點，或做成手環／掛繩卡，完成一關翻面或貼貼紙。"),
 page("展板配對｜路線底卡", "g1", [
   card("bike", "水圳之源", "官田・六甲・烏山頭", "wide"),
   card("hills", "湖丘時光", "左鎮・玉井・虎頭埤・走馬瀨", "wide"),
   card("clouds", "雲水之間", "大埔・曾文水庫・梅嶺", "wide"),
 ], "放大列印或護貝當底板，學生把小圖卡放到對的底卡上。"),
 page("展板配對｜小圖卡（剪下）", "g3", [
   card("statue", "八田與一"), card("cypress", "落羽松森林"), card("caltrop", "菱角"),
   card("fossil", "化石"), card("ice", "芒果冰"), card("bridge", "吊橋"),
   card("horse", "走馬瀨的馬"), card("gate", "玄空法寺"), card("hotspring", "龜丹溫泉"),
 ], "答案（教師用）：水圳之源＝八田與一、落羽松、菱角｜湖丘時光＝化石、芒果冰、吊橋、走馬瀨的馬｜雲水之間＝玄空法寺、龜丹溫泉。"),
]

# 先…再… 行程條 + 證書
sched = "".join(f'<div class="step"><div class="ic">{ICON[i]}</div><div>{t}</div></div>' for i, t in
                (("m1", "1 草帽"), ("m2", "2 壺"), ("m3", "3 光"), ("m4", "4 風"), ("m5", "5 水"), ("m6", "6 顏色")))
pages.append(f'''<section class="page"><h1>行程條 + 獎勵證書</h1>
<div class="sched"><div class="lbl">今天的探險</div>{sched}</div>
<div class="sched"><div class="lbl">今天的探險</div>{sched}</div>
<div class="cert"><div class="flw">{ICON["flower"]}</div><h2>西拉雅建築師</h2>
<p>________ 完成了 6 個建築探險關卡！</p><p>我找到了 <b>光</b>、<b>風</b>、<b>水</b> 三個好朋友。</p>
<div class="stk">{"".join('<span></span>' for _ in range(6))}</div><p class="date">日期：____年____月____日</p></div>
<p class="note">行程條可剪下貼在桌上或護照封面，完成一格就打勾；證書下方 6 格貼貼紙。</p></section>''')

css = f"""
@page {{ size: A4; margin: 10mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: "WenQuanYi Zen Hei", "Noto Sans TC", "Microsoft JhengHei", sans-serif; color: {K}; }}
.page {{ height: 277mm; page-break-after: always; display: flex; flex-direction: column; }}
.page:last-child {{ page-break-after: auto; }}
h1 {{ font-size: 15pt; margin: 0 0 4mm; padding-left: 3mm; border-left: 3mm solid {R}; }}
.grid {{ flex: 1; display: grid; gap: 0; }}
.g1 {{ grid-template-columns: 1fr; }}
.g2 {{ grid-template-columns: 1fr 1fr; }}
.g3 {{ grid-template-columns: 1fr 1fr 1fr; }}
.card {{ border: 1px dashed #999; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 4mm; text-align: center; }}
.card .ic {{ width: 60%; max-width: 55mm; }}
.card .ic svg {{ width: 100%; height: auto; display: block; }}
.card .t {{ font-size: 22pt; font-weight: bold; margin-top: 2mm; }}
.card .s {{ font-size: 11pt; color: #444; margin-top: 1mm; line-height: 1.4; }}
.g2 .card.big .t {{ font-size: 54pt; }}
.card.big .s {{ font-size: 13pt; }}
.card.big .ic {{ width: 55%; }}
.card.wide {{ flex-direction: row; gap: 8mm; justify-content: flex-start; padding-left: 12mm; }}
.card.wide .ic {{ width: 60mm; }}
.card.wide .t {{ font-size: 34pt; text-align: left; }}
.card.wide .s {{ text-align: left; font-size: 14pt; }}
.card.wide > .t, .card.wide > .s {{ }}
.sw {{ width: 38mm; height: 38mm; border-radius: 4mm; }}
.g2 .card .t {{ font-size: 20pt; }}
.note {{ font-size: 9.5pt; color: #555; margin: 3mm 0 0; }}
.sched {{ display: flex; border: 1px dashed #999; margin-bottom: 4mm; align-items: center; }}
.sched .lbl {{ writing-mode: vertical-rl; font-weight: bold; padding: 2mm; background: {D}; color: #fff; align-self: stretch; text-align: center; }}
.step {{ flex: 1; text-align: center; font-size: 12pt; font-weight: bold; padding: 2mm; border-left: 1px solid #ccc; }}
.step .ic svg {{ width: 18mm; height: 18mm; }}
.step::after {{ content: "□"; display: block; font-size: 16pt; }}
.cert {{ flex: 1; border: 3mm double {R}; text-align: center; padding: 8mm; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
.cert .flw svg {{ width: 34mm; height: 34mm; }}
.cert h2 {{ font-size: 34pt; margin: 4mm 0; color: {D}; }}
.cert p {{ font-size: 16pt; margin: 2mm 0; }}
.stk {{ display: flex; gap: 4mm; margin: 6mm 0; }}
.stk span {{ width: 20mm; height: 20mm; border: 1.5px dashed {K}; border-radius: 50%; }}
.date {{ font-size: 13pt !important; }}
"""
# 左右排列的路線底卡需要把文字包起來
html = f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>西拉雅建築探險圖卡</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
html = html.replace('<div class="t">水圳之源', '<div><div class="t">水圳之源').replace('<div class="t">湖丘時光', '<div><div class="t">湖丘時光').replace('<div class="t">雲水之間', '<div><div class="t">雲水之間')
for s in ("官田・六甲・烏山頭", "左鎮・玉井・虎頭埤・走馬瀨", "大埔・曾文水庫・梅嶺"):
    html = html.replace(f'{s}</div>', f'{s}</div></div>')
open(__file__.replace("build.py", "cards.html"), "w", encoding="utf-8").write(html)
