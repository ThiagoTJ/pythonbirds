'''
Você deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
- Atributo de dado velocidade
- Método acelerar, que deverá incrementar a velocidade de uma unidade
- Método frear que deverá decrementar a velociadade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
- Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
- Método girar_a_direita
- Método girar_a_esquerda

            N
          O   L
            S

Exemplo:

>>>#Testando motor
>>>motor = Motor()
>>>motor.velocidade
0
>>>motor.acelarar()
>>>motor.velocidade
1
>>>motor.acelerar()
>>>motor.velocidade
2
>>>motor.frear()
>>>motor.velocidade
0
>>>#Testando direção
>>>direcao = Direcao()
>>>direcao.valor
'Norte'
>>>direcao girar_a_direita()
>>>direcao.valor
'Leste'
>>>direcao girar_a_esquerda()
>>>direcao.valor
'Norte'
>>>direcao girar_a_esquerda()
>>>direcao.valor
'Esquerda'
>>>#Juntando tudo
>>>carro = Carro(direcao, motor)
>>>carro.calcular_velocidade()
0
>>>carro.acelerar()
>>>carro.calcular_velocidade()
1
>>>carro.acelerar()
>>>carro.calcular_velocidade()
2
>>>carro.frear()
>>>carro.calcular_velocidade()
0
>>>carro.calcular_direcao()
'Norte'
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Leste'
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Sul'
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Oeste'
>>>carro.girar_a_direita()
>>>carro.calcular_direcao()
'Norte'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Norte'
>>>carro.girar_a_esquerda()
>>>carro.calcular_direcao()
'Oeste'
'''


class Carro:
    def __init__(self, direcao, motor):
        self.car_engine = motor
        self.steering_wheel = direcao

    def calcular_velocidade(self):
        return self.car_engine.velocidade

    def acelerar(self):
        self.car_engine.acelerar()

    def frear(self):
        self.car_engine.frear()

    def calcular_direcao(self):
        return self.steering_wheel.valor

    def girar_a_direita(self):
        self.steering_wheel.girar_a_direita()

    def girar_a_esquerda(self):
        self.steering_wheel.girar_a_esquerda()


NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE,
                             LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE,
                              OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.value = NORTE

    def girar_a_direita(self):
        self.value = self.rotacao_a_direita_dct[self.value]

    def girar_a_esquerda(self):
        self.value = self.rotacao_a_esquerda_dct[self.value]


class Motor:
    def __init__(self):
        self.velocity = 0

    def acelerar(self):
        self.velocity += 1

    def frear(self):
        self.velocity -= 2
        self.velocity = max(0, self.velocity)
