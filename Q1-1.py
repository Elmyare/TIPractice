import random

symbols = ['A', 'B', 'C']
file_size = 10240  # 10 KB
with open('file1.txt', 'w') as file:
    for _ in range(file_size):
        file.write(random.choice(symbols))