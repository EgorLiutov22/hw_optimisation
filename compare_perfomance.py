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

    print("Testing ORIGINAL approach...")
    start = time.time()
    orig_result = original_approach(url, words_to_count)
    orig_time = time.time() - start
    print(f"Original time: {orig_time:.3f} seconds")
    print(f"Result: {orig_result}")

    print("Testing OPTIMIZED approach...")
    start = time.time()
    opt_result = optimized_approach(url, words_to_count)
    opt_time = time.time() - start
    print(f"Optimized time: {opt_time:.3f} seconds")
    print(f"Result: {opt_result}")

    print(f"SPEEDUP: {orig_time / opt_time:.1f}x faster")
    print(f"TIME SAVED: {orig_time - opt_time:.3f} seconds")
    print("=" * 60)


if __name__ == "__main__":
    compare()