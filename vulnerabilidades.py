from enums import TipoVulnerabilidade, Severidade, StatusTratamento

class Vulnerabilidades:

    def __init__(self, descricao):

        self.descricao = descricao
        self.tipo = TipoVulnerabilidade
        self.severidade = Severidade
        self.status = StatusTratamento