def calcPotencia(rTamBase, e):
    if e==0 :
        return 1
    else:
        return rTamBase * calcPotencia(rTamBase, e-1)


if __name__=="__main__":

    try:

        rTamBase=0.0; hTamAltura=0.0; volumeCm3=0.0; volumeMt3=0.0; volumeLt=0.0; PI=3.14159
        e = 2

        print("\nCALCULO DE AREA DE CILINDRO E CONVERSÃO EM LITROS")
        rTamBase = float(input("\nInsira em centímetros (cm), o tamanho do raio da base do cilindro (Dica: raio=diametro da base / 2): "))
        hTamAltura = float(input("\nInsira em centímetros (cm), o tamanho da altura do cilindro: "))

        #para cálculo da potência, é possível utilizar também os métodos pow() ou math.power().
        volumeCm3 = PI * calcPotencia(rTamBase, e) * hTamAltura

        volumeMt3 = volumeCm3 / 1000000

        volumeLt = volumeMt3 * 1000

        print("\nO volume total do cilindro em centimetros cubicos eh: %.4f" % volumeCm3 + " cm3")
        print("\nO volume total do cilindro em metros cubicos eh: %.8f" % volumeMt3 + " mt3")
        print("\nO volume total do cilindro em litros eh: %.3f" % volumeLt + " lt(s)\n")

    except Exception as e:
        print("ERRO: ", str(e))