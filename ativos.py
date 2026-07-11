

class Ativo:

    def __init__(self, id_ativo, nome_hostname, responsavel, setor, tipo):

        self.id_ativo = id_ativo
        self.nome_hostname = nome_hostname
        self.responsavel = responsavel
        self.setor = setor
        self.tipo = tipo
        self.vulnerabilidades = []

    def listar(self):
        
        print(f""" 
-------------------------
          
ID: {self.id_ativo}
Nome/Hostname: {self.nome_hostname}
Responsável: {self.responsavel}
Setor: {self.setor}
Tipo: {self.tipo.name}   
""")  

        print('---- Vulnerabilidades --- ')
        
        if not self.vulnerabilidades:
            
            print('\nNão existem Vulnerabilidades cadastradas!!')

        else:
            
            for i, vulnerabilidade in enumerate(self.vulnerabilidades, start=1):
                
                print(f"""   
Vulnerabilidade {i}

Descrição: {vulnerabilidade.descricao}
Tipo: {vulnerabilidade.tipo.name}
Severidade: {vulnerabilidade.severidade.name}
Status: {vulnerabilidade.status.name} """)




