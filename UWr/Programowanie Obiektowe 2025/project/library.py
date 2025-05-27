from datetime import date, datetime, timedelta
import json
import os

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
        return f'{self.title} autorstwa {self.author} - {self.available_copies}/{self.total_copies} dostępnych kopii.'

class User:

    def __init__(self, name: str, user_id: int, borrowed_books: list = None):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def to_dict(self):
        return {
            'type': 'User',
            'name': self.name,
            'user_id': self.user_id,
            'borrowed_books': [book.book_id for book in self.borrowed_books],
        }

    @staticmethod
    def from_dict(data: dict):
        user = User(
            name=data['name'],
            user_id=data['user_id'],
            borrowed_books=[])
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
    def __init__(self, name: str, user_id: int, borrowed_books: list = None, reservation_history: list = None):
        super().__init__(name=name, user_id=user_id, borrowed_books=borrowed_books)
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
    def __init__(self, name: str, user_id: int, borrowed_books: list = None):
        super().__init__(name=name, user_id=user_id, borrowed_books=borrowed_books)

    def to_dict(self):
        data = super().to_dict()
        data['type'] = 'Librarian'
        return data

    @staticmethod
    def from_dict(data: dict):
        librarian = Librarian(
            name=data['name'],
            user_id=data['user_id'],
            borrowed_books=[]
        )
        return librarian

    def add_book(self, book, library) -> None :
        library.add_book(book)

    def remove_book(self, book, library) -> None:
        library.remove_book(book)

    def create_user(self, library, user) -> None:
        library.add_user(user)

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

    def get_book_by_id(self, book_id: int):
        return next((book for book in self.books if book.book_id == book_id), None)

    def get_user_by_id(self, user_id: int):
        return next((user for user in self.users if user.user_id == user_id), None)


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

    @staticmethod
    def load_library():
        library = Library()
        if os.path.exists('books.json'):
            with open('books.json', 'r', encoding='utf-8') as file:
                for data in json.load(file):
                    book = Book.from_dict(data)
                    library.add_book(book)

        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                for data in json.load(file):
                    user_type = data.get('type')
                    if user_type == 'Reader':
                        user = Reader.from_dict(data)
                    elif user_type == 'Librarian':
                        user = Librarian.from_dict(data)
                    else:
                        continue
                    library.add_user(user)

        if os.path.exists('reservations.json'):
            with open('reservations.json', 'r', encoding='utf-8') as file:
                for data in json.load(file):
                    book = library.get_book_by_id(data['book_id'])
                    user = library.get_user_by_id(data['user_id'])
                    if book and user:
                        reservation = Reservation(book, user, data['return_date'])
                        library.add_reservation(reservation)

        if os.path.exists('loans.json'):
            with open('loans.json', 'r', encoding='utf-8') as file:
                for data in json.load(file):
                    book = library.get_book_by_id(data['book_id'])
                    user = library.get_user_by_id(data['user_id'])
                    if book and isinstance(user, Reader):
                        user.borrowed_books.append(book)
                        library.borrows_list.append(Loan(book, user, data['return_date']))

        return library


def main():
    library = Library()

    while True:
        print("\n===== MENU BIBLIOTEKI =====")
        print("1. Dodaj książkę")
        print("2. Usuń książkę")
        print("3. Pokaż wszystkie książki")
        print("4. Dodaj użytkownika")
        print("5. Usuń użytkownika")
        print("6. Pokaż wszystkich użytkowników")
        print("7. Wypożycz książkę")
        print("8. Zwróć książkę")
        print("9. Zarezerwuj książkę")
        print("10. Usuń rezerwację")
        print("11. Sprawdź czy rezerwacja jest po terminie")
        print("12. Sprawdź opłatę za przetrzymanie")
        print("S. Zapisz dane do plików")
        print("X. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            title = input("Tytuł: ")
            author = input("Autor: ")
            total_copies = int(input("Liczba egzemplarzy: "))
            book_id = int(input("ID książki: "))
            book = Book(title, author, total_copies, book_id)
            library.add_book(book)
            print("Dodano książkę.")

        elif choice == '2':
            book_id = int(input("ID książki: "))
            book_to_remove = None
            for b in library.books:
                if b.book_id == book_id:
                    book_to_remove = b
                    break
            if book_to_remove:
                library.remove_book(book_to_remove)
                print("Usunięto książkę!")
            else:
                print("Nie znaleziono książki!")

        elif choice == '3':
            if not library.books:
                print('Brak książek!')
            for book in library.books:
                print(book)

        elif choice == '4':
            name = input('Imię użytkownika: ')
            user_id = int(input('ID użytkownika: '))
            user_type = input('Typ użytkownika (reader/librarian): ').lower()
            if user_type == 'reader':
                user = Reader(name, user_id)
            else:
                user = Librarian(name, user_id)
            library.users.append(user)
            print('Dodano użytkownika!')

        elif choice == '5':
            user_id = int(input("Podaj ID użytkownika: "))
            user_to_remove = None
            for u in library.users:
                if u.user_id == user_id:
                    user_to_remove = u
                    break
            if user_to_remove:
                library.remove_user(user_to_remove)
                print("Usunięto użytkownika!")
            else:
                print("Nie znaleziono użytkownika")

        elif choice == '6':
            if not library.users:
                print("Brak użytkowników!")
            else:
                for user in library.users:
                    print(user)

        elif choice == '7':
            user_id = int(input('ID użytkownika: '))
            book_id = int(input("ID książki: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.book_id == book_id), None)
            if user and book:
                if user.borrow_book(book):
                    today = date.today()
                    return_date = (today + timedelta(days=14)).strftime('%d-%m-%Y')
                    loan = Loan(
                        user_id=user.user_id,
                        book=book.title,
                        reservation_date=today.strftime('%d-%m-%Y'),
                        return_date=return_date,
                        actual_return_date=""  # jeszcze nie zwrócono
                    )
                    library.add_loan(loan)
                    print('Wypożyczono książkę!')
                else:
                    print('Brak dostępnych egzemplarzy')
            else:
                print('Nie znaleziono książki lub użytkownika!')


        elif choice == '8':
            user_id = int(input('ID użytkownika: '))
            book_id = int(input("ID książki: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.book_id == book_id), None)
            if user and book:
                if user.return_book(book):
                    print('Zwrot przyjęty!')
                else:
                    print('Podany użytkownik nie ma tej książki!')
            else:
                print('Nie znaleziono książki lub użytkownika!')

        elif choice == '9':
            user_id = int(input('ID użytkownika: '))
            book_id = int(input("ID książki: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.book_id == book_id), None)
            if user and book:
                if user.reserve_book(book):
                    r_dt = (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y')
                    reservation = Reservation(book, user, return_date=r_dt)
                    library.add_reservation(reservation)
                    print('Zarezerwowano książkę!')
                else:
                    print('Nie można zarezerwować!')
            else:
                print('Nie znaleziono książki lub użytkownika!')

        elif choice == '10':
            user_id = int(input('ID użytkownika: '))
            book_id = int(input("ID książki: "))
            reservation_to_remove = None
            for res in library.reservations:
                if res.user.user_id == user_id and res.book.book_id == book_id and res.active:
                    reservation_to_remove = res
                    break
            if reservation_to_remove:
                library.remove_reservation(reservation_to_remove)
                print('Rezerwacja usunięta!')
            else:
                print('Nie znaleziono rezerwacji!')

        elif choice == '11':
            user_id = int(input('ID użytkownika: '))
            book_title = input("Tytuł książki: ")
            found = False
            for loan in library.borrows_list:
                if loan.user_id == user_id and loan.book_title == book_title:
                    if loan.is_overdue():
                        roznica = (datetime.today() - loan.return_date).days
                        print(f'Wypożyczenie jest po terminie o {roznica} dni!')
                        found = True
                        break
                    else:
                        print('Wypożyczenie jest w terminie!')
                        break
            if not found:
                print('Nie znaleziono wypożyczenia!')

        elif choice == '12':
            user_id = int(input('ID użytkownika: '))
            book_title = input('Tytuł książki: ')
            found = False
            for loan in library.borrows_list:
                if loan.user_id == user_id and loan.book == book_title:
                    cost = loan.overdue_cost()
                    print(f'Opłata za przetrzymanie: {cost} zł')
                    found = True
                    break
            if not found:
                print('Nie znaleziono wypożyczenia!')


        elif choice == 'S':
            FileManager.save_library(library)
            print('Dane zapisane do plików!')

        elif choice == 'X':
            print('Do zobaczenia!')
            break

        else:
            print('Nieznana opcja!')

main()