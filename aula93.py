# Try, except, else e finally

a = 18
b = 0

# print(f"{a} / {b} = {a/b}")
print(a[0])
try:
    # print(f"{a} / {b} = {a/b}")
    print(a[0])
except ZeroDivisionError:
    print("Divisão por zero!")
except NameError:
    print("Variável não definida!")
except Exception as error:
    print(f"Erro desconhecido: {error.__class__.__name__}")