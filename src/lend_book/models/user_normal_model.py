from lend_book.constants.codes import CODE_ERROR_BOOK_RETURN_REQUIRED, CODE_ERROR_OUT_OF_STOCK, CODE_NOT_FOUND_RENTED_BOOK
from lend_book.constants.messages import MESSAGE_ERROR_BOOK_RETURN_REQUIRED, MESSAGE_ERROR_OUT_OF_STOCK, MESSAGE_NOT_FOUND_RENTED_BOOK
from lend_book.models.book_model import BookModel
from lend_book.models.user_model import UserModel
from lend_book.utils.exceptions import BusinessError, NotFoundError


class UserNormalModel(UserModel):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_book: BookModel = None

    @property
    def rented_book(self) -> BookModel:
        return self.__rented_book

    def rent_book(self, book: BookModel) -> None:
        if self.rented_book:
            raise BusinessError(code=CODE_ERROR_BOOK_RETURN_REQUIRED, message=MESSAGE_ERROR_BOOK_RETURN_REQUIRED.format(name=self.rented_book.name))

        if not book.stock:
            raise BusinessError(code=CODE_ERROR_OUT_OF_STOCK, message=MESSAGE_ERROR_OUT_OF_STOCK.format(name=book.name))

        book.decrease_unit()
        self.__rented_book = book

    def return_book(self) -> None:
        if not self.rented_book:
            raise NotFoundError(code=CODE_NOT_FOUND_RENTED_BOOK, message=MESSAGE_NOT_FOUND_RENTED_BOOK)

        self.rented_book.increase_unit()
        self.__rented_book = None

    def __str__(self) -> None:
        return (
            f"----- User Normal Model {self.id} -----\n"
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Book Rented: {self.rented_book.name if self.rented_book else None}\n\n"
        )
