import random

tal = random.randint(1,100)
count = 0
while True:
    try:
        gissa = int(input("Gissa: "))
    except ValueError:
        print("Endast siffror mellan 1-100 går att mata in")
        continue
    if gissa < tal:
        print("Större!")
        count += 1

    elif gissa > tal:
        print("mindre!")
        count += 1
        continue
    else:
        print("sweet!")
        count += 1
        break
print("du gissade rätt på", count,"försök!")
print("Hejsvejs!")
