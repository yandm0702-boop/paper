# Файл: tests/test_library.py
# Это простейший пример. Вам нужно заменить его на свои тесты!

from src.library import Library  # Импортируем ваш класс Библиотека из вашего же кода

def test_add_book():
    """Тест на добавление книги"""
    my_lib = Library()
    my_lib.add_book("Война и мир")
    # Проверяем, что книга добавилась. Предположим, у библиотеки есть список `books`
    assert "Война и мир" in my_lib.books

def test_remove_book():
    """Тест на удаление книги"""
    my_lib = Library()
    my_lib.add_book("Преступление и наказание")
    my_lib.remove_book("Преступление и наказание")
    assert "Преступление и наказание" not in my_lib.books
