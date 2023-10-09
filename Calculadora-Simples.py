# olá galerinha está ai uma  calculado bem simples...
print("Calculadora simples:\n")
print("lets calculate 1+2=3 2*1=2  \n")


n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo  número::"))
op = input("Digite a operaçao matemática:")


if op == "+":
    resto = n1 + n2
elif op == "-":
    resto = n1 - n2
elif op == "*":
    resto = n1 * n2
elif op == "/":
    resto = n1 / n2
else:
    resto = " Atenção! operaçao invalida"

print(f" Resultado  da operação {n1:.2f} {op} {n2:.2f} = {resto:.2f} ")
