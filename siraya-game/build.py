# 把圖卡的 SVG 圖示嵌入互動遊戲頁
import json, os, runpy
here = os.path.dirname(os.path.abspath(__file__))
icons = runpy.run_path(os.path.join(here, "..", "siraya-cards", "build.py"))["ICON"]
src = open(os.path.join(here, "game.src.html"), encoding="utf-8").read()
out = src.replace("/*ICONS*/", json.dumps({k: v for k, v in icons.items() if v}, ensure_ascii=False))
open(os.path.join(here, "index.html"), "w", encoding="utf-8").write(out)
