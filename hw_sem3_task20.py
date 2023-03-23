score_point = {1:"AEIOULNSTRАВЕИНОРСТ", 2:"DGДКЛМПУ",
               3:"BCMPБГЁЬЯ",
               4:"FHVWYЙЫ",
               5:"KЖЗХЦЧ",
               8:"JXШЭЮ",
               10:"QZФЩЪ"}



word = input("Введите слово: ").upper()
score = 0

for i in word:
    for v, k in score_point.items():
        if i in k:
            score += v
print(score)
