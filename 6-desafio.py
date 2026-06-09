# Desafio Aula 04
# Refatorar nosso código usando Dicionário, Type Hint e Funcões.

# ─── Funções ──────────────────────────────────────────────────────────────────

# Validação do nome
def pedir_nome() -> str:
    while True:  # loop infinito: só sai quando o return executar
        try:
            nome: str = input("Digite seu nome: ")
            if not nome.strip():
                raise ValueError("Nome não pode ser vazio ou apenas espaços.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            return nome  # valor válido: devolve e sai do loop
        except ValueError as e:
            print(e)


# label: str → nome do campo ("salário" ou "bônus"), usado só nas mensagens
# valor: float → variável separada para guardar o número digitado
# -> float  → a função devolve um número float
def validacao_valor(label: str) -> float:
    while True:
        try:
            valor: float = float(input(f"Digite o valor do seu {label}: "))
            if valor < 0:
                print(f"Por favor, digite um valor positivo para o {label}.")
            else:
                print(f"{label} válido:", valor)
                return valor  # valor válido: devolve e sai do loop
        except ValueError:
            print(f"Entrada inválida para o {label}. Por favor, digite um número.")


# ─── Coleta de dados (chamando as funções) ────────────────────────────────────

nome = pedir_nome()
salario = validacao_valor("salário")
bonus = validacao_valor("bônus")
bonus_recebido = 1000 + (salario * bonus)

# ─── Dicionário: agrupa todos os dados do usuário em um lugar só ──────────────

usuario: dict = {
    "nome": nome,
    "salario": salario,
    "bonus": bonus,
    "bonus_final": bonus_recebido
}

# Acessa os valores pelo nome da chave: usuario["nome"], usuario["salario"], etc.
print(f"{usuario['nome']}, seu salário é R${usuario['salario']:.2f} e seu bônus final é R${usuario['bonus_final']:.2f}.")
