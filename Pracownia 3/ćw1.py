x=int(input("Podaj liczbę godzin:"))
y=int(input("Podaj stawkę godzinową:"))
if x>40:
    y=y*1.5
print("Wynagrodzenie wynosi",x*y)