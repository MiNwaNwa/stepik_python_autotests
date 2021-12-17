import random
import string


def generateRandomStringNumbersLetters(length):
    result = ""
    for i in range(0, length):
        if (random.randint(0, 9) % 2) == 0:
            result += str(random.randint(0, 9))
        else:
            result += str(random.choice((string.ascii_letters[random.randint(0, 5)])))
    return result

print(generateRandomStringNumbersLetters(15))


