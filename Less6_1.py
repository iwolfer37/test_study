import random
# Генеруємо рандомне число 1-100
number = random.randint(1, 100)
# Правила гри кільсть спроб - 6
print("Зіграємо в гру? Перевіриш свою інтуїцію? Python загадав число, попробуй його вгадати, в тебе є 6 спроб")
# Створюємо цикл, для вгадування числа
for i in range(6):
# Ввести число від користувача та назначити змінну
    while True:
        try:
            guess = int(input("Спроба {0}: Введіть число: ".format(i + 1)))
            break
        except ValueError:
            print("УВАГА! Дозволено вводити тільки цілі числа!")
# Чи наше рандомне число вгадав користувач, чи ні?
    if guess == number:
# Якщо користувач відгадав число, вивести повідомлення про перемогу і кількість використаних спроб
        print("Що спільного між тобою і згаданим числом? Ви обидва загадкові! З такою інтуїцією пора зареєструватися на шоу Хто хоче стати мільйонером?! Python не зміг подолати Вас, можливо Ви родич Ванги? Ви вгадали число за {0} спроб, ВІТАЄМО, ПЕРЕМОГА!".format(i + 1))
        break
    elif guess < number:
# Якщо введене число менше задуманого
        print("Не вгадали! Ваше число менше за загадане, введіть більше (>) число")
    else:
# Якщо введене число більше заданого
        print("Максималіст, Спробуйте щось менше (<) Ваше число більше за загадане.")
else:
# Якщо користувач не відгадав число за 6 спроб, вивести повідомлення про програш і показати задане число
    print("Як відомо, математика - це наука точних наук, а не наука прощання з лузерами. Python переміг! Не вдача у грі - це не кінець світу. Адже ви можете завжди випробувати щастя ще раз, або просто зрозуміти, що ваше покликання - не вгадувати числа, а займатися чимось іншим. Це було число {0}.".format(number))
