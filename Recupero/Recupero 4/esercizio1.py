def calculateChange(time: float):
    if time % 1 != 0:
        time = (time // 1) +1
    if time <= 3:
        return 2.0
    result = 2 + (time - 3) * 0.5
    return 10.0 if result > 10 else float(result)

tests = [1.5, 4, 5.5, 24]
result = []
print(f"{'Car':<8}", end= "")
print(f"{'Hours':<8}", end= "")
print(f"{'Charge':<8}")

for n in range(len(tests)):
    result.append(calculateChange(tests[n]))
    print(f'{n+1:<8}', end= "")
    print(f'{tests[n]:<8}', end= "")
    print(f"{str(calculateChange(tests[n]))+'$':<8}")

print(f"{'TOTAL':<8}", end= "")
print(f"{sum(tests):<8}", end= "")
print(f"{str(sum(result))+'$':<8}")





