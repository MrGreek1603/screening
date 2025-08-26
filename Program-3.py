def generate_series(a: int):
    length = a if a % 2 != 0 else a - 1
    series = []
    for i in range(length):
        series.append(2 * i + 1)   
    return series



a = int(input("Enter a number: "))
result = generate_series(a)
print("Output:", ", ".join(map(str, result)))
