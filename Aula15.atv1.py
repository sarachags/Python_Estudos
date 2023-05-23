class ContaBancaria:
    def __init__ (self, numero, cliente, tipo, credito_limite, status=False):
        self.numero=numero
        self.saldo=0
        self.status=status
        self.cliente=cliente
        self.tipo=tipo
        self.credito_limite = credito_limite
        self.limite_disponivel = self.credito_limite

    def deposito(self, depositar):
        self.depositar=depositar
        if self.limite_disponivel==self.credito_limite:
            self.saldo+=self.depositar
        elif self.limite_disponivel<self.credito_limite:
            valor_para_limite = self.credito_limite-self.limite_disponivel
            valor_para_saldo = self.depositar-self.limite_disponivel
            self.limite_disponivel+=valor_para_limite
            self.saldo+=valor_para_saldo


    def saque(self, sacar):
        self.sacar = sacar
        if self.status == False:
            print(f'CONTA DESATIVADA')

        else:
            if sacar <= self.saldo:
                self.saldo -= sacar
                print(f'HOUVE UM SAQUE, SEU SALDO AGORA É {self.saldo}')
            elif sacar <= self.saldo + self.limite_disponivel:
                self.saldo-=sacar
                self.limite_disponivel+=self.saldo
                self.saldo=0
            else:
                print(f'SALDO INDISPONIVEL')

    def verificar_saldo(self):
        if self.status==False:
            print(f'SUA CONTA NÃO ESTÁ ATIVA')
        elif self.saldo >= 0:
            print(f'SEU SALDO É {self.saldo}. SEU SALDO ESTÁ POSITIVO')
        else:
            print(f'SEU SALDO É {self.saldo}. SEU SALDO ESTÁ NEGATIVO')

    def ativa_conta(self):
        if self.status==False:
            self.status=True
            print(f' CONTA ATIVA')
        else:
            print(f' JÁ ESTÁ ATIVA')

    def desativar_conta(self):
        if self.status==True:
            self.status=False
            print(f' CONTA DESATIVADA')
        else:
            print(f' JÁ ESTÁ DESATIVADA')


    def ativar_limite(self, credito_limite):
         if self.status==True:
             self.credito_limite = credito_limite
             self.limite_disponivel = self.credito_limite
             print(f'VOCÊ TEM {self.credito_limite}!')

dados = ContaBancaria(123, 0, "Diego", "Debito")
print(vars(dados))
dados.deposito(20)
print(vars(dados))
dados.deposito(30)
print(vars(dados))
dados.saque(20)
print(vars(dados))
dados.verificar_saldo()
print(vars(dados))
dados.ativa_conta()
print(vars(dados))
dados.ativar_limite(2000)
print(vars(dados))