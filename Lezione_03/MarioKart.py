while True:
    n = int(input("Write your finishing position:\n"))
    if not(n > 0 and n % 1 == 0):
        print("Insert a positive integer position...")
    else:
        break
print(f"Finishing position: {n}")

if n == 1:
    print(f"{n}st")
elif n == 2:
    print(f"{n}nd")
elif n == 3:
    print(f"{n}rd")
else:
    print(f"{n}th")

match n:
    case 1:
        print(f"{n}st")
    case 2:
        print(f"{n}nd")
    case 3:
        print(f"{n}rd")
    case _:
        print(f"{n}th")