Celem projektu jest stworzenie prostego, modularnego systemu do zarządzania biblioteką, który umożliwia:

-   przechowywanie informacji o książkach i użytkownikach,
-   zarządzanie wypożyczeniami oraz rezerwacjami książek,
-   rozróżnienie ról użytkowników (czytelnik, bibliotekarz),
-   trwałe zapisywanie i wczytywanie danych z pliku.

📘 Book
Reprezentuje książkę w bibliotece.

 -   Atrybuty: tytuł, autor, identyfikator, liczba egzemplarzy, dostępność.
    
  -  Obsługuje wypożyczanie i zwracanie egzemplarzy.
    
   - Metody pomocnicze: to_dict, from_dict, __str__.

👤 User (klasa bazowa)
    Bazowa klasa użytkownika biblioteki.
    
  -  Atrybuty: imię, identyfikator, lista wypożyczonych książek.
    
  -  Metody do wypożyczania i zwracania książek.
    
  -  Obsługuje serializację (to_dict / from_dict).

📖 Reader (dziedziczy po User)
   - Reprezentuje zwykłego czytelnika.
    
   - Dodatkowo przechowuje historię rezerwacji.
    
   - Może rezerwować książki i przeglądać historię.

🧑‍🏫 Librarian (dziedziczy po User)
  -  Reprezentuje pracownika biblioteki.
    
   - Może dodawać/usuwać książki i użytkowników.
    
   - Ma dostęp do wszystkich funkcji administracyjnych.

📅 Loan
  -  Reprezentuje pojedyncze wypożyczenie książki.
    
   - Dane: użytkownik, tytuł książki, data wypożyczenia, planowana i faktyczna data zwrotu.
    
   - Oblicza czy książka jest przetrzymana i nalicza karę.

🔒 Reservation
  -  Reprezentuje rezerwację książki.
    
   - Przechowuje książkę, użytkownika, datę zwrotu, status aktywności.
    
   - Pozwala anulować rezerwację lub sprawdzić jej ważność.

🏛️ Library
  -  Zbiorczy moduł zarządzający całą biblioteką.

   - Przechowuje listę książek, użytkowników, wypożyczeń i rezerwacji.
    
    
   - Umożliwia wyszukiwanie po ID.

💾 FileManager
  -  Obsługuje zapis i odczyt danych biblioteki do/z pliku JSON.
    
   - Serializuje i deserializuje obiekty Library, Book, User itd.