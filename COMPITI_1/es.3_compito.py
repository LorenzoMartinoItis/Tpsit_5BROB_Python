diz = {"a":1, "b":2, "c":3}
diz_invertito = {}
#vado a leggere e salvare la chiave ed il valore di ogni elemento del dizionario
for chiave,valore in dizionario.items():
    diz_invertito[valore]=chiave #vado ad inserire la coppia valore-chiave nel dizionario invertendo il valore e la chiave precedenti
    

print(diz_invertito)
