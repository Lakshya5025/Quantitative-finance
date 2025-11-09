from pathlib import Path
from math import *

path = Path("quant-week1/day5")
file_path = path / "numbers.txt"
 
content = ""
with open(file_path, "r+", encoding="utf-8") as f:
    content = f.read().strip()

numbers = list(map(int, content.split("\n")))
total = sum(numbers)
average = total/len(numbers)
maximum = max(numbers)
minimum = min(numbers)
print(numbers)
print(total)
print(average)
print(maximum)
print(minimum)