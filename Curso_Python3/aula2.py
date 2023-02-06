'''
Argumentos "12" e "34" são ditos não nomeados;
Argumento "sep" é um separador.
Argumento "end" muda o valor default de quebra de linha do windows (CRLF(\r\n)).
'''
print(12, 34, 23, sep="--", end="%@") #não quebrar a linha 
print(33, 44, 77, sep="--", end="\n") 
print(56, 78, sep='..', end="\n\n") #quebrar 2 linhas
print(99, 55, sep='..', end="\n\n")

