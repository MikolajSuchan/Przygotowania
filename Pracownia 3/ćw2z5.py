najw = 0
najm = 0
while True:
    try:
        x = input("Wprowadź liczbę:\n")
        if x == "gotowe":
            break
        x = int(x)
        if najw == None and najm == None:
            najw = 0
            najm = 0
        if x > najw:
            najw = x
        if  x < najm:
            najm = x
    except:
        print("Nieprawidłowe wejście")
print(f"Wartość największa to {najw} natomiast najmniejsza wrtość to {najm}")