import glob
import json

data = {}
for file in glob.glob("es_*/README.md"):
    try:
        with open(file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            # check if "ragionamento" is in the file
            content = "".join(lines)
            if "ragionamento" in content.lower():
                data[file] = "".join(lines[:6])
    except Exception as e:
        data[file] = str(e)

with open('summary.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2, ensure_ascii=False)
