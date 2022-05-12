
if __name__=="__main__":

    try:
        
        a=0
        b=0
        result=0

        a = int(input("Digite o primeiro valor numérico: "))
        b = int(input("Digite o segundo valor numérico: "))

        if a>b:
            result = a - b
        else:
            result = b - a
    
        print(result)

    except Exception as e:
        print("ERRO: ", str(e))

