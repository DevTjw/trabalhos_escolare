# Dicionário com tipos de madeira e preços por m³
madeiras = {
    'PIN': ('Tora de Pinho', 150.48,),
    'PER': ('Tora de Peroba', 170.20),
    'MOG': ('Tora de Mogno', 190.90),
    'IPE': ('Tora de Ipê', 210.10),
    'IMB': ('Tora de Imbuia', 220.70),
}



# Opções de transporte e custos fixos
transportes = {
    '1': ('Transporte Rodoviário', 1000.00),
    '2': ('Transporte Ferroviário', 2000.00),
    '3': ('Transporte Hidroviário', 2500.00),
}


print('Bem vindo a Madeireira do Lenhador Cleber moraes\n')

    # Função para escolha do tipo de madeira [EXIGÊNCIA DE CÓDIGO 2 de 7]
def escolha_tipo():
    while True:
        print('Entre com o Tipo de Madeira desejado')
        # O método .items() retorna pares (chave, valor) do dicionário.
        # em madeiras vamos buscar em madeiras o tipo por sigla e nome, preço
        for sigla, (nome, preco_madeira) in madeiras.items(): 
            # chave → sigla ----- valor → dividido em nome e preco
            print(f'{sigla} - {nome}')

        #.upper()Converte todos os caracteres da string para maiúsculas..lower()Converte tudo para minúsculas
        tipoMadeira = input('>> ').strip().upper() 
        if tipoMadeira in madeiras:
            # retorna o VALOR da madeira
            nome, preco_madeira = madeiras[tipoMadeira] 
            return nome, float(preco_madeira)
        else:
            #Errou o tipo de Madeira volta ao inicio
            print('Escolha inválida, entre com o modelo novamente\n')
            continue
  
# Função para escolha da quantidade de toras 
def qtd_toras():

    while True:
        # Tente executar o código dentro de aqui
        try: 
            qtd = int(input('Entre com quantidade de toras em m³: '))
            if  qtd > 2000:  # limite para evitar valores absurdos
                print('Não aceitamos pedidos com essa quantidade de toras.')
                print('Por favor, entre com a quantidade novamente.\n')
                continue
            elif qtd >= 0 and qtd <= 100:
                desconto = 0.00
                return qtd, desconto
            elif qtd >= 100 and qtd <= 500:
                desconto = 0.04
                return qtd, desconto
            elif qtd >= 500 and qtd <= 1000:
                desconto = 0.09
                return qtd, desconto
            else:
                desconto = 0.16
            return qtd, desconto
        # se não for numero não aceita letras
        except ValueError: # Se der erro do tipo ValueError, faça o que está no except.' Exemplo: tentar converter texto para número. 
            print('Valor inválido! Digite apenas números inteiros.')
             # vai voltar pro início do while, pedindo de novo
            continue
      
def transporte():
    while True:
        try:
            print('\nEscolha o tipo de Tranporte:')
            # O método .items() retorna pares (chave, valor) do dicionário.   
            for frete, (tipo_transporte, valor_transporte) in transportes.items(): 
                print(f'{frete} - {tipo_transporte} - R$ {valor_transporte:.2f}') # chave → sigla ----- valor → dividido em nome e preco

            escolha = input('>> ').strip()
            
            # Verifica se escolha está nas chaves do dicionário
            if escolha in transportes:
                tipo_transporte, valor_transporte = transportes[escolha]
                # <<< retorna o valor correto do frete float
                return float(valor_transporte)
            else:
                continue
        except ValueError:  # se não for numero não aceita letras # Se der erro do tipo ValueError, faça o que está no except.' Exemplo: tentar converter texto para número.
            print("Opção inválida. Digite 1, 2 ou 3.")
            # vai voltar pro início do while, pedindo de novo 
            continue         

# ---------------------------------------------------------------

# Escolha do tipo de madeira # chamando função chamada escolha_tipo(), e o que ela retorna (dois valores)
nome, preco_madeira = escolha_tipo() 

# Escolha da quantidade de toras
qtd, desconto = qtd_toras()

# Escolha do transporte
valor_transporte = transporte()

# Cálculo do total final
total = ((preco_madeira * qtd) * (1 - desconto)) + valor_transporte

print(f'TOTAL A PAGAR: R$ {total:.2f}')