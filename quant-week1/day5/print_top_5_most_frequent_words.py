from pathlib import Path
import re
path = Path('quant-week1/day5')
file_path = path / 'paragraph.txt'
content = ""
with open(file_path , "r", encoding="utf-8") as f:
    content = f.read()
    
words = re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*", content)

freq = {}

for word in words:
    if(freq.get(word) == None): freq[word] = 1
    else: freq[word] += 1
print(freq)