import heapq
from collections import Counter
import math

# Класс для узла дерева Хаффмана
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Построение дерева Хаффмана
def build_huffman_tree(freq):
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Построение кодов Хаффмана
def build_huffman_codes(node, prefix="", code=None):
    if code is None:
        code = {}
    if node:
        if node.char is not None:
            code[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", code)
        build_huffman_codes(node.right, prefix + "1", code)
    return code

# Кодирование текста методом Хаффмана
def huffman_encode(text):
    freq = Counter(text)
    tree = build_huffman_tree(freq)
    codes = build_huffman_codes(tree)
    encoded_text = ''.join([codes[char] for char in text])
    return encoded_text, codes, freq

# Вычисление энтропии на символ
def calculate_entropy(freq, total, block_size):
    entropy = 0
    for block, count in freq.items():
        probability = count / total
        entropy -= probability * math.log2(probability)
    return entropy / block_size  # Энтропия на символ

# Вычисление средней длины кодового слова на символ
def calculate_average_code_length(codes, freq, total, block_size):
    avg_length = 0
    for block, count in freq.items():
        avg_length += (count / total) * len(codes[block])
    return avg_length / block_size  # Средняя длина на символ

# Основная функция для блочного кодирования
def block_encoding(text, block_size):
    # Разбиваем текст на блоки
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    
    # Считаем частоту блоков
    freq = Counter(blocks)
    total = len(blocks)
    
    # Кодируем блоки методом Хаффмана
    encoded_text, codes, freq = huffman_encode(blocks)
    
    # Вычисляем энтропию и среднюю длину кодового слова
    entropy = calculate_entropy(freq, total, block_size)
    avg_length = calculate_average_code_length(codes, freq, total, block_size)
    
    # Избыточность на один символ
    redundancy = avg_length - entropy
    
    return redundancy

# Основная функция
def main():
    # Чтение текста из файла
    with open("2.txt", "r") as f:
        text = f.read()
    
    # Вычисление избыточности для разных размеров блоков
    results = []
    for block_size in [1, 2, 3, 4]:
        redundancy = block_encoding(text, block_size)
        results.append((block_size, redundancy))
    
    # Вывод результатов
    print("+-------------------+-------------------+")
    print("| Длина блока (n)   | Избыточность (r)  |")
    print("+-------------------+-------------------+")
    for block_size, redundancy in results:
        print(f"| {block_size:<17} | {redundancy:<17.4f} |")
    print("+-------------------+-------------------+")

if __name__ == "__main__":
    main()