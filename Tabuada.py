num = int(input("Qual o número deseja multiplicar: "))
print("\n")
for i in range(1,11):
    r = i * num
    print(f"{num} x {i} = {r}")
    i = i+1

input()