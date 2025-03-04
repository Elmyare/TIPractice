import math
from collections import Counter

# Функция для вычисления энтропии по формуле Шеннона
def shannon_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

# Функция для вычисления первой оценки (частоты отдельных символов)
def entropy_single_chars(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Подсчет частот символов
    char_counts = Counter(text)
    total_chars = len(text)
    
    # Вычисление вероятностей
    probabilities = [count / total_chars for count in char_counts.values()]
    
    # Вычисление энтропии
    return shannon_entropy(probabilities)

# Функция для вычисления второй оценки (частоты пар символов)
def entropy_pairs(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Генерация пар символов с перехлестом
    pairs = [text[i:i+2] for i in range(len(text) - 1)]
    
    # Подсчет частот пар
    pair_counts = Counter(pairs)
    total_pairs = len(pairs)
    
    # Вычисление вероятностей
    probabilities = [count / total_pairs for count in pair_counts.values()]
    
    # Вычисление энтропии и деление на 2
    return shannon_entropy(probabilities) / 2

# Функция для вычисления третьей оценки (частоты троек символов)
def entropy_triples(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Генерация троек символов с перехлестом
    triples = [text[i:i+3] for i in range(len(text) - 2)]
    
    # Подсчет частот троек
    triple_counts = Counter(triples)
    total_triples = len(triples)
    
    # Вычисление вероятностей
    probabilities = [count / total_triples for count in triple_counts.values()]
    
    # Вычисление энтропии и деление на 3
    return shannon_entropy(probabilities) / 3

# Основная функция для вычисления всех оценок энтропии
def calculate_entropies(filename):
    print(f"Оценки энтропии для файла {filename}:")
    print(f"1.  по отдельным символам: {entropy_single_chars(filename):.4f}")
    print(f"2.  по парам символов: {entropy_pairs(filename):.4f}")
    print(f"3.  по тройкам символов: {entropy_triples(filename):.4f}")
    print()

# Вычисление оценок для всех файлов
files = ['1.txt', '2.txt', '3.txt']
for file in files:
    calculate_entropies(file)