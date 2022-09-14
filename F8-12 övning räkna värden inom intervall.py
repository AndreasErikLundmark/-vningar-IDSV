# F8:12 räkna värden inom intervall. övning föreläsningsmaterial

allatal = []

while True:
    i = input("Tal: ")
    if not i:
        break

    try:
        heltal = int(i)
    except ValueError:
        print("Du måste skriva siffror")
        continue

    allatal.append(heltal)

commmand = input("Vill du räkna?: ").lower()

while commmand != "nej":
    match commmand:
        case "ja":
            min = int(input("Vad är minsta värdet?"))
            max = int(input("Vad är högsta värdet?"))
            count = 0
            for i in allatal:
                if i >= min and i <= max:
                    count += 1

            print(count)
