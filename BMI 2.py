weight = int(input("Hur mycket väger du ?(kg) "))

maxweight = 300
minweight = 20
maxlength = 250
minlength = 100



while weight < minweight:

    print("minimumvikt är 20 kg")
    weight = int(input("Hur mycket väger du ?(kg) "))

    while weight > maxweight:
        print("maxvikt är 300 kg")

        weight = int(input("Hur mycket väger du ?(kg) "))



length = int(input("Hur lång är du ? (cm) "))

while length < minlength:
    print("minimumlängd är 100 cm")
    length = int(input("Hur lång är du ? (cm) "))

    while length > maxlength:
            print("maxlängd är 250 cm")
            length = int(input("Hur lång är du ? (cm) "))




BMI = weight/length**2*10000

Underviktig = 18.5
Normalviktig = 24.9
Overviktig = 29.9
Fet = 30

if BMI < Underviktig:
    print("Ditt BMI är:", round(BMI), " Du väger för lite")

elif BMI < Normalviktig:
    print("Ditt BMI är:", round(BMI), " Du har normalvikt")

elif BMI < Overviktig:
    print("Ditt BMI är:", round(BMI), " Du är överviktig")

elif BMI > Fet:
    print("Ditt BMI är:", round(BMI), " Du bör gå ner i vikt")
