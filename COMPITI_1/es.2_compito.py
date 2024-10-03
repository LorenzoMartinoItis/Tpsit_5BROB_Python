num = int(input("Inserisci un numero: "))

def fattoriale(num):
    if num <= 1:
        return 1
    else:
        return num * fattoriale(num - 1)

print(f"Il fattoriale è {fattoriale(num)}")