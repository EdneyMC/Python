if __name__=="__main__":

    try:

        a=0; b=0; apoioTrocaValor=0
        
        print("\nTROCA DE VALORES")
        a=float(input("Insira um valor para A: "))
        b=float(input("Insira outro valor para B: "))
        print("\nVALORES INSERIDOS:")
        print("A = %.2f" %a)
        print("B = %.2f" %b)

        apoioTrocaValor=a
        a=b
        b=apoioTrocaValor

        print("\nVALORES SUBSTITUIDOS:")
        print("A = %.2f" %a)
        print("B = %.2f\n" %b)

    except Exception as e:
        print("ERRO: ", str(e))