
if __name__=="__main__":

    try:

        n1=0; n2=0; n3=0; n4=0; md1=0; ne=0; md2=0

        n1=int(input("Insira a primeira nota: "))
        n2=int(input("Insira a segunda nota: "))
        n3=int(input("Insira a terceira nota: "))
        n4=int(input("Insira a quarta nota: "))

        md1=(n1+n2+n3+n4)/4

        if md1>=7:
            print("\nAPROVADO")
            print("Nota média: ", md1, "\n")
        else:
            print("\nREPROVADO")
            print("Nota média: ", md1, "\n")
            ne=int(input("Insira a nota de EXAME: "))
            md2=(md1+ne)/2
            if md2>=5 :
                print("\nAPROVADO EM EXAME")
            else:
                print("\nREPROVADO")
            
            print("Nota média após EXAME: ", md2, "\n")

    except Exception as e:
        print("ERRO: ",str (e))