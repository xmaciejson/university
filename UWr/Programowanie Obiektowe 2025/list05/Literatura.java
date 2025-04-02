import java.util.ArrayList;
import java.util.List;

class Ksiazka {
    String tytul;
    List<Pisarz> autorzy; // (D) - przechowywanie wielu autorów

    Ksiazka(String tytul, List<Pisarz> autorzy) { // (D) - konstruktor dla wielu autorów
        this.tytul = tytul;
        this.autorzy = autorzy;
    }

    @Override
    // (A) - implementacja toString()
    public String toString() {
        StringBuilder sb = new StringBuilder("Ksiazka: " + tytul + " autorstwa: ");
        for (Pisarz autor : autorzy) {
            sb.append(autor.pseudonim).append(", ");
        }
        if (autorzy.size() > 0) {
            sb.setLength(sb.length() - 2);
        }
        return sb.toString();
    }
}

interface Obserwator {
    void powiadomienie(Ksiazka k);
}

class Pisarz {
    String pseudonim;
    // (B) - lista wielu obserwatorów
    List<Obserwator> obserwatorzy = new ArrayList<>(); 
    List<Ksiazka> ksiazki = new ArrayList<>();

    Pisarz(String pseudonim) {
        this.pseudonim = pseudonim;
    }

    // (B) - metody dodawania/usuwnia obserwatorów
    void dodajObserwatora(Obserwator o) {
        obserwatorzy.add(o);
    }

    void usunObserwatora(Obserwator o) {
        obserwatorzy.remove(o);
    }

    void napisz(String tytul) {
        List<Pisarz> autorzy = new ArrayList<>();
        autorzy.add(this);
        napiszKsiazke(tytul, autorzy);
    }

    // (D) - metoda dla wielu autorów
    static void napiszKsiazke(String tytul, List<Pisarz> autorzy) {
        Ksiazka ksiazka = new Ksiazka(tytul, autorzy);
        for (Pisarz autor : autorzy) {
            autor.ksiazki.add(ksiazka);
            // (B) - powiadamianie wszystkich obserwatorów
            for (Obserwator o : autor.obserwatorzy) {
                o.powiadomienie(ksiazka);
            }
        }
    }
}

// (C) - pierwsza implementacja Obserwatora (oprócz Wydawnictwa)
class Czytelnik implements Obserwator {
    String imie;

    Czytelnik(String imie) {
        this.imie = imie;
    }

    public void powiadomienie(Ksiazka k) {
        System.out.println(imie + " dowiedział się o nowej książce: " + k);
    }
}

// (C) - druga implementacja Obserwatora
class Biblioteka implements Obserwator {
    public void powiadomienie(Ksiazka k) {
        System.out.println("Biblioteka przyjmuje książkę: " + k);
    }
}

class Wydawnictwo implements Obserwator {
    char nazwa;

    Wydawnictwo(char nazwa) {
        this.nazwa = nazwa;
    }

    void wydajKsiazke(Ksiazka ksiazka) {
        System.out.println("Wydaje książkę: " + ksiazka);
    }

    public void powiadomienie(Ksiazka ksiazka) {
        if (ksiazka.tytul.charAt(0) == this.nazwa) {
            wydajKsiazke(ksiazka);
        }
    }
}

public class Literatura {
    public static void main(String[] args) {
        // Przykładowe użycie wszystkich funkcjonalności
        Wydawnictwo wydawnictwoT = new Wydawnictwo('T');
        // (C) - tworzenie obserwatorów
        Czytelnik jan = new Czytelnik("Jan"); 
        Biblioteka biblioteka = new Biblioteka();

        Pisarz aho = new Pisarz("Aho");
        Pisarz hopcroft = new Pisarz("Hopcroft");
        Pisarz ullmann = new Pisarz("Ullmann");

        // (B) - dodawanie wielu obserwatorów
        aho.dodajObserwatora(wydawnictwoT);
        aho.dodajObserwatora(jan);
        hopcroft.dodajObserwatora(biblioteka);

        // (D) - tworzenie książki przez wielu autorów
        List<Pisarz> autorzy = List.of(aho, hopcroft, ullmann);
        Pisarz.napiszKsiazke("AiSD", autorzy);
    }
}