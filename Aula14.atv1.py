class Pessoa:
    def __init__ (self, nome, peso, idade, comendo=False, falando=False, andando=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        self.andando=andando

    def comer(self, comida):
        self.comida=comida
        if self.comendo == False:
            print(f'{self.nome} está comendo {self.comida}')
            self.comendo = True
        else:
            print(f'Já está comendo')

    def parar_comer(self):
        if self.comendo == True:
            self.comendo=False
            self.comida = ''
            print(f'{self.nome} parou de comer')


        else:
            print(f'comendo...')


    def falar(self):
        if self.comendo == False:
               if self.falando==False:
                   print(f'começou a falar')
                   self.falando = True

               else:

                   print(f'{self.nome} disse: não Posso Falar')

    def andar(self):
        if self.andando == False:
            self.andando=True
            # self.comendo=False
            print(f'{self.nome} disse: Posso Andar')

        else:
            print(f'NÃO POSSO ANDAR...ELE ESTÁ COMENDO!')


p1 = Pessoa("João", 80, 19)

p1.comer("arroz")
print(vars(p1))
p1.comer('bolo')
p1.parar_comer()
print(vars(p1))
p1.falar()
print(vars(p1))
p1.andar()
print(vars(p1))

# vars = Todos os objetos em formato de dicionario