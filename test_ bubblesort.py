import main
import pytest

# Тест функции, которая сортирует список
class TestBubblesort:

    # Тестируем программу на коррктных данных. Функция возвращает отсортированный список элементов.
    def test_on_correct_n(self):
        assert main.bubblesort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 5]

    # Тестируем программу на некорретных данных. Функция вызывает исключение TypeError.
    def test_on_negative(self):
        assert main.bubblesort([1, 5, 3, 2, 4]) == [1, 2, 3, 4, 4]


# Тестируем программу на некорретных данных. Функция вызывает исключение TypeError.
    def test_on_negative1(self):
        with pytest.raises(TypeError):
            main.bubblesort('hi')