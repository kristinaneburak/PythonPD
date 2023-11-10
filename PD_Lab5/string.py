class StringModule:
    def count_letters(word):
        """
        Функция для подсчета количества букв в слове.

        Параметры:
        word (str): Слово, в котором нужно подсчитать буквы.

        Возвращает:
        int: Количество букв в слове.
        """
        return len([letter for letter in word if letter.isalpha()])

    def count_words(sentence):
        """
        Функция для подсчета количества слов в предложении.

        Параметры:
        sentence (str): Предложение, в котором нужно подсчитать слова.

        Возвращает:
        int: Количество слов в предложении.
        """
        return len(sentence.split())

    def count_vowels(word):
        """
        Функция для подсчета количества гласных букв в слове.

        Параметры:
        word (str): Слово, в котором нужно подсчитать гласные буквы.

        Возвращает:
        int: Количество гласных букв в слове.
        """
        vowels = "aeiouAEIOU"
        return len([letter for letter in word if letter in vowels])

    def concatenate_strings(str1, str2):
        """
        Функция для конкатенации двух строк.

        Параметры:
        str1 (str): Первая строка.
        str2 (str): Вторая строка.

        Возвращает:
        str: Результат конкатенации двух строк.
        """
        return str1 + str2

    def multiply_string(str1, n):
        """
        Функция для умножения строки на число.

        Параметры:
        str1 (str): Строка, которую нужно умножить.
        n (int): Число, на которое нужно умножить строку.

        Возвращает:
        str: Результат умножения строки на число.
        """
        return str1 * n
