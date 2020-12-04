from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main():
    menu()


def menu():
    print('===================================')
    print('============ Bem-vindo ============')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto; \n2 - Listar produto; \n3 - Comprar produto; \n4 - Visualizar carrinho;'
          '\n5 - Fechar pedido; \n6 - Sair do sistema')

    opcao: int = int(input())
    menu_switch(opcao)
    sleep(1)


def menu_switch(opcao):
    # switcher = {
    #     1: cadastrar_produto,
    #     2: listar_produtos,
    #     3: comprar_produtos,
    #     4: visualizar_produto,
    #     5: fechar_pedido,
    #     6: print('Volte sempre!')
    # }
    # return switcher.get(opcao, 'Opção inválida.')
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        visualizar_produto()
    elif opcao == 5:
        fechar_pedido()
    else:
        print('Opção inválida!')


def cadastrar_produto():
    print('===================================')
    print('======= Cadastro do Produto =======')
    print('===================================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(1)
    menu()


def listar_produtos():
    if len(produtos) > 0:
        print('===================================')
        print('======= Listagem de Produto =======')
        print('===================================')

        for produto in produtos:
            print(produto)
            sleep(1)
    else:
        print('Ainda não existem produto a serem listados')
    sleep_and_run_menu()


def comprar_produtos():
    if len(produtos) > 0:
        print('Informe o código do produto que deseja ser adicionado ao carrinho: ')
        print('------------------------------------')
        print('======= Produtos Disponiveis =======')
        print('====================================')
        for produto in produtos:
            print(produto)
            sleep(1)
        
        codigo: int = int(input())
        produto:Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)

                    checa_itens_no_carrinho(item, produto, quant, tem_no_carrinho)


            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicioando ao carrinho.')
                sleep_and_run_menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado')
            sleep_and_run_menu()
    else:
        print('Ainda não existem produto a serem listados')
        sleep_and_run_menu()


def checa_itens_no_carrinho(item, produto, quant, tem_no_carrinho):
    if quant:
        item[produto] = quant + 1
        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
        tem_no_carrinho = True
        sleep_and_run_menu()
    if not tem_no_carrinho:
        prod = {produto: 1}
        carrinho.append(prod)
        print(f'O produto {produto.nome} foi adicionado ao carrinho.')
        sleep_and_run_menu()


def sleep_and_run_menu():
    sleep(2)
    menu()


def visualizar_produto():
    if len(carrinho) > 0:
        print('===================================')
        print('======== Itens no Carrinho ========')
        print('===================================')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
    else:
        print('Ainda não existem produto no carrinho')
    sleep_and_run_menu()


def fechar_pedido():
    if len(carrinho) > 0:
        valor_total: float = 0
        print('====================================')
        print('======= Produtos no Carrinho =======')
        print('====================================')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
        print(f'Sua compra é de: {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(3)

    else:
        print('Ainda não existem produto no carrinho')
    sleep_and_run_menu()


def pega_produto_por_codigo(codigo: int):
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
