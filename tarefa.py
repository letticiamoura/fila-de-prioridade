class Tarefa:
    contador = 0 #Identificador único das tarefas

    #Construtor onde vai ser definido a descrição e o nivel de prioridade. SELF = THIS (java)
    def __init__(self, descricao, prioridade, nivel_prioridade):
        self.descricao = descricao
        self.prioridade = prioridade 
        self.nivel_prioridade = nivel_prioridade
        self.id = Tarefa.contador
        Tarefa.contador += 1
    
    #Definindo a prioridade e o numero correspondente a prioridade
    def definirPrioridade(self, nivel):
        prioridades = {
            'Urgente': 1,
            'Alto': 2,
            'Médio': 3,
            'Baixo': 4
        }
        return prioridades.get(nivel, 5) #Se não encontrar nenhum dos números acima retorna 5 = Invalido