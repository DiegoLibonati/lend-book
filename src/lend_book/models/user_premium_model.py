from lend_book.constants.codes import CODE_ALREADY_EXISTS_BOOK_RENTED, CODE_ERROR_OUT_OF_STOCK, CODE_NOT_FOUND_RENTED_BOOK
from lend_book.constants.messages import MESSAGE_ALREADY_EXISTS_BOOK_RENTED, MESSAGE_ERROR_OUT_OF_STOCK, MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME
from lend_book.models.book_model import BookModel
from lend_book.models.user_model import UserModel
from lend_book.utils.exceptions import BusinessError, NotFoundError


class UserPremiumModel(UserModel):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_books: list[BookModel] = []

    @property
    def rented_books(self) -> list[BookModel]:
        return self.__rented_books

    def rent_book(self, book: BookModel) -> None:
        if book in self.rented_books:
            raise BusinessError(code=CODE_ALREADY_EXISTS_BOOK_RENTED, message=MESSAGE_ALREADY_EXISTS_BOOK_RENTED.format(name=book.name))

        if not book.stock:
            raise BusinessError(code=CODE_ERROR_OUT_OF_STOCK, message=MESSAGE_ERROR_OUT_OF_STOCK.format(name=book.name))

        book.decrease_unit()
        self.__rented_books.append(book)

    def return_book(self, book: BookModel) -> None:
        if book not in self.rented_books:
            raise NotFoundError(code=CODE_NOT_FOUND_RENTED_BOOK, message=MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME.format(name=book.name))

        book.increase_unit()
        self.__rented_books.remove(book)

    def _get_list_name_rented_books(self) -> list[str]:
        return [book.name for book in self.rented_books]

    def __str__(self) -> None:
        return (
            f"----- User Premium {self.id} -----\n"
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Books Rented: {self._get_list_name_rented_books()}\n\n"
        )
