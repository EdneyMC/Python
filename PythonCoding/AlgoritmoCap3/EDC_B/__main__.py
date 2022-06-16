if __name__=="__main__":

    try:

        celsius=0; fahrenheit=0

        print("\nCONVERSÃO DE TEMPERATURA GRAUS FAHRENHEIT PARA GRAUS CELSIUS")
        fahrenheit = float(input("\nInsira a temperatura em graus Fahrenheit: "))

        celsius = ((fahrenheit-32)*5)/9

        print("\nA temperatura em graus Celsius é: %.1f°C." %celsius + "\n")

    except Exception as e:
        print("ERRO: ",str(e))