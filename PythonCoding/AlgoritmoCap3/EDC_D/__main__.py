if __name__=="__main__":

    try:
        tempoMin=0; velMediaKmHora=0; tempoSeg=0; velMediaKmSeg=0; distPercorrida=0; consumoLitro=0
        KM_LITRO=12

        print("\nCALCULO CONSUMO  DE COMBUSTIVEL POR VIAGEM")
        tempoMin = float(input("Insira o tempo de duração da viagem (minutos): "))
        velMediaKmHora = float(input("Insira a velocidade média realizada na viagem (km/h): "))

        tempoSeg=tempoMin*60

        velMediaKmSeg=velMediaKmHora/3600

        distPercorrida=tempoSeg*velMediaKmSeg

        consumoLitro=distPercorrida/KM_LITRO

        print("\nRESUMO DA VIAGEM")
        print("Velocidade média: %.0f km/h." %velMediaKmHora)
        print("Tempo gasto: %.0f minuto(s)." %tempoMin)
        print("Distância percorrida: %.1f km." %distPercorrida)
        print("Quantidade de combustível utilzada: %.1f litro(s).\n" %consumoLitro)

    except Exception as e:
        print("ERRO: ", str(e))
