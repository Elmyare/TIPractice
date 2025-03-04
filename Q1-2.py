import random

symbols = ['A', 'B', 'C']
probabilities = [0.1, 0.3, 0.6]
file_size = 10240  # 10 KB
with open('file2.txt', 'w') as file:
    for _ in range(file_size):
        file.write(random.choices(symbols, weights=probabilities)[0])