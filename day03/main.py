import re

INPUTPATH = "input.txt"
#INPUTPATH = "input-test1.txt"
#INPUTPATH = "input-test2.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()

pattern1 = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
print(sum(int(m.group(1))*int(m.group(2)) for m in pattern1.finditer(raw)))

pattern2 = re.compile(r"(do\(\))|(don't\(\))|(mul\(([0-9]+),([0-9]+)\))")
total = 0
enabled = True
for m in pattern2.finditer(raw):
    if enabled and m.group(3):
        total += int(m.group(4))*int(m.group(5))
    else:
        enabled = bool(m.group(1))
print(total)
