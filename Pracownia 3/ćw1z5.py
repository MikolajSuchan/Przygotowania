ile= 0
suma = 0.0
while True:
    x = input("Wprowadź liczbę:\n")
    if x == "gotowe":
        break
    try:
        pomoc = float(x)
    except:
        print("Nieprawidłowe wejście")
        continue
    ile = ile+1
    suma = suma + pomoc
print (suma,ile,suma/ile)