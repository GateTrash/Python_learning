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
print(file_path.name)
print(file_path.stem)
print(file_path.suffixes)
print(file_path.parent)
try:
    if file_path.dir():
        print("this directory")
except:
    print("Error; This isn't directory")
if file_path.exists():
    if file_path.is_file: print("this is file")
    print("file found!")
    #with open(file_path, "a") as file:
else: print("File not found")
    
