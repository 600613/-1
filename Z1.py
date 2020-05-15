a,b = map(int, input('Введите последовательность через пробел') .split())

# Список с введенной последовательностью
posled = list(range(a, b+1))

print(posled)
result = sum(posled) / len(posled)
print(result)

