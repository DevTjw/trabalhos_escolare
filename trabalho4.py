# Trabalho 4 - Lista de Contatos
# Nome: Cleber Dos Santos Moraes    
lista_contatos  = [] # Lista de usuarios
id_global = 5518728 # id do programador

def cadastrar_contato (id_global):
    print(f'\n{ "-" * 64}')
    print(f'{ "-" * 20} MENU CADASTRAR CONTATO { "-" * 20}\n')


    id_global = input('ID do Contatato: ')
    nome = input('Por favor entra com Nome do Contato: ')
    atividade = input('Por favor entra com Atividade do Contato: ')
    telefone = input('Por favor entra com Telefone do Contato: ')

    contato = {
        "id_global": id_global,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    # O método .append() adiciona um novo item ao final da lista_contatos.
    lista_contatos.append(contato.copy())  # usar .copy(), cada item na lista será independente, evitando que alterações em um contato afetem os outros.
    print(f'{ "-" * 64}')
    print("\n")

def consultar_contato ():
    while True:
        print(f'\n{ "-" * 64}')
        print(f'{ "-" * 19} MENU CONSULTA DE CONTATOS { "-" * 18}\n')
        print('Escolha a Opção desejada: ')
        print('1 - Consultar Todos os contatos')
        print('2 - Consultar contato por ID')
        print('3 - Consultar contato por atividade')
        print('4 - Retornar')
        escolha = input('>> ')
        print(f'{ "-" * 64}')  
        
        if not lista_contatos: # A instrução if not lista_contatos  verificar se uma lista está vazia.
            print("A lista de contatos está vazia.\n")
            break

        elif escolha == '1':
            for contato in lista_contatos:                
                print(f"ID: {contato['id_global']}")
                print(f"Nome: {contato['nome']}")
                print(f"Atividade: {contato['atividade']}")
                print(f"Telefone: {contato['telefone']}\n")
            print(f'{ "-" * 64}\n')
            break    
        
        elif escolha == '2':
            ref_id = input('Digite o ID do Contato: ')
            print(f'{ "-" * 64}')
            encontrados = False  # Flag para saber se achou pelo menos um contato
            for contato in lista_contatos:
                # Verifica se a escolha corresponde ao ID ou nome do contato
                if contato['id_global'] == ref_id: 
                    print(f"ID: {contato['id_global']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}\n")
                    encontrados = True
                    print(f'{ "-" * 64}\n')
                        
            if not encontrados: # Se não encontrou nenhum contato
                print("ID de Contato não encontrado.")
            print(f'{ "-" * 64}\n')    
            
        elif escolha == '3':
            ref_atividade = input('Digite a Atividade do (s) Contato (s):')
            print(f'{ "-" * 64}')
            encontrados = False  # Flag para saber se achou pelo menos um contato
            for contato in lista_contatos:
                # Verifica se a escolha corresponde ao ID ou nome do contato
                if contato['atividade'].lower() == ref_atividade.lower(): # .lower() compara o nome ignorando maiúsculas/minúsculas.
                    print(f"ID: {contato['id_global']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}\n")
                    encontrados = True
                    
            if not encontrados: # Se não encontrou nenhum contato
                print("Contato não encontrado.")
            print(f'{ "-" * 64}\n')

            
        elif escolha == '4':
            print(f'\n')
            break

        else:
            print("Escolha uma opção correta!!")
            continue

def remover_contato ():
    # 1. Verificar se a lista está vazia antes de iniciar
    if not lista_contatos:
        print(f'\n{ "-" * 64}')
        print("A lista de contatos está vazia. Não há nada para remover.")
        print(f'{ "-" * 64}\n')
        return
    else:
        while True:
            print(f'\n{ "-" * 64}')
            print(f'{ "-" * 21} MENU REMOVER CONTATO { "-" * 21}\n')
            ref_id = input('Digite o ID do Contato que deseja remover: ')
            print(f'{ "-" * 64}')

            for contato in lista_contatos:
                
                if ref_id == contato['id_global'].lower(): # .lower() compara o nome ignorando maiúsculas/minúsculas.
                    lista_contatos.remove(contato) # Remove o contato da lista de - ref_id == contato['id']
                    print("Contato removido com sucesso!")
                    print(f'{ "-" * 64}\n') 
                    return
                
            else:
                print("id Invalido.")
                print(f'{ "-" * 64}\n')      
                return 


# Menu Principal
while True:
    print('--- Bem vindo a Lista de Contato de Cleber Dos Santos Moraes ---')
    print(f'{ "-" * 64}')
    print(f'{ "-" * 24} MENU PRINCIPAL { "-" * 24}\n')
    print('Escolha a Opção desejada: ')
    print('1 - Cadastrar Contato \n2 - Consultar contato \n3 - Remover Contato \n4 - Sair')
    opcao = input('>> ')
    if opcao == '1':    
        # Chama a função cadastrar_contato, passando o id_global como argumento.    
        cadastrar_contato (id_global)
        
    elif opcao == '2':
        # Chama a função consultar_contato para exibir o menu de consulta.        
        consultar_contato ()
        
    elif opcao == '3': 
        # Chama a função remover_contato para exibir o menu de remoção.
        remover_contato ()
        
    elif opcao == '4':
        print('Programa Encerrado')
        break
    else:
        print('Opção inválida\n')
        continue
