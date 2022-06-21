if __name__=="__main__":

    try:

        valorOrigBoleto=0; tempoAtraso=0; taxaJurosSimples=0; boletoAtualizado=0

        print("\nCALCULO DE JUROS SIMPLES DE PRESTAÇOES EM ATRASO")
        valorOrigBoleto=float(input("Insira o valor original da prestação em atraso: "))
        tempoAtraso=int(input("Insira o total de dias corridos, desde um dia após o vencimento da parcela até a data atual: "))
        taxaJurosSimples=float(input("Insira a taxa de juros ao dia, informada no campo observações do boleto: "))

        boletoAtualizado=valorOrigBoleto+(valorOrigBoleto*(taxaJurosSimples/100)*tempoAtraso)

        print("\nO valor atualizado da parcela para pagamento hoje é: %.2f\n"%boletoAtualizado)

    except Exception as e:
        print("ERRO: ", str(e))