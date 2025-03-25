import random

def read_binary_file(filename):
    """Чтение бинарного файла из практической работы 2"""
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def hamming_encode(data):
    """Кодирование (7,4)-кодом Хэмминга"""
    blocks = [data[i:i+4] for i in range(0, len(data), 4)]
    encoded = []
    for block in blocks:
        if len(block) < 4:
            block = block + [0]*(4-len(block))
        d1, d2, d3, d4 = block
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4
        encoded.extend([p1, p2, d1, p3, d2, d3, d4])
    return encoded

def hamming_decode(encoded):
    """Декодирование (7,4)-кода Хэмминга с исправлением ошибок"""
    decoded = []
    for i in range(0, len(encoded), 7):
        block = encoded[i:i+7]
        if len(block) < 7:
            break
        p1, p2, d1, p3, d2, d3, d4 = block
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4
        syndrome = s1 + 2*s2 + 4*s3
        if syndrome != 0:
            pos = syndrome - 1
            if pos < 7:
                block[pos] ^= 1
        decoded.extend([block[2], block[4], block[5], block[6]])
    return decoded

def introduce_errors(data, error_prob):
    """Внесение ошибок с заданной вероятностью"""
    return [bit if random.random() > error_prob else bit ^ 1 for bit in data]

def main():
    # Чтение сгенерированного файла
    input_file = "hamming_test/encoded_input.txt"
    original_data = read_binary_file(input_file)
    
    # Кодирование
    encoded_data = hamming_encode(original_data)
    
    # Тестирование для разных вероятностей ошибок
    probabilities = [0.0001, 0.001, 0.01, 0.1]
    results = []
    
    for p in probabilities:
        # Создаем копию с ошибками
        corrupted_data = introduce_errors(encoded_data.copy(), p)
        # Декодируем
        decoded_data = hamming_decode(corrupted_data)
        # Сравниваем с оригиналом
        errors = sum(1 for o, d in zip(original_data, decoded_data[:len(original_data)]) if o != d)
        results.append(errors)
    
    # Вывод результатов
    print("+---------------------+-----------+-----------+-----------+-----------+")
    print("| Вероятность ошибки  |  0.0001   |   0.001   |   0.01    |    0.1    |")
    print("+---------------------+-----------+-----------+-----------+-----------+")
    print(f"| Обнаружено ошибок  | {results[0]:^9} | {results[1]:^9} | {results[2]:^9} | {results[3]:^9} |")
    print("+---------------------+-----------+-----------+-----------+-----------+")

if __name__ == "__main__":
    main()