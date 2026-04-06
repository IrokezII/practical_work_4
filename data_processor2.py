import sys

def parse_numbers(raw: str) -> list[int]:
    parts = raw.strip().split()
    if not parts:
        return []
    return list(map(int, parts))

def process_numbers(numbers: list[int]) -> dict:
    if not numbers:
        return {"sum": 0, "min": None, "max": None, "avg": None, "count": 0}
    return {
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "avg": round(sum(numbers) / len(numbers), 2),
        "count": len(numbers)
    }

def process_string(text: str, mode: str = "upper") -> str:
    if mode == "upper":
        return text.upper()
    elif mode == "lower":
        return text.lower()
    elif mode == "reverse":
        return text[::-1]
    else:
        return text

# НОВАЯ ФУНКЦИЯ: подсчёт гласных букв
def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

# НОВАЯ ФУНКЦИЯ: проверка, является ли строка палиндромом (без учёта регистра и пробелов)
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

def main():
    # ИЗМЕНЕНО: более яркое приветствие
    print("       РАСШИРЕННЫЙ ОБРАБОТЧИК ЧИСЕЛ И СТРОК")
    print()

    num_input = input("Введите целые числа через пробел: ")
    numbers = parse_numbers(num_input)

    text = input("Введите любую строку: ")

    mode = input("Выберите режим преобразования строки (upper/lower/reverse): ").strip().lower()

    stats = process_numbers(numbers)
    transformed = process_string(text, mode)

    # ИЗМЕНЕНО: добавлен разделитель и дополнительная информация
    print("РЕЗУЛЬТАТЫ ОБРАБОТКИ")

    print(f"📊 Чисел получено: {stats['count']}")
    if stats['count'] > 0:
        print(f"   Сумма: {stats['sum']}")
        print(f"   Минимум: {stats['min']}")
        print(f"   Максимум: {stats['max']}")
        print(f"   Среднее: {stats['avg']}")
    else:
        print("   Числа не введены.")

    # НОВОЕ: вывод статистики по строке
    print(f"\n📝 Строка: '{text}'")
    print(f"   Длина строки: {len(text)} символов")
    print(f"   Количество гласных букв: {count_vowels(text)}")          # НОВОЕ
    palindrom_flag = is_palindrome(text)                                # НОВОЕ
    print(f"   Является палиндромом: {'Да' if palindrom_flag else 'Нет'}")  # НОВОЕ

    print(f"\n🔄 Преобразованная строка (режим {mode}): '{transformed}'")

    # ИЗМЕНЕНО: завершающая линия
    print("          Обработка завершена")

if __name__ == "__main__":
    main()