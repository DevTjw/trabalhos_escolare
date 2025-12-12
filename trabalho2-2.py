PS = [30.00 ,45.00,60.00]
PD = [34.00,48.00,66.00]
tamanho = ['P', 'M', 'G']

# Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome (somente print, não usar input aqui).
#  Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. 
print(f"|{'-' * 70}|")
print(f"|{'-' * 10} Bem-vindo a Pizzaria do Cleber dos Santos Moraes {'-' * 10}|")
print(f"|{'-' * 30} Cardápio {'-' * 30}|")
print(f"|{'-' * 10}| Tamanho | Pizza Salgada (PS) | Pizza Doce (PD) |{'-' * 10}|")
print(f"|{'-' * 10}|   P     |     R$ {PS [0]:.2f}       |    R$ {PD [0]:.2f}     |{'-' * 10}|")
print(f"|{'-' * 10}|   M     |     R$ {PS [1]:.2f}       |    R$ {PD [1]:.2f}     |{'-' * 10}|")
print(f"|{'-' * 10}|   G     |     R$ {PS [2]:.2f}       |    R$ {PD [2]:.2f}     |{'-' * 10}|")
print(f"|{'-' * 70}|")

totalFinal = 0.0
while True:

    # Escolha do sabor
    while True:                                                               # .strip()Remove os espaços em branco (e quebras de linha, #tabulações etc.) do início e do fim da string.
        sabor = input("Entre com o sabor desejado (PS/PD): ").strip().upper() #.upper()Converte todos os caracteres da string para maiúsculas..lower()Converte tudo para minúsculas
        if sabor == 'PS':
            tipo = "Pizza Salgada" # vamos ronomear PS e alocar na variavel tipo
            
        elif sabor == 'PD':
            tipo = "Pizza Doce" # vamos ronomear PD e alocar na variavel tipo
            
        else: # se não for PS OU PD retorna ao loop
            print("Sabor inválido. Tente novamente.\n")
            continue   # volta para o início do while sem executar nada abaixo

        # Escolha do tamanho
        while True:                                                                     # .strip()Remove os espaços em branco (e quebras de linha, #tabulações etc.) do início e do fim da string.
            tamanho = input("Entre com o tamanho desejado (P/M/G): ").strip().upper()   #.upper()Converte todos os caracteres da string para maiúsculas..lower()Converte tudo para minúsculas
            if tamanho == "P":
                if tipo == 'Pizza Salgada': 
                    preco = PS[0] # se for salgada adiciona ps (referencia) com preço em preco
                else:
                    preco = PD[0]  # se for Doce adiciona ps (referencia) com preço em preco
                break

            elif tamanho == "M":
                if tipo == 'Pizza Salgada': 
                    preco = PS[1] # se for salgada adiciona ps (referencia) com preço em preco
                else:
                    preco = PD[1] # se for Doce adiciona ps (referencia) com preço em preco
                break
            elif tamanho == "G":
                if tipo == 'Pizza Salgada': 
                    preco = PS[2] # se for salgada adiciona ps (referencia) com preço em preco
                else:
                    preco = PD[2] # se for Doce adiciona ps (referencia) com preço em preco
                break
            else: # se não for P/M/G  retorna ao loop
                print("Tamanho inválido. Tente novamente.\n")
                continue   # volta para o início do while sem executar nada abaixo

        # totalFinal acrecenta valor de compra realizada armanzenando total
        totalFinal += preco
        # imprimir pedido tipo e tamanho
        print(f"Você pediu uma {tipo} no tamanho {tamanho}: R$ {preco:.2f}\n")
                                                                            # .strip()Remove os espaços em branco (e quebras de linha, #tabulações etc.) do início e do fim da string.
        mais = input("Deseja mais alguma coisa? (S/N): ").strip().upper()   #.upper()Converte todos os caracteres da string para maiúsculas..lower()Converte tudo para minúsculas
        # Verifica se o cliente deseja mais algo. sim volta ao ciclo
        if mais != 'S':
            break # sai do loop
    break
# finalizado pedido imprime o resultado final
print(f"\nO valor total a ser pago: R$ {totalFinal:.2f}") # :.2f ADICIONA PONTO DEPOSIs de duas casas decimais
