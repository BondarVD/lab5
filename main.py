import string


def read_first_sentence(file_path):
    """
    Зчитує перше речення з файлу.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = text.split('.')
            first_sentence = sentences[0].strip() + '.' if sentences else ""
            return first_sentence
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None


def sort_words(text):
    """
    Сортує слова за алфавітом, спочатку українські, потім англійські.
    """
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    ukr_words = sorted([word for word in words if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)])
    eng_words = sorted([word for word in words if any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in word)])
    return ukr_words, eng_words


def process_file(file_path):
    """
    Основна функція для обробки текстового файлу.
    """
    # Зчитуємо перше речення
    first_sentence = read_first_sentence(file_path)
    if not first_sentence:
        return

    print("Перше речення з файлу:")
    print(first_sentence)

    # Сортуємо слова
    ukr_words, eng_words = sort_words(first_sentence)
    all_words = ukr_words + eng_words

    print("\nСлова у тексті, відсортовані по алфавіту:")
    print("Українські слова:", ukr_words)
    print("Англійські слова:", eng_words)
    print("\nЗагалом слів у тексті:", len(all_words))


if __name__ == "__main__":
    # Назва текстового файлу
    file_name = "input.txt"

    # Запуск програми
    process_file(file_name)
