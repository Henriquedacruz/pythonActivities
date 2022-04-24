
from calculator import Calculator

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
myCalc = Calculator(numero1, numero2)  # Na variavel myClac

op = input("Digite a operação matemática desejada( + - * / ): ")
if op == "+":
    myCalc.somar()
elif op == "-":
    myCalc.subtrair()
elif op == "*":
    myCalc.multiplicar()
elif op == "/":
    myCalc.dividir()
else:
    print("Opção inválida!!! ")

if op == "+" or op == "-" or op == "*" or op == "/":
    print("O Resultado é ", myCalc.resultado)
