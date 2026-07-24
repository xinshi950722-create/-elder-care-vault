import re
import asyncio
import edge_tts

SRC = r"D:\workbuddy work\2026-07-20-09-10-29\养老转行\04素材库\养老行业通勤可听口播稿.md"
OUT = r"D:\workbuddy work\2026-07-20-09-10-29\养老转行\04素材库\养老行业通勤可听口播稿.mp3"
VOICE = "zh-CN-XiaoxiaoNeural"  # 年轻女性、自然清晰，适合通勤听

def clean(md_text: str) -> str:
    lines = []
    for raw in md_text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith(">") or line == "---":
            continue
        line = re.sub(r"^（[^）]*）\s*", "", line)
        line = line.replace("**", "")
        line = re.sub(r"\[\[([^\]]+)\]\]", r"\1", line)
        line = line.replace("`", "")
        if line:
            lines.append(line)
    return "\n".join(lines)

def main():
    md = open(SRC, encoding="utf-8").read()
    text = clean(md)
    print("清洗后字数: " + str(len(text)))
    communicate = edge_tts.Communicate(text, VOICE)
    asyncio.run(communicate.save(OUT))
    print("已生成: " + OUT)

if __name__ == "__main__":
    main()
