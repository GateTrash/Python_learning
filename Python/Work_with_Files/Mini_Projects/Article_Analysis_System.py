# Программа должна:
# 1. Прочитать содержимое файла.
# 2. Посчитать количество строк, слов и символов.
# 3. Найти самое длинное слово.
# 4. Найти самое часто встречающееся слово.
# 5. Вывести статистику в консоль.
# 6. Сохранить отчёт в отдельный файл report.txt.
# Дополнительные условия:
# - Регистр букв не должен влиять на подсчёт слов.
# - Пустые строки не должны учитываться как слова.
# - Если исходный файл отсутствует, программа должна корректно сообщить об этом.
# - Отчёт должен содержать дату и время анализа.
from pathlib import Path
file_path = Path("/Users/a0000/Developer/Git_Repositories/Python_learning/Python/Work_with_Files/files/Article.txt")

with open(file_path, "r+", encoding="utf8") as file:
    text = file.read()
    text.upper()
    print(f"text: {text}")
    words = text.split()
    print(f"Words: {words}")
    
