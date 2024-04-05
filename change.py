def change():
    expense = 23.75
    money = 100
    frase1= f"Ingresar gasto\n{expense}"
    frase2= f"Dinero recibido\n{money}"
    print(frase1)
    print(frase2)
    print()
    frase3= "Vuelto"
    print(frase3)
    print()
    frase4= "Pesos"
    print(frase4)
    vuelto_pesos= money-expense
    print(int(vuelto_pesos)) 
    frase5="Centavos"
    print(frase5)
    vuelto_centavos= vuelto_pesos-int(vuelto_pesos)
    print(vuelto_centavos)
change()
