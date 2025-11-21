import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageColor

#введення цілого числа з перевіркою
def input_int(prompt: str, min_value=None, max_value=None) -> int:
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if min_value is not None and num < min_value:
                print(f"Число має бути не менше {min_value}.")
                continue
            if max_value is not None and num > max_value:
                print(f"Число має бути не більше {max_value}.")
                continue
            return num
        except ValueError:
            print("Помилка: введіть ціле число.")

#перевірка так/ні
def yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (так/ні): ").strip().lower()
        if ans in ("так", "yes"):
            return True
        if ans in ("ні", "no"):
            return False
        print("Введіть 'так' або 'ні'.")

#перевірка шляху до файлу
def input_file(prompt: str) -> str:
    while True:
        path = input(prompt).strip().strip('"')
        if path == "":
            print("Ввід порожній. Спробуйте ще раз.")
            continue
        if os.path.isfile(path):
            return path
        print("Файл не знайдено. Перевірте шлях і спробуйте ще раз.")

#поточний стан листівки
class ProjectState:

    def __init__(self):
        self.image = None
        self.greeting_text = ""
        self.history = []

    #збереження поточного зображення
    def backup(self):
        if self.image is not None:
            self.history.append(self.image.copy())

#завантажити фонове зображення
def background(state: ProjectState):
    path = input_file("Введіть шлях до фонового зображення: ")
    try:
        img = Image.open(path).convert("RGBA")
    except OSError:
        print("Файл не є коректним зображенням.")
        return

    state.image = img
    state.history.clear()
    print(f"Фон завантажено: {os.path.basename(path)} ({img.width}x{img.height})")

#завантижити текстовий файл
def text_file(state: ProjectState):
    path = input_file("Введіть шлях до TXT-файлу: ")
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except Exception as e:
        print(f"Не вдалося прочитати файл: {e}")
        return

    if not text:
        print("Файл порожній.")
        return

    state.greeting_text = text
    print("Текст завантажено.")

#змінити розмір
def resize(state: ProjectState):
    if state.image is None:
        print("Спочатку завантажте фонове зображення.")
        return

    print(f"Поточний розмір: {state.image.width}x{state.image.height}")
    mode = input_int("Оберіть режим: 1 - нова ширина, 2 - масштаб (%): ", 1, 2)

    if mode == 1:
        new_w = input_int("Нова ширина (пікселі): ", min_value=10)
        new_h = int(state.image.height * new_w / state.image.width)
    else:
        scale = input_int("Масштаб у % (10-300): ", 10, 300) / 100
        new_w = int(state.image.width * scale)
        new_h = int(state.image.height * scale)

    state.backup()
    state.image = state.image.resize((new_w, new_h), Image.LANCZOS)
    print(f"Новий розмір: {new_w}x{new_h}")

#вибрати шрифт
def set_font():
    path = input("Введіть шлях до .ttf для власного шрифту (Enter для стандартного): ").strip().strip('"')
    size = input_int("Розмір шрифту: ", 8)

    if path:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            print("Не вдалося завантажити шрифт. Використовую стандартний.")
    return ImageFont.load_default()

#додати текст
def add_text(state: ProjectState):
    if state.image is None:
        print("Спочатку завантажте фонове зображення.")
        return
    if state.greeting_text:
        if yes_no("Використати текст із файлу?"):
            text = state.greeting_text
        else:
            text = input("Введіть текст: ")
    else:
        text = input("Введіть текст: ")
    if not text.strip():
        print("Текст порожній.")
        return

    x = input_int("Ширина X: ", 0)
    y = input_int("Висота Y: ", 0)
    font = set_font()

    while True:
        color = input("Колір тексту (RGB або назва): ").strip()
        parts = color.split()

        if len(parts) == 3 and all(p.isdigit() for p in parts):
            text_color = tuple(map(int, parts))
            break
        else:
            try:
                ImageColor.getrgb(color)
                text_color = color
                break
            except ValueError:
                print("Невідомий колір. Спробуйте ще раз.")
    state.backup()
    draw = ImageDraw.Draw(state.image)
    draw.text((x, y), text, font=font, fill=text_color)
    print("Текст додано.")

#додати наклейку
def add_sticker(state: ProjectState):
    if state.image is None:
        print("Спочатку завантажте фонове зображення.")
        return

    path = input_file("Шлях до наклейки: ")
    try:
        sticker = Image.open(path).convert("RGBA")
    except OSError:
        print("Не вдалося відкрити наклейку.")
        return

    scale = input_int("Масштаб наклейки (%): ", 10, 300) / 100
    new_w = int(sticker.width * scale)
    new_h = int(sticker.height * scale)
    sticker = sticker.resize((new_w, new_h), Image.LANCZOS)
    x = input_int("X: ", 0)
    y = input_int("Y: ", 0)

    state.backup()
    state.image.alpha_composite(sticker, (x, y))
    print("Наклейку додано.")

#додати фільтр
def add_filter(state: ProjectState):
    if state.image is None:
        print("Спочатку завантажте фонове зображення.")
        return

    print("\nОберіть фільтр:")
    print("1 - Чорно-білий")
    print("2 - Розмиття")
    print("3 - Різкість")
    print("4 - Збільшити яскравість")
    print("5 - Зменшити яскравість")
    choice = input_int("Ваш вибір: ", 1, 5)
    state.backup()

    if choice == 1:
        state.image = state.image.convert("L").convert("RGBA")
    elif choice == 2:
        rad = input_int("Радіус (1-10): ", 1, 10)
        state.image = state.image.filter(ImageFilter.GaussianBlur(radius=rad))
    elif choice == 3:
        intense = input_int("Інтенсивність різкості (50-300): ", 50, 300)
        state.image = state.image.filter(ImageFilter.UnsharpMask(radius=2, percent=intense))
    elif choice in (4, 5):
        factor = input_int("Коефіцієнт (50-300): ", 50, 300) / 100
        if choice == 5:
            factor = 1 / factor
        bright = ImageEnhance.Brightness(state.image)
        state.image = bright.enhance(factor)

    print("Фільтр застосовано.")

#попередній перегляд
def preview(state: ProjectState):
    if state.image is None:
        print("Немає зображення.")
        return
    state.image.show()

#скасувати крок
def undo(state: ProjectState):
    if not state.history:
        print("Немає попередніх станів.")
        return
    state.image = state.history.pop()
    print("Повернуто попередній стан.")

#зберегти результат
def save(state: ProjectState):
    if state.image is None:
        print("Немає що зберігати.")
        return

    filename = input("Назва файлу (без розширення): ").strip()
    if not filename:
        print("Порожня назва.")
        return

    img_path = filename + ".png"

    try:
        state.image.save(img_path)
    except Exception as e:
        print(f"Помилка під час збереження: {e}")
        return
    print(f"Зображення збережено як {img_path}")

#меню
def main_menu():
    state = ProjectState()

    while True:
        print("\n========== МЕНЮ ==========")
        print("1 - Завантажити фон")
        print("2 - Завантажити текст")
        print("3 - Змінити розмір")
        print("4 - Додати текст на зображення")
        print("5 - Додати наклейку")
        print("6 - Фільтри")
        print("7 - Попередній перегляд")
        print("8 - Повернутись на попередній крок")
        print("9 - Зберегти")
        print("0 - Вихід")

        choice = input_int("Ваш вибір: ", 0, 9)
        if choice == 0:
            print("Роботу завершено.")
            break
        elif choice == 1:
            background(state)
        elif choice == 2:
            text_file(state)
        elif choice == 3:
            resize(state)
        elif choice == 4:
            add_text(state)
        elif choice == 5:
            add_sticker(state)
        elif choice == 6:
            add_filter(state)
        elif choice == 7:
            preview(state)
        elif choice == 8:
            undo(state)
        elif choice == 9:
            save(state)

if __name__ == "__main__":
    print("Програма створення персоналізованих листівок.")
    main_menu()