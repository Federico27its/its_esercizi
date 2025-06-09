def binary_search(l: list, value: int) -> bool:
    i: int = 0
    j: int = len(l)-1
    while i <= j:
        half = (j + i) // 2 
        if l[half] > value:
            j = half - 1 
        elif l[half] < value:
            i = half + 1 
        else:
            return True
    return False

print(binary_search([-10, -5, -3, -1, 0, 1, 2, 3, 5, 7, 34, 432, 453, 500,  534, 643, 754, 875, 3421, 5423, 6644, 6646, 7000, 5233243, 99999999999999], -9000))
