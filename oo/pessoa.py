class Pessoa:

    eyes = 2

    def __init__(self, *familia, nome=None, idade=33):
        self.age = idade
        self.name = nome
        self.family = list(familia)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - eyes {cls.eyes}'


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
    print(Pessoa.metodo_estatico(), pai.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),
          pai.nome_e_atributos_de_classe())
