"""Demo entry point for the lend-book library.

Run with:
    python -m examples.demo
or (if installed via `pip install -e .`):
    lend-book-demo
"""

from lend_book import BookModel, Manager, UserNormalModel, UserPremiumModel
from lend_book.configs.logger_config import setup_logger

logger = setup_logger("lend-book - examples/demo.py")


def main() -> None:
    # Library
    library = Manager(name="Libreria LaRosca")

    # Books
    dracula_book = BookModel(
        name="Drácula",
        description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.",
        author="Bram Stoker",
        units=20,
    )
    la_clase_de_griego_book = BookModel(
        name="LA CLASE DE GRIEGO",
        description="En Seúl, una mujer asiste a clases de griego antiguo.",
        author="KANG, HAN",
        units=1,
    )
    gravity_falls_book = BookModel(
        name="Gravity Falls",
        description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.",
        author="Alex Hirsch",
        units=5,
    )

    # Users
    user_normal = UserNormalModel(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormalModel(name="Sergio", surname="Sorg", address="Calle False 12345")
    user_premium = UserPremiumModel(name="Carlos", surname="Skere", address="Calle False 1234")

    library.register_user(user=user_normal)
    library.register_user(user=user_normal_2)
    library.register_user(user=user_premium)

    library.add_book(dracula_book)
    library.add_book(la_clase_de_griego_book)
    library.add_book(gravity_falls_book)

    library.rent_book(user=user_normal, book=dracula_book)
    library.rent_book(user=user_premium, book=dracula_book)
    library.rent_book(user=user_premium, book=la_clase_de_griego_book)
    library.rent_book(user=user_premium, book=gravity_falls_book)

    library.return_book(user=user_normal)
    library.return_book(user=user_premium, book=dracula_book)

    logger.info(library)
    library.str_users()
    library.str_books()


if __name__ == "__main__":
    main()
