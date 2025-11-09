from pathlib import Path
import re

from collections import Counter
path = Path('quant-week1/day5')
file_path = path / 'paragraph.txt'
content = ""
with open(file_path , "r", encoding="utf-8") as f:
    content = f.read()
    
words = re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*", content)

freq = Counter(words)
top5 = freq.most_common(5)
print(freq)
print(top5)