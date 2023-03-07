from cliente import Cliente

#criando o cliente
cliente = Cliente("gabriel")
#consigo chamar o nome sem precisar do () no final por causa do @property
#transforma a 1ª letra em maisucula por causa do title
print(cliente.nome)

#utilizando setter (set)
cliente.nome = "Eduarda"
print(cliente.nome)