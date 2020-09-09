class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    laura = Pessoa(nome = 'Laura')
    thiago = Pessoa(laura, nome = 'Thiago')
    print(Pessoa.cumprimentar(thiago))
    print(id(thiago))
    print(thiago.cumprimentar())
    print(thiago.nome)
    print(thiago.idade)
    for filha in thiago.filhos:
        print(filha.nome)
