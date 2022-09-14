class Main:
    pass

print("testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("joão", "81818-1234")
conta=Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()