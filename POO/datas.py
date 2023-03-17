class Data():

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f'{self.dia:02d}/{self.mes:02d}/{self.ano:02d}')

d = Data(21, 11, 2007)
d.formatada()
d1 = Data(5, 9, 2001)
d1.formatada()