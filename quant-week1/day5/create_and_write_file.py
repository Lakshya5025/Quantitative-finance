from pathlib import Path

base = Path("quant-week1/day5")               
base.mkdir(exist_ok=True)         
file_path = base / "numbers.txt"   

with open(file_path, "w", encoding="utf-8") as f:
    for i in range(100):
        f.write(str(i) + "\n")