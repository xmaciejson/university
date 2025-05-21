from datetime import date, datetime
import json

class Book:

    def __init__(self, title: str, author: str, total_copies: int , book_id: int, reserved: int = 0):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.book_id = book_id
        self.reserved = reserved

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'book_id': self.book_id,
            'reserved': self.reserved
        }

    @staticmethod
    def from_dict(data: dict):
        book = Book(
            title=data['title'],
            author=data['author'],
            total_copies=data['total_copies'],
            book_id=data['book_id'],
            reserved=data.get('reserved', 0)
        )
        book.available_copies = data.get('available_copies', book.total_copies)
        return book

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

    def __init__(self, name: str, user_id: int, is_blocked: bool = False, borrowed_books: list = None):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        self.is_blocked = is_blocked

    def to_dict(self):
        return {
            'type': 'User',
            'name': self.name,
            'user_id': self.user_id,
            'borrowed_books': [book.book_id for book in self.borrowed_books],
            'is_blocked': self.is_blocked
        }

    @staticmethod
    def from_dict(data: dict):
        user = User(
            name=data['name'],
            user_id=data['user_id'],
            borrowed_books=[],
            is_blocked=data['is_blocked']
        )
        return user

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
    def __init__(self, name: str, user_id: int, is_blocked: bool = False, borrowed_books: list = None, reservation_history: list = None):
        super().__init__(name=name, user_id=user_id, is_blocked=is_blocked, borrowed_books=borrowed_books)
        self.reservation_history = reservation_history if reservation_history is not None else []

    def to_dict(self):
        data = super().to_dict()
        data['type'] = 'Reader'
        data['reservation_history'] = [book.book_id for book in self.reservation_history]
        return data

    @staticmethod
    def from_dict(data: dict):
        reader = Reader(
            name=data['name'],
            user_id=data['user_id'],
            is_blocked=data['is_blocked'],
            borrowed_books=[],
            reservation_history=[]
        )
        return reader

    def reserve_book(self, book) -> bool:
        if book.reserved < book.available_copies:
            book.reserved += 1
            self.reservation_history.append(book)
            return True
        return False

    def get_reservation_history(self):
        return self.reservation_history

class Librarian(User):
    def __init__(self, name: str, user_id: int, is_blocked: bool = False, borrowed_books: list = None):
        super().__init__(name=name, user_id=user_id, is_blocked=is_blocked, borrowed_books=borrowed_books)

    def to_dict(self):
        data = super().to_dict()
        data['type'] = 'Librarian'
        return data

    @staticmethod
    def from_dict(data: dict):
        librarian = Librarian(
            name=data['name'],
            user_id=data['user_id'],
            is_blocked=data['is_blocked'],
            borrowed_books=[]
        )
        return librarian

    def add_book(self, book, library) -> None :
        library.add_book(book)

    def remove_book(self, book, library) -> None:
        library.remove_book(book)

    def create_user(self, library, user) -> None:
        library.add_user(user)

    def block_user(self, user) -> None:
        user.is_blocked = True

class Loan:
    def __init__(self, user_id: int, book: str, reservation_date: str, return_date: str, actual_return_date: str):
        self.user_id = user_id
        self.book = book
        self.reservation_date = reservation_date
        self.return_date = return_date
        self.actual_return_date = actual_return_date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'book': self.book,
            'reservation_date': self.reservation_date,
            'return_date': self.return_date,
            'actual_return_date': self.actual_return_date
        }
    @staticmethod
    def from_dict(data: dict):
        loan = Loan(
            user_id=data['user_id'],
            book=data['book'],
            reservation_date=data['reservation_date'],
            return_date=data['return_date'],
            actual_return_date=data['actual_return_date']
        )
        return loan

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
        return 0

class Reservation:
    def __init__(self, book: Book, user: User, return_date: str, active: bool = True):
        self.book = book
        self.user = user
        self.return_date = return_date
        self.active = active

    def to_dict(self):
        return {
            'book_id': self.book.book_id,
            'user_id': self.user.user_id,
            'return_date': self.return_date,
            'active': self.active
        }

    @staticmethod
    def from_dict(data: dict, books_id, users_id):
        book = books_id.get(data['book_id'])
        user = users_id.get(data['user_id'])
        if book is None or user is None:
            raise ValueError('Book or user not found!')
        return Reservation(
            book=book,
            user=user,
            return_date=data['return_date'],
            active=data['active']
        )

    def is_expired(self) -> bool:
        current_date = date.today()
        if current_date > datetime.strptime(self.return_date, '%d-%m-%Y').date():
            return True
        return False

    def cancel_reservation(self) -> bool:
        if self.active:
            if self.book.reserved > 0:
                self.book.reserved -= 1

            if self.book in self.user.borrowed_books:
                self.user.borrowed_books.remove(self.book)

            self.active = False
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.borrows_list = []
        self.reservations = []

    def add_user(self, user: User) -> None:
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user: User) -> None:
        if user in self.users:
            self.users.remove(user)

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)

    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)

    def add_loan(self, loan: Loan) -> None:
        if loan not in self.borrows_list:
            self.borrows_list.append(loan)

    def remove_loan(self, loan: Loan) -> None:
        if loan in self.borrows_list:
            self.borrows_list.remove(loan)

    def add_reservation(self, reservation: Reservation):
        if reservation not in self.reservations:
            self.reservations.append(reservation)

    def remove_reservation(self, reservation: Reservation):
        if reservation in self.reservations:
            reservation.cancel_reservation()
            self.reservations.remove(reservation)


class FileManager:
    @staticmethod
    def save_library(library):
        with open('books.json', 'w') as file:
            json.dump([book.to_dict() for book in library.books], file)

        with open('users.json', 'w') as file:
            json.dump([user.to_dict() for user in library.users], file)

        with open('reservations.json', 'w') as file:
            json.dump([reservation.to_dict() for reservation in library.reservations], file)

        with open('loans.json', 'w') as file:
            json.dump([loan.to_dict() for loan in library.borrows_list], file)









