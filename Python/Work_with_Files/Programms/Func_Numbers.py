#ф-ция возвращает наибольшее число в файле
def largest():
    with open("Python/Work_with_Files/files/numbers.txt", "r") as file: 
        text = file.read()
        strings = text.split()
        numbers = []
        for line in strings:
            numbers.append(int(line))
        maximum = numbers[0]
        for number in numbers:
              if maximum < number:
                    maximum = number
        print(f"maximum number equal: {maximum}")
#ф-ция возвращает список продукта в виде клбча и цены в виде значения
def store():
     with open("files/fruits.csv") as file:
            text = file.readlines()
            dictionary = {}
            for line in text:
                buf = line.split(";")
                dictionary[buf[0]] = float(buf[1].replace("\n", ""))
            print(dictionary)
largest()
store()