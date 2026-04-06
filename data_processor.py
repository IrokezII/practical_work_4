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


def main():
    print("Обработчик чисел и строк\n")

    num_input = input("Введите целые числа через пробел: ")
    numbers = parse_numbers(num_input)

    text = input("Введите любую строку: ")

    mode = input("Выберите режим (upper/lower/reverse): ").strip().lower()

    stats = process_numbers(numbers)
    transformed = process_string(text, mode)

    print("\nРезультаты")
    print(f"Чисел получено: {stats['count']}")
    if stats['count'] > 0:
        print(f"Сумма: {stats['sum']}")
        print(f"Минимум: {stats['min']}")
        print(f"Максимум: {stats['max']}")
        print(f"Среднее: {stats['avg']}")
    else:
        print("Числа не введены.")

    print(f"Исходная строка: '{text}'")
    print(f"Преобразованная строка (режим {mode}): '{transformed}'")


if __name__ == "__main__":
    main()