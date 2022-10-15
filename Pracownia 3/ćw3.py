x=input("Podaj wartość z przedziału 0.0-1.0\n")
try:
    x=float(x)
    if float(x)>0 and float(x)<1.0:
        if x>= 0.9:
            print("Ocena:",5.0)
        elif x>= 0.8:
            print("Ocena:",4.5)
        elif x>= 0.7:
            print("Ocena:",4.0)
        elif x>= 0.6:
            print("Ocena:",3.5)
        elif x>= 0.5:
            print("Ocena:",3.0)
        elif x< 0.5:
            print("Ocena:",2.0)
except:
    print("Niepoprawna wartość")