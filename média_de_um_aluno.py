#Deselvolva um programa que leia as duas notas de um aluno e calcule a sua média.

print ('Olá aluno, seja bem vindo')
nome = input ('Digite seu nome:')
print('É um prazer te receber, {}'.format(nome))
print('Se gostaria de saber sua média, digite SIM')
SIM = input ('Gostaria de saber sua média?')
A1 = float(input('Digite sua nota A1: '))
A2 = float(input('Agora digite sua nota A2: '))
print('Sua média é: {}'.format((A1 + A2) / 2))
