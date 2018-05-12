class CuentaCorriente:

    def __init__(self,saldo: int):
        self.saldo=saldo

    def depositar(self,monto: int):
        if monto <0:
            print ('No peudes depositar canitdades negativas')
            return
        self.saldo += monto

    def transferir(self, cuenta: 'CuentaCorriente', monto: int):
        if monto > self.saldo:
            print(" Fondos insuficientes")
            return
        self.saldo -= monto
        cuenta.saldo +=monto
        #cuenta.depositar(cantidad)











keiko = CuentaCorriente(32847)
print(keiko.saldo) # 32847
keiko.depositar(10)
print(keiko.saldo) # 32857

AG = CuentaCorriente(37249274)
AG.transferir(keiko, 234)
print(AG.saldo) # disminuido
print(keiko.saldo) # aumentado
