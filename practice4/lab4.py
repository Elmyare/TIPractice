import numpy as np
from itertools import product


def read_matrix(file_path):
    """Чтение матрицы из файла."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    n, m = map(int, lines[0].split())
    G = [list(map(int, line.split())) for line in lines[1:]]
    return n, m, np.array(G)


def generate_random_D(n, m):
    """Генерация случайной подматрицы D."""
    return np.random.randint(0, 2, size=(n, m - n))


def calculate_code_properties(n, m, G):
    """Вычисление характеристик линейного кода."""
    # Размерность кода
    k = n

    # Количество кодовых слов
    num_codewords = 2 ** k

    # Генерация всех возможных кодовых слов
    codewords = []
    for binary in product([0, 1], repeat=k):
        binary = np.array(binary)
        codeword = np.dot(binary, G) % 2
        codewords.append(codeword)

    # Вычисление минимального кодового расстояния
    min_distance = float('inf')
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            distance = np.sum(codewords[i] != codewords[j])
            if distance < min_distance:
                min_distance = distance

    return k, num_codewords, min_distance


def main():
    # Пути к файлам с матрицами
    file_paths = ["matrix1.txt", "matrix2.txt", "matrix3.txt", "matrix4.txt", "matrix5.txt"]

    # Таблица для результатов
    results = []

    for idx, file_path in enumerate(file_paths, start=1):
        try:
            # Чтение данных из файла
            n, m, G = read_matrix(file_path)

            # Если матрица не содержит единичную подматрицу, генерируем случайную D
            if not np.array_equal(G[:, :n], np.eye(n)):
                D = generate_random_D(n, m)
                G = np.hstack((np.eye(n, dtype=int), D))

            # Вычисление характеристик кода
            k, num_codewords, min_distance = calculate_code_properties(n, m, G)

            # Сохранение результатов
            results.append({
                "Code": f"Код {idx}",
                "Length": m,
                "Dimension": k,
                "Codewords": num_codewords,
                "Min Distance": min_distance
            })
        except Exception as e:
            print(f"Ошибка при обработке файла {file_path}: {e}")

    # Вывод таблицы результатов
    print("| Код      | Длина кода (n) | Размерность кода (k) | Количество кодовых слов | Кодовое расстояние |")
    print("|----------|----------------|-----------------------|-------------------------|--------------------|")
    for result in results:
        print(
            f"| {result['Code']}    | {result['Length']}              | {result['Dimension']}                     | {result['Codewords']}                  | {result['Min Distance']}            |")


if __name__ == "__main__":
    main()