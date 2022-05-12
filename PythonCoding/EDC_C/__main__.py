
if __name__=="__main__":

    try:

        n1=0; n2=0; n3=0; n4=0; md=0

        n1 = int(input("Insira a primeira nota do aluno: "))
        n2 = int(input("Insira a segunda nota do aluno: "))
        n3 = int(input("Insira a terceira nota do aluno: "))
        n4 = int(input("Insira a quarta nota do aluno: "))
        
        md=(n1+n2+n3+n4)/4

        if md>=5:
            print("\nAPROVADO")
        else:
            print("\nREPROVADO")

        print("Nota média: ", md, "\n")

    except Exception as e:
        print("ERRO: ",str (e))