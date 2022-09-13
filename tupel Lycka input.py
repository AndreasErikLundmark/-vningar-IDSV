folk = []

commmand = input("Kommando: ").lower()

while commmand != "sluta":
    match commmand:
        case "ny":
            name = input("Namn: ")
            age = int(input("Ålder: "))
            happy = input("Är du lycklig?") == "ja"

            if happy:
                humör = "lycklig"

            else:
                humör = "ledsen"

            commmand = input("Kommando: ").lower()

            tupel = (name, age, humör)
            folk.append(tupel)
        case "skriv":
            for person in folk:
                print(person[0], person[1], person[2])

            commmand = input("Kommando: ").lower()



        case "spara":
            filename = input("Fil: ")
            file = open(filename, "w")
            for pers in folk:
                file.write(str(pers[0]) + " ")
                file.write(str(pers[1]) + " ")
                file.write(str(pers[2]) + "\n")
            file.close()

        case "ladda":
            folk.clear()  # tömmer listan
            filename = input("Fil: ")
            file = open(filename, "r")

            for line in file:
                terms = line.split()  # ger en lista
                tupel = terms[0], int(terms[1]), terms[2] 
                folk.append(tupel)

                for person in folk:

                    print(person[0], person[1], person[2])

    commmand = input("Kommando: ").lower()
