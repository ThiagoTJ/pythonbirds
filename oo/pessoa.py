class Pessoa:
    def __init__(self, *familia, nome=None, idade=33):
        self.age = idade
        self.name = nome
        self.family = list(familia)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    filha = Pessoa(nome='Laura')
    esposa = Pessoa(nome='Suellen')
    pai = Pessoa(esposa, filha, nome='Thiago')

    print(Pessoa.cumprimentar(pai))
    print(pai.name)
    print(pai.age)

    for pai in pai.family:
        print(pai.name)
