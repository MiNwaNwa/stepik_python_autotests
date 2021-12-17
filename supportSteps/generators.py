import random
import string

# Генерируем случайную строку из букв и цифр
def generateRandomStringNumbersLetters(length):
    result = ""
    for i in range(0, length):
        if (random.randint(0, 9) % 2) == 0:
            result += str(random.randint(0, 9))
        else:
            result += str(random.choice((string.ascii_letters[random.randint(0, 5)])))
    return result


