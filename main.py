class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id_ должен быть целым числом")
        if id_ < 0:
            raise ValueError("id_ должен быть неотрицательным числом")
        self.id_ = id_

        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        self.name = name

        if not isinstance(id_, int):
            raise TypeError("pages должен быть целым числом")
        if id_ < 1:
            raise ValueError("pages должен быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = []):
        if not isinstance(books, list):
            raise TypeError("books должен быть списком")
        for book in books:
            if not isinstance(book, Book):
                raise TypeError(
                    "Список books должен содержать только элементы Book или быть пустым"
                )
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return max(self.books, key=lambda x: x.id_).id_ + 1

    def get_index_by_book_id(self, id_: int):
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        return ValueError("Книги с запрашиваемым id не существует")


if __name__ == "__main__":
    lib = Library()
    print(lib.get_next_book_id())
    print(lib.get_index_by_book_id(3))
