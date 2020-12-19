class Pessoa:
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

    pai.sobrenome = 'Gonçalves'
    del pai.family

    print(pai.__dict__)
    print(filha.__dict__)
