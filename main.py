import conversion as con

currency = float(input("Si quieres convertir euros a dolares intoduce 1\nSi quieres convertir dolares a euros intoduce 2\nSi quieres convertir euros a libras intoduce 3\nSi quieres convertir libras a euros intoduce 4\nSi quieres convertir euros a yenes intoduce 5\nSi quieres convertir yenes a euros intoduce 6\n"))
if currency == 1:
    con.euros_dolars()
elif currency == 2:
    con.dolars_euros()
elif currency == 3:
    con.euros_pounds()
elif currency == 4:
    con.pounds_euros()
elif currency == 5:
    con.euros_yen()
elif currency == 6:
    con.yen_euros()
else:
    print("Disculpa pero no te he entendido.")