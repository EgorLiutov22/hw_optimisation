import tracemalloc
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


def profile_memory():
    words_to_count = ["Phystech", "students", "research", "MIPT", "science"]
    url = "https://eng.mipt.ru/why-mipt/"

    print("Исходное использование памяти:")

    tracemalloc.start()
    original_approach(url, words_to_count)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая использование памяти: {current / 1024 / 1024:.2f} MB")
    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} MB")
    tracemalloc.stop()

    print("Доработанное использование памяти:")
    tracemalloc.start()
    optimized_approach(url, words_to_count)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая использование памяти: {current / 1024 / 1024:.2f} MB")
    print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} MB")
    tracemalloc.stop()


if __name__ == "__main__":
    profile_memory()