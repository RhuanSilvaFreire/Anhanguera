num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

op = input('Qual calculo deseja realizar? + - * / ?: ')

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
    if num2 == 0:
        print("Erro de divisão! ")
    else:
       print(num1 / num2)
else:
    print("Erro de operação: ")
input()