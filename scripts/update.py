from datetime import datetime

START = "<!--LAST_UPDATED-->"
END = "<!--/LAST_UPDATED-->"

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

start = readme.index(START) + len(START)
end = readme.index(END)

updated = (
    readme[:start]
    + "\n"
    + timestamp
    + "\n"
    + readme[end:]
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print("README updated!")