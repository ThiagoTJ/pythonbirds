class Pessoa:

    eyes = 2

    def __init__(self, *familia, nome=None, idade=33):
        self.age = idade
        self.name = nome
        self.family = list(familia)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    filha = Pessoa(nome='Laura')
    pai = Pessoa(filha, nome='Thiago')

    print(Pessoa.cumprimentar(pai))
    print(pai.name)
    print(pai.age)

    for filha in pai.family:
        print(filha.name)

    pai.last_name = 'Gonçalves'
    del pai.family
    pai.eyes = 1
    del pai.eyes

    print(pai.__dict__)
    print(filha.__dict__)

    print(Pessoa.eyes)
    print(pai.eyes)
    print(filha.eyes)

    print(id(Pessoa.eyes), id(pai.eyes), id(filha.eyes))
