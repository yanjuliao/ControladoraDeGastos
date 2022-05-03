#Objetivos do programa---------------------------------------------------------
   #Escolher entre entrada e saída
     #Dar um nome a entrada ou saída escolhida
       #Informar o valor
         #Informar ao usuário como estão seus gastos.

Entrada = []
Saída = []
ValorEntrada = []
ValorSaída = []

Base = input("Digite 'E' para inserir uma entrada ou 'S' para inserir uma saída >> ")
Base = Base.upper()

while Base != 'X':
  while Base == 'E':
    Entrada.append(input("[Dê um nome a sua entrada] >> "))
    Base = Base.upper()
    ValorEntrada.append(float(input("[Digite o valor da entrada] >> ")))
    Base = input("Digite 'E' para inserir uma entrada ou 'S' para inserir uma saída, ou X para sair>> ")
    Base = Base.upper()
  while Base == 'S':
    Saída.append(input("[Dê um nome a sua saída] >> "))
    ValorSaída.append (float(input("[Digite o valor da saída] >> ")))
    Base = input("Digite 'E' para inserir uma entrada ou 'S' para inserir uma saída, ou X para sair>> ")
    Base = Base.upper()


Dívida = sum(ValorEntrada) - sum(ValorSaída)
if Dívida <(-1500):
  print("[Seu gastos estão sem controle, verifique sua situação de endividamento na Receita Federal]")
  print("Isso foi tudo que entrou na sua conta ",Entrada)
  print("Isso foi tudo que saiu na sua conta ",Saída)
elif Dívida <0:
  print("[Você está gastando muito, tente controlar melhor seus gastos, " + "seu saldo é de", Dívida ,"]")
  print("Isso foi tudo que entrou na sua conta ",Entrada)
  print("Isso foi tudo que saiu na sua conta ",Saída)
elif Dívida >0:
  print("Isso foi tudo que entrou na sua conta: ",Entrada)
  print("Isso foi tudo que saiu na sua conta ",Saída)
  print("Seu saldo é de ",Dívida)