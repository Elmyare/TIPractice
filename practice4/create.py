import numpy as np
import os

def generate_matrix(n, m):
    """Генерация порождающей матрицы G = [E_n | D]"""
    En = np.eye(n, dtype=int)  # Единичная подматрица
    D = np.random.randint(0, 2, size=(n, m-n))  # Случайная подматрица
    G = np.hstack((En, D))
    return G

def save_matrix_to_file(matrix, filename):
    """Сохранение матрицы в файл"""
    n, m = matrix.shape
    with open(filename, 'w') as f:
        f.write(f"{n} {m}\n")
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

def generate_test_files():
    # Создаем директорию для тестовых файлов, если ее нет
    if not os.path.exists("test_matrices"):
        os.makedirs("test_matrices")
    
    # Параметры для 5 тестовых файлов (n, m)
    test_cases = [
        (2, 4),  # Простой код с 2 информационными битами
        (3, 5),  # Код из примера задания
        (3, 6),  # Код с большей длиной
        (4, 7),  # Код с 4 информационными битами
        (4, 8)   # Код с большей избыточностью
    ]
    
    for i, (n, m) in enumerate(test_cases, 1):
        G = generate_matrix(n, m)
        filename = f"test_matrices/code{i}.txt"
        save_matrix_to_file(G, filename)
        print(f"Создан файл {filename} с матрицей {n}x{m}")

if __name__ == "__main__":
    generate_test_files()