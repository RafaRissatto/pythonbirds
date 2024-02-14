class Pessoa:
    def __init__(self, nome=None, idade=34):
        self.idade = idade
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'

p = Pessoa()
print(Pessoa.comprimentar(p))
print(p.comprimentar())
print(p.nome)
p.nome = 'Rafael'
print(p.nome)
print(p.idade )
