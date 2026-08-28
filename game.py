import random

number = random.randint(1, 10)

print("🎮 Угадай число!")
print("Я загадал число от 1 до 10.")

guess = int(input("Твоё число: "))

if guess == number:
    print("🎉 Правильно!")
else:
    print("❌ Неправильно!")
    print("Я загадал:", number)