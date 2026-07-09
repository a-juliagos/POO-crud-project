from enums import TipoAtivo

class Ativos:

    def __init__(self, id, nome_hostname, responsavel, setor):

        self.id = id
        self.nome_hostname = nome_hostname
        self.responsavel = responsavel
        self.setor = setor
        self.tipo = TipoAtivo
        self.vulnerabilidades = []

