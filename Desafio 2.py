# Desafio 2 - Aumento de Salário
salario = float(input("Digite um valor do salário:"))  # Recebe o valor e converte para float
percAumento = float(input("Digite a porcentagem de aumento(Somente numeros):"))  # Recebe o valor e converte para float
aumento = salario*percAumento/100
novoSalario = salario + aumento
print("O valor do aumento foi {:.2f} e o novo salario é R$ {:.2f}!!! "
      .format(aumento, novoSalario))
