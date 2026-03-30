import time
import requests
from collections import Counter


def original_approach(url, words_to_count):

    def get_text(url):
        response = requests.get(url)
        return response.text

    def count_word_frequencies(url, word):
        text = get_text(url)
        words = text.split()
        count = 0
        for w in words:
            if w == word:
                count += 1
        return count

    frequencies = {}
    for word in words_to_count:
        frequencies[word] = count_word_frequencies(url, word)

    return frequencies


def optimized_approach(url, words_to_count):
    response = requests.get(url)
    text = response.text

    all_words = text.split()
    word_counter = Counter(all_words)

    frequencies = {}
    for word in words_to_count:
        frequencies[word] = word_counter.get(word, 0)

    return frequencies


def compare():
    words_to_count = ["Phystech", "students", "research", "MIPT", "science"] * 2  # 10 words
    url = "https://eng.mipt.ru/why-mipt/"

    print("Проверка оригинальной скорости")
    start = time.time()
    orig_result = original_approach(url, words_to_count)
    orig_time = time.time() - start
    print(f"Оригинальное время: {orig_time:.3f} секунд")
    print(f"Итог: {orig_result}")

    print("Проверка исправленной скорости")
    start = time.time()
    opt_result = optimized_approach(url, words_to_count)
    opt_time = time.time() - start
    print(f"Оптимизированное время: {opt_time:.3f} секунд")
    print(f"Итог: {opt_result}")

    print(f"Улучшение: {orig_time / opt_time:.1f} раз")
    print(f"Выигрыш времени: {orig_time - opt_time:.3f} секунд")



if __name__ == "__main__":
    compare()