import heapq  #Biblioteca p/ fila de prioridade
from tarefa import Tarefa

class FilaChamados:
    def __init__(self):
        self.fila = []  #Inicializa a lista de tarefas vazia

    def adicionar_tarefa(self, tarefa):
        heapq.heappush(self.fila, (tarefa.prioridade, tarefa.id, tarefa))
        print(f"\n++++++++++++++++ Tarefa '{tarefa.descricao}' adicionada com prioridade '{tarefa.nivel_prioridade}'. ++++++++++++++++\n")

    def atender_tarefa(self):
        if not self.fila:
            print("\nNenhuma tarefa na fila para atender.\n")
            return
        prioridade, id, tarefa = heapq.heappop(self.fila)
        print(f"\n\nAtendendo tarefa: '{tarefa.descricao}' (Prioridade: {tarefa.nivel_prioridade})\n\n")

    def listar_tarefas(self):
        if not self.fila:
            print("Nenhuma tarefa na fila.")
            return
        print("\nTarefas na fila (do mais prioritário ao menos):\n")
        for prioridade, id, tarefa in sorted(self.fila):
            print(f"- {tarefa.descricao} (Prioridade: {tarefa.nivel_prioridade})")

def menu():
    fila = FilaChamados()

    while True:
        print("\n *********** Sistema de Gerenciamento de Tarefas ***********")
        print("1. Adicionar Tarefa")
        print("2. Atender Tarefa")
        print("3. Listar Tarefas")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            descricao = input("\nDigite o título da tarefa: ")
            print("\nNíveis de prioridade disponíveis: ")
            print("1 - Urgente")
            print("2 - Alto")
            print("3 - Médio")
            print("4 - Baixo")

            nivel_opcao = input("\nDigite o número da prioridade (1 a 4): ")

            prioridades = {
                '1': (1, 'Urgente'),
                '2': (2, 'Alto'),
                '3': (3, 'Médio'),
                '4': (4, 'Baixo')
            }

            valores = prioridades.get(nivel_opcao)

            if not valores:
                print("Número de prioridade inválido.")
                continue

            prioridade_num, prioridade_nome = valores
            nova_tarefa = Tarefa(descricao, prioridade_num, prioridade_nome)
            fila.adicionar_tarefa(nova_tarefa)

        elif opcao == '2':
            fila.atender_tarefa()

        elif opcao == '3':
            fila.listar_tarefas()

        elif opcao == '4':
            print("\n1...")
            print("2...")
            print("3...")
            print("Saindo do sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
