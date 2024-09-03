class UrnaEletronica:
    def __init__(self):
        self.candidatos = {}
        self.votos = {}

    def adicionar_candidato(self, nome):
        if nome not in self.candidatos:
            self.candidatos[nome] = len(self.candidatos) + 1
            self.votos[nome] = 0
        else:
            print(f"Candidato {nome} já está registrado.")

    def registrar_voto(self, nome):
        if nome in self.votos:
            self.votos[nome] += 1
        else:
            print(f"Candidato {nome} não encontrado.")

    def exibir_resultados(self):
        for candidato, votos in self.votos.items():
            print(f"{candidato}: {votos} votos")

def main():
    urna = UrnaEletronica()
    while True:
        print("\n1. Adicionar Candidato")
        print("2. Registrar Voto")
        print("3. Exibir Resultados")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do candidato: ")
            urna.adicionar_candidato(nome)
        elif opcao == '2':
            nome = input("Nome do candidato: ")
            urna.registrar_voto(nome)
        elif opcao == '3':
            urna.exibir_resultados()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()