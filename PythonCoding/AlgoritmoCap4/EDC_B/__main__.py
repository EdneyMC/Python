
if __name__=="__main__":

    try:

        n=0

        n = int(input("Digite um valor numérico inteiro: "))

        if n<0 :
            n = n*-1
        
        print(n)

    except Exception as e:
        print("ERRO: ",str (e))
