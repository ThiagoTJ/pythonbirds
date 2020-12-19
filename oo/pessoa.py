class Pessoa:
    def __init__(self, nome=None, idade=33):
        self.age = idade
        self.name = nome

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    print(Pessoa().cumprimentar())
    print(Pessoa('Thiago').name)
    print(Pessoa().age)
