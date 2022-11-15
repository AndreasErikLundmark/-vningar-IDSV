

Weekday = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
Monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        year = int(input("Year: "))
    except ValueError:
        print("Only digits allowed")
        continue

    if year not in range(1583, 10000):
        print("Out of allowed range 1583 to 9999")
        continue

    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        Monthdays[1] = 29


    while True:
        try:
            month = int(input("Month: "))
        except ValueError:
            print("Only digits allowed")
            continue

        if month not in range(1, 13):
            print("Out of allowed range 1 to 12")
            continue


        while True:
            mnd = Monthdays[month -1]

            try:
                day = int(input("Day: "))
            except ValueError:
                print("Only digits allowed")
                continue

            if day not in range(1, mnd +1):
                print("Out of allowed range 1 to", mnd)
                continue

            else:

                if month == 1 or month == 2:
                    month += 12
                    year -= 1

                wday = (day + 13 * (month + 1) // 5 + year + year // 4 - year//100 + year//400 ) % 7

                print("It is a", Weekday[wday])

            break
        break
    break
