import time

WATER_PER_KG = 30                      # Константа - норма воды в мл на кг
ML_IN_L = 1000                         # Константа - количество мл в литре

# Приветствие с задержкой
print("\n" + 'Доброго времени суток, здоровяк!')
print("-" * 40)                        # Просто красивое оформление
# Задержка для визуального оформления и демонстрации усвоения материала
# Задержка была 2, но pytest не проходил из за своей задержки, поэтому 0.5 сек
time.sleep(0.5)


# Имя и возраст
user_name = input("Как тебя зовут?")
name = user_name.title()


while True:
    user_age = input("Какой твой возраст?")

    try:                                       # Пробую преобразовать str в int
        int_user_age = int(user_age)           # Проверяем на int + str в int
        break                                  # Стоп цикл, если все ок
    except ValueError:                         # Если не int, тогда ошибка
        print("Ошибка! Введите возраст цифрами. Пример: 25")


# Вес и  рост
user_weight = input("Укажите ваш вес(в кг): ")
kilo_weight = float(user_weight)  # Вес в float

user_height = input("Укажите ваш рост(формат: 1.75): ")
metre_height = float(user_height)


# Расчеты:

# 1. ИМТ
bmi = kilo_weight / (metre_height ** 2)
round_bmi = round(bmi, 1)              # Округляю ИМТ


# 2. Норма воды в миллилитрах
water_ml = kilo_weight * WATER_PER_KG
round_water_ml = round(water_ml, 1)    # Округляю до одного знака после запятой


# 3. Перевод в литры
water_l = water_ml / ML_IN_L
round_water_l = round(water_l, 1)


# Отчет для пользователя:

print("\n" + "=" * 40)                   # Просто красивое оформление
# имя и возраст пользователя;
print(f"Отчет для пользователя: {name}, Возраст: {user_age}")  # ф-строка
print("=" * 40)                          # Просто красивое оформление


# значение ИМТ (округлённое);
print(f"Твой Индекс Массы Тела: {round_bmi:1.1f}")

# норму воды в литрах
print(f"Рекомендуемая норма воды: {round_water_l:1.1f} л. в день")

print("=" * 40)                          # Просто красивое оформление

print(f"{name}, ты молодец! До скорой встречи!")  # дружелюбное завершение
print()
