class Calculator:

    def __init__(self, num1, num2):
        self.resultado = 0
        self.operando1 = num1
        self.operando2 = num2

    def somar(self):
        self.resultado = self.operando1 + self.operando2

    def subtrair(self):
        self.resultado = self.operando1 - self.operando2

    def multiplicar(self):
        self.resultado = self.operando1 * self.operando2

    def dividir(self):
        self.resultado = self.operando1 / self.operando2