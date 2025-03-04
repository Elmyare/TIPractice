import heapq
from collections import Counter, defaultdict
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
def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
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
    tree = build_huffman_tree(text)
    codes = build_huffman_codes(tree)
    encoded_text = ''.join([codes[char] for char in text])
    return encoded_text, codes

# Метод Шеннона-Фано
def shannon_fano_encode(text):
    frequency = Counter(text)
    sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    codes = {}

    def build_shannon_fano_codes(char_list, prefix=""):
        if len(char_list) == 1:
            codes[char_list[0][0]] = prefix
            return
        total = sum([freq for char, freq in char_list])
        half = 0
        for i in range(len(char_list)):
            half += char_list[i][1]
            if half >= total / 2:
                build_shannon_fano_codes(char_list[:i+1], prefix + "0")
                build_shannon_fano_codes(char_list[i+1:], prefix + "1")
                break

    build_shannon_fano_codes(sorted_chars)
    encoded_text = ''.join([codes[char] for char in text])
    return encoded_text, codes

# Вычисление энтропии H1
def calculate_h1(encoded_text):
    frequency = Counter(encoded_text)
    total = len(encoded_text)
    h1 = 0
    for char, freq in frequency.items():
        probability = freq / total
        h1 -= probability * math.log2(probability)
    return h1

# Вычисление энтропии H2
def calculate_h2(encoded_text):
    pairs = [encoded_text[i:i+2] for i in range(len(encoded_text) - 1)]
    frequency = Counter(pairs)
    total = len(pairs)
    h2 = 0
    for pair, freq in frequency.items():
        probability = freq / total
        h2 -= probability * math.log2(probability)
    return h2 / 2

# Вычисление энтропии H3
def calculate_h3(encoded_text):
    triples = [encoded_text[i:i+3] for i in range(len(encoded_text) - 2)]
    frequency = Counter(triples)
    total = len(triples)
    h3 = 0
    for triple, freq in frequency.items():
        probability = freq / total
        h3 -= probability * math.log2(probability)
    return h3 / 3

# Вычисление средней длины кодового слова
def calculate_average_code_length(codes, text):
    frequency = Counter(text)
    total = len(text)
    avg_length = 0
    for char, freq in frequency.items():
        avg_length += freq / total * len(codes[char])
    return avg_length

# Вычисление избыточности
def calculate_redundancy(avg_length, entropy):
    return avg_length - entropy

# Основная функция
def main():
    # Пример текста
    texts = []
    files = ["1.txt", "2.txt", "3.txt"]
    with open("1.txt", "r") as f: 
        texts.append(f.read())
    
    with open("2.txt", "r") as f: 
        texts.append(f.read())
    
    with open("3.txt", "r") as f: 
        texts.append(f.read())

        # Вывод результатов
    print("\nResults:")
    print("+-------------------+--------+-----------+----------+------------+------------+")
    print("| Method            | Text   | Redundancy| H1       | H2         | H3         |")
    print("+-------------------+--------+-----------+----------+------------+------------+")

    for i, text in enumerate(texts):
        # Кодирование методом Хаффмана
        huffman_encoded_text, huffman_codes = huffman_encode(text)
        # print("Huffman encoded text:", huffman_encoded_text)
        # print("Huffman codes:", huffman_codes)

        # Кодирование методом Шеннона-Фано
        shannon_fano_encoded_text, shannon_fano_codes = shannon_fano_encode(text)
        # print("Shannon-Fano encoded text:", shannon_fano_encoded_text)
        # print("Shannon-Fano codes:", shannon_fano_codes)

        # Вычисление средней длины кодового слова
        huffman_avg_length = calculate_average_code_length(huffman_codes, text)
        shannon_fano_avg_length = calculate_average_code_length(shannon_fano_codes, text)

        # Вычисление энтропии H1, H2, H3 для Хаффмана
        huffman_h1 = calculate_h1(huffman_encoded_text)
        huffman_h2 = calculate_h2(huffman_encoded_text)
        huffman_h3 = calculate_h3(huffman_encoded_text)

        # Вычисление энтропии H1, H2, H3 для Шеннона-Фано
        shannon_fano_h1 = calculate_h1(shannon_fano_encoded_text)
        shannon_fano_h2 = calculate_h2(shannon_fano_encoded_text)
        shannon_fano_h3 = calculate_h3(shannon_fano_encoded_text)

        # Вычисление избыточности
        huffman_redundancy = calculate_redundancy(huffman_avg_length, huffman_h1)
        shannon_fano_redundancy = calculate_redundancy(shannon_fano_avg_length, shannon_fano_h1)

        print(f"| Huffman           | {files[i]}  | {huffman_redundancy:.4f}    | {huffman_h1:.4f}   | {huffman_h2:.4f}     | {huffman_h3:.4f}     |")
        print(f"| Shannon-Fano      | {files[i]}  | {shannon_fano_redundancy:.4f}    | {shannon_fano_h1:.4f}   | {shannon_fano_h2:.4f}     | {shannon_fano_h3:.4f}     |")
    
    
    print("+-------------------+--------+-----------+----------+------------+------------+")

if __name__ == "__main__":
    main()