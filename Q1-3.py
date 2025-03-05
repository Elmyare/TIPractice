import re

# Пример текста
text = """
Your artistic text is in Russian or English.Your artistic text is in Russian or English.Your artistic text is in Russian or English.
"""

# Приведение к нижнему регистру
text = text.lower()

# Удаление знаков препинания
text = re.sub(r'[^\w\s]', '', text)

# Замена «ё» на «е», «ъ» на «ь»
text = text.replace('ё', 'е').replace('ъ', 'ь')

# Запись в файл
with open('3.txt', 'w') as file:
    file.write(text)