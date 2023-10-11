class cuentabancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        cuentabancaria.cuentas.append(self)
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5 fee")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print (f"balance: {self.balance}")
        return self
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.cuentas:
            account.mostrar_info_cuenta()

savings = cuentabancaria(.05,1000)
checking = cuentabancaria(.02,5000)

savings.deposito(10).deposito(20).deposito(40).retiro(600).generar_interes().mostrar_info_cuenta()
checking.deposito(100).deposito(200).deposito(400).retiro(60).generar_interes().mostrar_info_cuenta()


cuentabancaria.print_all_accounts()