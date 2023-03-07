# arquivo criado para criar os objetos

#importando do meu arquivo conta a classe Conta
from conta import Conta

#criando o objeto (conta e conta2)
conta = Conta(123, "Gabriel", 55.5, 1000.0)
conta2 = Conta(321, "Eduarda", 100.0, 1000.0)
#Acesso aos atributos através do objeto
print(conta.titular)
print(conta2.titular)
#Acessando através do metodo(função) extrato
print(conta.extrato())
print(conta2.extrato())
#Acessando através do metodo(função) deposita
print(conta.deposita(15.0))
print(conta2.deposita(10.0))
print(conta.extrato())
print(conta2.extrato())
#Acessando através do metodo(função) saca
print(conta.saca(25.0))
print(conta2.saca(18.0))
print(conta.extrato())
print(conta2.extrato())
#Acessando através do metodo(função) transfere
print(conta2.transfere(10.0, conta))
print(conta2.extrato())
print(conta.extrato())
#acessando atrvés do get
print(conta.limite)
#utilizando o set e acessando através do get
conta.limite = 2000.0
print(conta.limite)
#verificando o codigo do banco
print(Conta.codigo_banco())
