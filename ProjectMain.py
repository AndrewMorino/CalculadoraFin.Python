import os
import math
import ProjectSub

class calculos1:

        C = float(input('Capital Inicial: '))
        I = float(input('Taxa de Juros: '))
        M = float(input('Montante Final: '))
        T = float(input('Período de Aplicação: '))
        R = ('Nenhuma opção valída executada digite novamente\n')

        taxa_100I = I / 100 #cal1

        if M == 0:
            resultado_montante = C * (1 + taxa_100I) ** T
            print('O montante final é de: {:.2f}'.format(resultado_montante))

        elif C == 0:
            resultado_capital = M / (1 + taxa_100I) ** T
            print('O capital inicial é de: {:.2f}'.format(resultado_capital))

        elif I == 0:
            resultado_taxa = (((M / C) ** (1 / T)) - 1) / 100
            print('A taxa de juros é de: {:.2f}%'.format(resultado_taxa))

        elif T == 0:
             resultado_periodo = math.log10(M/C) / math.log10(1+taxa_100I)
             print('O período de aplicação é de: {:.2f}'.format(resultado_periodo))


class calculos2:

        D = float(input('Desconto racional: '))
        V = float(input('Valor nominal: '))
        A = float(input('Taxa de juros: '))
        N = float(input('Período de antecipação: '))
        R = ('Nenhuma opção valída executada digite novamente\n')

        taxa_100A = A / 100 #cal2

        if D == 0:
            resultado_desconto = (V * I * N) / (1 + taxa_100A * N)
            print('O desconto racional é de: {:.2f}'.format(resultado_desconto))

        elif V == 0:
            resultado_valorn = (D * (1 + taxa_100A * N)) / (I * N)
            print('O valor nominal é de: {:.2f}'.format(resultado_valorn))

        elif A == 0:
            resultado_taxa2 = D / (N * (V - D)) / 100
            print('A taxa de juros é de: {:.2f}%'.format(resultado_taxa2))

        elif N == 0:
            resultado_periodo2 = D / (taxa_100A * (V - D))
            print('O período de antecipação é de: {:.2f}'.format(resultado_periodo2))

class invalido:
   string('blablabla')


'''def fim():
        os.system("cls")
        print(R)
        calculos()

        opt = input("\nDeseja realizar outro cálculo? S/N\n").upper()
        if(opt == 'S'):
            os.system("cls")
            calculos()
        elif(opt == 'N'):
            os.system("cls")
            pass
'''


