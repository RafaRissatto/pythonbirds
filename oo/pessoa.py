class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá {id(self)}'

Rafael = Pessoa(nome= 'Rafael')
Francisco = Pessoa(Rafael, nome= 'Francisco', idade=64)
Rafael.olhos = 3
print(Pessoa.comprimentar(Francisco))
print(Francisco.comprimentar())
print(Francisco.nome)
print(Francisco.idade )
for filho in Francisco.filhos:
    print(filho.nome)
Francisco.sobrenome = 'Rissatto'
print(Francisco.__dict__)
print(Rafael.__dict__)
print(Rafael.olhos)
print(Francisco.olhos)
print(id(Pessoa.olhos), id(Rafael.olhos), id(Francisco.olhos))