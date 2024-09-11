from src.Book import Book
from src.User import User


class Library:
    def __init__(self) -> None:
        self.__books: list = []
        self.__users: list = []
        self.__checked_out_books: list = []
        self.__checked_in_books: list = []

    # Getters
    def get_books(self) -> list:
        return self.__books

    def get_users(self) -> list:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        book_to_add: Book = Book(isbn,title, author)
        self.__books.append(book_to_add)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(book.__str__())

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date) -> str:
        book_to_checkout = self.__books[0]
        user_checkouting = self.__users[0]
        check_book = False
        check_user = False
        for book in self.__books:
            if book.get_isbn() == isbn:
                book_to_checkout = book
                check_book = True

        for user in self.__users:
            if user.get_dni() == dni:
                user_checkouting = user
                check_user = True
        if not check_book and not check_user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"
        else:
            if not book_to_checkout.is_available():
                return f"Book {isbn} is not available"
            else:
                self.__checked_out_books.append([isbn, dni, due_date])
                user_checkouting.increment_checkouts()
                book_to_checkout.set_available(False)
                return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        book_to_checkin = Book(isbn,'','')
        user_checking_in = User('','')
        check_book = False
        for book in self.__books:
            if book == book_to_checkin:
                book_to_checkin = book
                check_book = True

        for user in self.__users:
            if user.get_dni() == dni:
                user_checking_in == user

        if not check_book and book_to_checkin.is_available():
            return f"Book {isbn} is not available"
        else:
            book_to_checkin.set_available(True)
            user_checking_in.increment_checkins()
            self.__checked_in_books.append(book_to_checkin)
            for book2 in self.__checked_out_books:
                if book2[0] == book_to_checkin.get_isbn():
                    self.__checked_out_books.remove(book2)
            return f"Book {isbn} checked in by user {dni}"


    # Utils
    def add_user(self, dni, name) -> None:
        user = User(dni,name)
        self.__users.append(user)
