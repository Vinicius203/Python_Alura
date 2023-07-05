class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano:02d}")


data = Data(21, 11, 2007)
data.data_formatada()
data2 = Data(5, 9, 2001)
data2.data_formatada()
