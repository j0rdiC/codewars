# HELP THE BOOK SELLER - 6 kyu
# https://www.codewars.com/kata/54dc6f5a224c26032800005c

#, "(A : 200) - (B : 1140)"

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]

dic = {key:0 for key in c}

for i in b:
    if i[0] in dic:
        dic[i[0]] += int(i.split()[1])
            
out = ""
for x in dic:
    if len(out) != 0:
        out += " - "
    out += f"({x} : {dic[x]})"

