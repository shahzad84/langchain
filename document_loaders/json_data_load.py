import json
from pathlib import Path
from pprint import pprint

file_path="C:\\Users\\hp\Documents\\Geneai\\langchain\\sample\\data.json"
data=json.loads(Path(file_path).read_text())
# pprint(data)

pprint(data["contacts"])

# jsonloader won't work for me