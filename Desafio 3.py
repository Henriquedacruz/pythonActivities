# Desafio 3 - Desconto do produto
preco = float(input("Digite um valor do produto:"))  # Recebe o valor e converte para float
percDesc = float(input("Digite a porcentagem de desconto(Apenas números):"))  # Recebe o valor e converte para float
desconto = preco*percDesc/100
novoPreco = preco - desconto
print("O desconto é de {:.2f} e o preço com desconto é R$ {:.2f}!!! "
      .format(desconto, novoPreco))
