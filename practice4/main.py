import numpy as np

def read_matrix(file_path):
    with open(file_path, 'r') as file:
        n, m = map(int, file.readline().split())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
        return np.array(matrix)

def check_matrix(matrix):
    n, m = matrix.shape
    En = matrix[:, :n]
    if not np.array_equal(En, np.eye(n)):
        raise ValueError("Матрица не соответствует формату G = [En | D].")
    return True

def get_code_parameters(matrix):
    n, m = matrix.shape
    num_codewords = 2 ** n
    min_distance = compute_min_distance(matrix)
    return n, m, num_codewords, min_distance

def compute_min_distance(matrix):
    n, m = matrix.shape
    codewords = generate_codewords(matrix)
    min_distance = float('inf')
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            distance = np.sum(codewords[i] != codewords[j])
            if distance < min_distance:
                min_distance = distance
    return min_distance

def generate_codewords(matrix):
    n, m = matrix.shape
    En = matrix[:, :n]
    D = matrix[:, n:]
    codewords = []
    for i in range(2 ** n):
        binary = format(i, f'0{n}b')
        info_bits = np.array([int(bit) for bit in binary])
        codeword = np.dot(info_bits, matrix) % 2
        codewords.append(codeword)
    return codewords

def main():
    file_paths = ["test_matrices/code"+str(c)+".txt" for c in range(1,6)]
    results = []
    for file_path in file_paths:
        matrix = read_matrix(file_path)
        check_matrix(matrix)
        n, m, num_codewords, min_distance = get_code_parameters(matrix)
        results.append((file_path, n, m, num_codewords, min_distance))
    
    print("|Матрица                |Длина кода n|Размерность кода m|Количество кодовых слов|Кодовое расстояние|")
    print("|-----------------------|------------|------------------|-----------------------|------------------|")
    for result in results:
        print(f"|{result[0]}|{result[1]:>12}|{result[2]:>18}|{result[3]:>23}|{result[4]:>18}|")

if __name__ == "__main__":
    main()