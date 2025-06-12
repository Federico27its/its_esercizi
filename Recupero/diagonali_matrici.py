def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    sum: int = 0
    for i in range(min(len(matrix), len(matrix[0]))):
        sum += matrix[i][i]
    return sum

def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    sum: int = 0
    for i in range(min(len(matrix), len(matrix[0]))):
        sum += matrix[i][len(matrix[0]) - i - 1]
    return sum
