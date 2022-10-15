x=input("Podaj liczbę godzin:")
try:
    x=int(x)
except:
    print("Muszisz podać wartośc numeryczną")
y=input("Podaj stawkę godzinową:")
try:
    y=int(y)
    if x>40:
        y=int(y)*1.5
        print("Twoje wynagrodzenie wynosi",x*y)
    else:
        print("Twoje wynagrodzenie wynosi",x*y)
except:
    print("Musisz podać wartośc numeryczną")
