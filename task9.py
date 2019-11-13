n = int(input("Введите число: "))
chek = 1
for x in range(1, n+1):
    factorial = chek * x
    chek = factorial
print(factorial)
