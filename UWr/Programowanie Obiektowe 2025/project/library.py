from datetime import date, datetime


class Book:
    def __init__(self, title: str, author: str, total_copies: int , book_id: int, reserved: int = 0):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.book_id = book_id
        self.reserved = reserved

    def is_available(self) -> bool:
        return self.available_copies > 0

    def borrow_copy(self) -> bool:

        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_copy(self) -> None:
        self.available_copies += 1

    def __str__(self) -> str:
        return f'{self.title} by {self.author} - {self.available_copies}/{self.total_copies} copies available.'

class User:

    def __init__(self, name: str, user_id: int, borrowed_books: list = None):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def borrow_book(self, book) -> bool:
        if book.borrow_copy():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book) -> bool:
        if book in self.borrowed_books:
            book.return_copy()
            self.borrowed_books.remove(book)
            return True
        return False

class Reader(User):
    def __init__(self, name: str, user_id: int, borrowed_books: list = None, reservation_history: list = None):
        super().__init__(name, user_id, borrowed_books)
        self.reservation_history = reservation_history if reservation_history is not None else []

    def reserve_book(self, book) -> bool:
        if book.reserved < book.available_copies:
            book.reserved += 1
            self.reservation_history.append(book)
            return True
        return False

    def get_reservation_history(self):
        return self.reservation_history

class Librarian(User):
    def __init__(self, name: str, user_id: int, borrowed_books: list = None):
        super().__init__(name, user_id, borrowed_books)

    def add_book(self, book, library) -> None :
        library.add_book(book)

    def remove_book(self, book, library) -> None:
        library.remove_book(book)

    def create_user(self, library, user) -> None:
        library.add_user(user)

    def block_user(self, user) -> None:
        user.blocked = True

class Loan:
    def __init__(self, user_id: int, book: str, reservation_date: str, return_date: str, actual_return_date: str):
        self.user_id = user_id
        self.book = book
        self.reservation_date = reservation_date
        self.return_date = return_date
        self.actual_return_date = actual_return_date

    def is_overdue(self) -> bool:
        current_date = date.today()
        if datetime.strptime(self.return_date, '%d-%m-%Y').date() < current_date:
            return True
        return False

    def overdue_cost(self) -> int:
        if self.is_overdue():
            current_date = date.today()
            overdue_time = current_date - datetime.strptime(self.return_date, '%d-%m-%Y').date()
            return overdue_time.days * 2

class Reservation:
    def __init__(self, book: Book, user: User, return_date: str, active: bool):
        self.book = book
        self.user = user
        self.return_date = return_date
        self.active = True

    def is_expired(self) -> bool:
        current_date = date.today()
        if current_date > datetime.strptime(self.return_date, '%d-%m-%Y').date():
            return True
        return False

    def cancel_reservation(self) -> bool:
        if self.active:
            if self.book.reserved > 0:
                self.book.reserved -= 1

            if self in self.user.borrowed_books:
                self.user.borrowed_books.remove(self)

            self.active = False
            return True
        return False









