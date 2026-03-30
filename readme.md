### Выявленные проблемы:
1. Повторные HTTP запросы (95% времени)
2. Многократный split() текста
3. Неэффективный ручной подсчёт в цикле

### Применённые оптимизации:
1. Кэширование ответа сервера
2. Однократная обработка текста
3. Использование Counter из collections


### Оригинальный файл:

    {'was': 1, 'this': 2, 'some': 0, 'yes': 0, 'say': 0, 'we': 3, 'too': 0, 'he': 0, 'no': 0, 'that': 7, 'cold': 0, 'by': 6, 'of': 108, 'will': 1, 'off': 0, 'how': 0, 'there': 0, 'a': 18, 'all': 4, 'is': 27, 'she': 0, 'our': 4, 'new': 5, 'must': 0, 'man': 0, 'why': 0, 'us': 0, 'then': 0, 'men': 0, 'me': 0, 'might': 0, 'so': 1, 'for': 26, 'would': 0, 'such': 4, 'than': 1, 'are': 10, 'or': 1, 'his': 0, 'the': 86, 'if': 4, 'with': 16, 'has': 2, 'could': 0, 'as': 12, 'out': 1, 'any': 0, 'may': 0, 'should': 1, 'cat': 0, 'does': 0, 'but': 0, 'be': 4, 'one': 2, 'to': 21, 'boy': 0, 'in': 35, 'can': 1, 'few': 0, 'sun': 0, 'dog': 0, 'hot': 0, 'her': 0, 'which': 2, 'two': 0, 'red': 0, 'where': 0, 'when': 0, 'my': 0, 'who': 0, 'sky': 0, 'sea': 0, 'you': 1, 'up': 0, 'had': 0, 'an': 4, 'and': 144, 'what': 0, 'on': 18, 'shall': 0, 'at': 3, 'yet': 0, 'big': 0, 'here': 0, 'not': 2, 'did': 0, 'old': 0, 'do': 0, 'they': 0, 'were': 0, 'now': 0, 'own': 1, 'it': 2}
             34412114 function calls (34349049 primitive calls) in 1625.745 seconds
    
       Ordered by: cumulative time
       List reduced from 701 to 20 due to restriction <20>
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.394    0.394 1625.867 1625.867 /Users/egor/PycharmProjects/hw_optimisation/original_main.py:16(main)
         7866   10.047    0.001 1625.473    0.207 /Users/egor/PycharmProjects/hw_optimisation/original_main.py:7(count_word_frequencies)
         7866    0.070    0.000 1610.477    0.205 /Users/egor/PycharmProjects/hw_optimisation/original_main.py:3(get_text)
         7866    0.157    0.000 1610.065    0.205 /Users/egor/Library/Python/3.9/lib/python/site-packages/requests/api.py:62(get)
         7866    0.139    0.000 1609.908    0.205 /Users/egor/Library/Python/3.9/lib/python/site-packages/requests/api.py:14(request)
         7866    0.164    0.000 1608.216    0.204 /Users/egor/Library/Python/3.9/lib/python/site-packages/requests/sessions.py:500(request)
         7866    0.350    0.000 1582.973    0.201 /Users/egor/Library/Python/3.9/lib/python/site-packages/requests/sessions.py:673(send)
         7866    0.261    0.000 1575.949    0.200 /Users/egor/Library/Python/3.9/lib/python/site-packages/requests/adapters.py:590(send)
         7866    0.261    0.000 1567.149    0.199 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connectionpool.py:592(urlopen)
         7866    0.299    0.000 1565.337    0.199 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connectionpool.py:377(_make_request)
         7866    0.083    0.000 1116.121    0.142 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connectionpool.py:1085(_validate_conn)
         7866    0.456    0.000 1116.029    0.142 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connection.py:724(connect)
         7866    0.456    0.000  745.344    0.095 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connection.py:901(_ssl_wrap_socket_and_match_hostname)
         7866    0.155    0.000  739.262    0.094 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/util/ssl_.py:413(ssl_wrap_socket)
         7866    0.056    0.000  689.552    0.088 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/util/ssl_.py:511(_ssl_wrap_socket_impl)
         7866    0.083    0.000  689.496    0.088 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py:494(wrap_socket)
         7866    0.391    0.000  689.413    0.088 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py:983(_create)
         7866    0.178    0.000  688.041    0.087 /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/ssl.py:1302(do_handshake)
         7866  687.795    0.087  687.795    0.087 {method 'do_handshake' of '_ssl._SSLSocket' objects}
         7866    0.499    0.000  445.310    0.057 /Users/egor/Library/Python/3.9/lib/python/site-packages/urllib3/connection.py:540(getresponse)
### Исходное использование памяти:
    Текущая использование памяти: 0.25 MB
    Пиковое использование памяти: 0.52 MB
### Доработанное использование памяти:
    Текущая использование памяти: 0.00 MB
    Пиковое использование памяти: 0.43 MB

### Проверка оригинальной скорости
    Оригинальное время: 1.727 секунд
    Итог: {'Phystech': 14, 'students': 7, 'research': 22, 'MIPT': 6, 'science': 1}
### Проверка исправленной скорости
    Оптимизированное время: 0.153 секунд
    Итог: {'Phystech': 14, 'students': 7, 'research': 22, 'MIPT': 6, 'science': 1}
### Улучшение: 11.3 раз
### Выигрыш времени: 1.574 секунд