from books_sdk import get_book_by_id, get_author

print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM',1)))

# Гипотеза 1: Неправильные скобки
# Способ проверки:  Удалить весь код, кроме скобок, и проверить их количество и порядок
# Установленный факт: получилось ((()))
# Вывод: Гипотеза опроверглась, со скобками всё в порядке

# Гипотеза 2: Ошибка во вложенной функции
# Способ проверки: Запустить вложенную функцию отдельно от внешней
# Код для проверки: print(get_author)  print(get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM'))
# Установленный факт: ошибка print(get_author) print(get_book_by_id(1, 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM'))
# Вывод: гипотеза опроверглась, с вложенной функцией все в порядке

# Гипотеза 3: Проблема в типе данных, 1 должно быть числом
# Способ проверки: добавить''
# Код для проверки: print(get_author(get_book_by_id('1', 'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: с ковычками 1 передается как строка
# Вывод: код функционирует при типе данных число

# Гипотеза 4: Книги с номером 1 не существует
# Способ проверки: попробовать запросить книгу с номером 2
# Код для проверки: print(get_author(get_book_by_id(2,'AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM')))
# Установленный факт: не получилось выполнить запрос, потому что книги с номером 2 не существует
# Вывод: id книги верный

# Гипотеза 5:  Аргументы перепутаны местами
# Способ проверки: поменять местами аргументы
# Код для проверки: print(get_author(get_book_by_id('AAECTkuGjWo1Imwr-_6UrN-nzbo89sd3WSM',1)))
# Установленный факт: получилось выполнить запрос
# Вывод: гипотеза подтвердилась