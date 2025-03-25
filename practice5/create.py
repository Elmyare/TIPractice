import random
import os

def generate_binary_file(filename, size_in_bits=1024):
    """
    Генерирует файл со случайной бинарной последовательностью
    :param filename: имя файла для сохранения
    :param size_in_bits: размер файла в битах (по умолчанию 1024)
    """
    # Создаем случайную бинарную последовательность
    binary_data = [str(random.randint(0, 1)) for _ in range(size_in_bits)]
    
    # Записываем в файл (каждый бит с новой строки для удобства)
    with open(filename, 'w') as f:
        f.write('\n'.join(binary_data))
    
    print(f"Сгенерирован файл {filename} с {size_in_bits} битами")

def create_test_environment():
    """Создает тестовую среду для практической работы 5"""
    # Создаем директорию если ее нет
    if not os.path.exists("hamming_test"):
        os.makedirs("hamming_test")
    
    # Генерируем тестовый файл
    input_file = "hamming_test/encoded_input.txt"
    generate_binary_file(input_file, 1024)  # Файл с 1024 битами (128 байт)
    
    print("\nТестовый файл готов для использования в практической работе 5")
    print(f"Используйте путь: {input_file}")

if __name__ == "__main__":
    create_test_environment()