import time
conjunto1 = [0]*5
conjunto2 = [0]*4


for i in range(0, 5):
  conjunto1[i] = input("Digite 5 números, letras ou palavras: ")

print(f'O CONJUNTO 1 É: {conjunto1}\n')

for j in range(0, 4):
  conjunto2[j] = input("Digite 4 números, letras ou palavras: ")

print(f'O CONJUNTO 2 É: {conjunto2}\n')

set1 = set(conjunto1)
set2 = set(conjunto2)

def produto_cartesiano(l1, l2):
  return [(item1, item2) for item1 in l1 for item2 in l2]

while True:
  print("\n--Escolha a operação--\n")
  print('1 = União')
  print('2 = Intersecção')
  print('3 = Diferença')
  print('4 = Produto cartesiano')
  print('0 = Sair\n')

  operacao = int(input("Digite a operação desejada: "))

  if operacao == 0:
    break

  elif operacao == 1:
    print(f'União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {set1 | set2} \n')

  elif operacao == 2:
    print(f'Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {set1 & set2}\n')

  elif operacao == 3:
    print(f'Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {set1 - set2}\n')

  elif operacao == 4:
    produto_cartesiano(conjunto1, conjunto2)
    resultado = produto_cartesiano(conjunto1, conjunto2)
    print(f'Produto cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: ')
    for item in resultado:
      print(item)  
  
  else:
    print("Erro, digite novamente.")

time.sleep(1)
print("Ok, tchau, tchau...")





