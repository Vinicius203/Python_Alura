from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses[mes_cadastro + 1]

    def dia_semana(self):
        dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias[dia_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def __str__(self):
        return self.format_data()
