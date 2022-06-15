if __name__=="__main__":

    try:

        celsius = 0; fahrenheit = 0

        celsius = float(input("Insira uma temperatura em graus Celsius: "))

        fahrenheit = (9*celsius+160)/5

        print('A temperatura em graus Fahrenheit é: %.2f°F' % fahrenheit)


    except Exception as e:
        print("ERRO: ",str(e))