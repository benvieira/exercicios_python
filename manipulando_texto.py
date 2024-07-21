# Fatiamento de String
# Análise com len(), count(), find() in ();
# transformações com replace(), upper(), lower(), capitalize(), title(), strip();
# Divisão com splip ();
# Junção com join ();

#Criando analisador de textos

nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome ...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print('Seu segundo nome é {} e ele tem {} letras'.format(separa[1], len(separa[1])))
print('Seu terceiro nome é {} e ele tem {} letras'.format(separa[2], len(separa[2])))