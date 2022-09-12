numbers=[]
stars = ["*","**","**","***","****","*****","******","*******","********","*********","**********"]
num =int(input("Tal:"))

while True:

    numbers.append(num)
    try:
        num = int(input("Tal: "))

    except ValueError:

        for i in numbers:
            print(i, "|", stars[i], end=" ")
        break

