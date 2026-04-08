import json
import os
import urllib.request

ARQUIVO = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(descricao, valor, categoria):
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")
    gastos = carregar_gastos()
    gasto = {"descricao": descricao, "valor": valor, "categoria": categoria}
    gastos.append(gasto)
    salvar_gastos(gastos)
    return gasto


def listar_gastos():
    return carregar_gastos()


def total_gastos():
    gastos = carregar_gastos()
    return sum(g["valor"] for g in gastos)


def remover_gasto(indice):
    gastos = carregar_gastos()
    if indice < 0 or indice >= len(gastos):
        raise IndexError("Índice inválido.")
    removido = gastos.pop(indice)
    salvar_gastos(gastos)
    return removido

def buscar_cotacao_dolar():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        with urllib.request.urlopen(url, timeout=5) as response:
            dados = json.loads(response.read().decode())
            cotacao = float(dados["USDBRL"]["bid"])
            return cotacao
    except Exception:
        return None


def menu():
    while True:
        print("\n===== GastoCerto =====")
        cotacao = buscar_cotacao_dolar()
        if cotacao:
            print(f"💵 Dólar hoje: R$ {cotacao:.2f}")
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Ver total")
        print("4. Remover gasto")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("Valor inválido!")
                continue
            categoria = input("Categoria (ex: alimentação, transporte): ")
            try:
                adicionar_gasto(descricao, valor, categoria)
                print("Gasto adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto registrado.")
            else:
                for i, g in enumerate(gastos):
                    print(f"{i}. {g['descricao']} - R${g['valor']:.2f} [{g['categoria']}]")

        elif opcao == "3":
            print(f"Total de gastos: R${total_gastos():.2f}")

        elif opcao == "4":
            gastos = listar_gastos()
            if not gastos:
                print("Nenhum gasto para remover.")
            else:
                for i, g in enumerate(gastos):
                    print(f"{i}. {g['descricao']} - R${g['valor']:.2f}")
                try:
                    indice = int(input("Número do gasto a remover: "))
                    removido = remover_gasto(indice)
                    print(f"Removido: {removido['descricao']}")
                except (ValueError, IndexError) as e:
                    print(f"Erro: {e}")

        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()