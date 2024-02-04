class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    """Бумажная книга"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.validate_pages(pages)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        self.validate_pages(pages)
        self._pages = pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"

    @staticmethod
    def validate_pages(pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")


class AudioBook(Book):
    """Аудиокнига"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.validate_duration(duration)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        self.validate_duration(duration)
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._duration:.1f})"

    @staticmethod
    def validate_duration(duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть вещественным числом")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")


if __name__ == "__main__":
    base_book = Book(name="Война и мир", author="Толстой Л.Н.")
    paper_book = PaperBook(name="Война и мир", author="Толстой Л.Н.", pages=1000)
    audio_book = AudioBook(name="Война и мир", author="Толстой Л.Н.", duration=3600.0)

    print(base_book)
    print("Бумажная книга: Название -", paper_book.name)
    print("Аудиокнига: Автор -", audio_book.author)
    print()

    paper_book.pages = 2000
    audio_book.duration = 7200.0
    print("Бумажная книга: Количество страниц -", paper_book.pages)
    print("Аудиокнига: Продолжительность  -", audio_book.duration)
    print()

    print(repr(Book(name="Война и мир", author="Толстой Л.Н.")))
    print(repr(PaperBook(name="Война и мир", author="Толстой Л.Н.", pages=1000)))
    print(repr(AudioBook(name="Война и мир", author="Толстой Л.Н.", duration=3600.0)))
