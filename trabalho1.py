'''QUESTÃO 1 de 4 – Conteúdos até Aula 3
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app para uma empresa X que vende Planos de Saúde. Uma das estratégias dessa empresa X é cobrar um valor diferente com base na idade do cliente, conforme a listagem abaixo: '''

print('Bem vindo ao sitema de cleber dos santos moraes')
 
valorMensal = 0
# vamos adicionar o valor do plano
valorBase = float(input('Qual o valor do plano? '))
# vamos buscar a idade do pessoa! 
idade = int(input('Qual a idade do coveniado? '))

 #• Se a idade for maior ou igual que 0 e menor que 19, o valor será de 100% do valor base do plano (100 / 100);
if idade >= 0 and idade < 19:
    valorMensal = valorBase * (100 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}')
  # Se a idade for maior ou igual que 19 e menor que 29, o valor será de 150% do valor base do plano (150 / 100);   
elif idade >= 19 and idade < 29:
    valorMensal = valorBase * (150 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}')
  # Se a idade for maior ou igual que 29 e menor que 39, o valor será de 225% do valor base do plano (225 / 100);   
elif idade >= 29 and idade < 39:
    valorMensal = valorBase * (225 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}')
  # Se a idade for maior ou igual que 39 e menor que 49, o valor será de 240% do valor base do plano (240 / 100);
elif idade >= 39 and idade < 49:
    valorMensal = valorBase * (240 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}')
  # Se a idade for maior ou igual que 49 e menor que 59, o valor será de 350% do valor base do plano (350 / 100);
elif idade >= 49 and idade < 59:
    valorMensal = valorBase * (350 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}') 
  # Se a idade for maior ou igual que 59, o valor será de 600% do valor base do plano (600 / 100);
else:
    valorMensal = valorBase * (600 / 100) 
    print(f'Valor mensal do plano será de: R$ {valorMensal:.2f}')