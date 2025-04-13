/*import java.util.ArrayList;
import java.util.List;
import java.util.Collections;
import java.util.Comparator;

// Rozszerzony interfejs Obserwator o priorytet
interface Obserwator {
    void powiadomienie(Ksiazka k);
    int getPriority(); // Nowa metoda określająca kolejność powiadomień
}

// Abstrakcyjna klasa bazowa dla obserwatorów
abstract class AbstractObserver implements Obserwator {
    private final int priority;
    
    protected AbstractObserver(int priority) {
        this.priority = priority;
    }
    
    @Override
    public int getPriority() {
        return priority;
    }
}

class Ksiazka {
    String tytul;
    List<Pisarz> autorzy;
    int rokWydania;
    String gatunek;

    Ksiazka(String tytul, List<Pisarz> autorzy, int rokWydania, String gatunek) {
        this.tytul = tytul;
        this.autorzy = autorzy;
        this.rokWydania = rokWydania;
        this.gatunek = gatunek;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Ksiazka: " + tytul + " (" + gatunek + ", " + rokWydania + ") autorstwa: ");
        for (Pisarz autor : autorzy) {
            sb.append(autor.pseudonim).append(", ");
        }
        if (autorzy.size() > 0) {
            sb.setLength(sb.length() - 2);
        }
        return sb.toString();
    }
}

class Pisarz {
    String pseudonim;
    int rokUrodzenia;
    String narodowosc;
    List<Obserwator> obserwatorzy = new ArrayList<>();
    List<Ksiazka> ksiazki = new ArrayList<>();

    Pisarz(String pseudonim, int rokUrodzenia, String narodowosc) {
        this.pseudonim = pseudonim;
        this.rokUrodzenia = rokUrodzenia;
        this.narodowosc = narodowosc;
    }

    void dodajObserwatora(Obserwator o) {
        obserwatorzy.add(o);
        // Sortowanie obserwatorów według priorytetu
        Collections.sort(obserwatorzy, Comparator.comparingInt(Obserwator::getPriority));
    }

    void usunObserwatora(Obserwator o) {
        obserwatorzy.remove(o);
    }

    void napisz(String tytul, int rokWydania, String gatunek) {
        List<Pisarz> autorzy = new ArrayList<>();
        autorzy.add(this);
        napiszKsiazke(tytul, autorzy, rokWydania, gatunek);
    }

    static void napiszKsiazke(String tytul, List<Pisarz> autorzy, int rokWydania, String gatunek) {
        Ksiazka ksiazka = new Ksiazka(tytul, autorzy, rokWydania, gatunek);
        for (Pisarz autor : autorzy) {
            autor.ksiazki.add(ksiazka);
            // Powiadamianie obserwatorów w określonej kolejności
            for (Obserwator o : autor.obserwatorzy) {
                o.powiadomienie(ksiazka);
            }
        }
    }
}

// Nowa klasa Krytyk z najwyższym priorytetem
class Krytyk extends AbstractObserver {
    String imie;
    String specjalizacja; // Nowe pole

    Krytyk(String imie, String specjalizacja) {
        super(1); // Najwyższy priorytet
        this.imie = imie;
        this.specjalizacja = specjalizacja;
    }

    @Override
    public void powiadomienie(Ksiazka k) {
        System.out.println("Krytyk " + imie + " (" + specjalizacja + ") recenzuje książkę: " + k);
    }
}

class Czytelnik extends AbstractObserver {
    String imie;
    int wiek;
    String ulubionyGatunek;

    Czytelnik(String imie, int wiek, String ulubionyGatunek) {
        super(3); // Najniższy priorytet
        this.imie = imie;
        this.wiek = wiek;
        this.ulubionyGatunek = ulubionyGatunek;
    }

    public void powiadomienie(Ksiazka k) {
        System.out.println(imie + " (lat " + wiek + ", lubi " + ulubionyGatunek + 
                         ") dowiedział się o nowej książce: " + k);
    }
}

class Biblioteka extends AbstractObserver {
    String nazwa;
    int liczbaKsiazek;

    Biblioteka(String nazwa, int liczbaKsiazek) {
        super(2); // Średni priorytet
        this.nazwa = nazwa;
        this.liczbaKsiazek = liczbaKsiazek;
    }

    public void powiadomienie(Ksiazka k) {
        liczbaKsiazek++;
        System.out.println(nazwa + " przyjmuje książkę: " + k + ". Teraz ma " + liczbaKsiazek + " książek.");
    }
}

class Wydawnictwo extends AbstractObserver {
    char nazwa;
    String kraj;
    int rokZalozenia;

    Wydawnictwo(char nazwa, String kraj, int rokZalozenia) {
        super(2); // Ten sam priorytet co Biblioteka
        this.nazwa = nazwa;
        this.kraj = kraj;
        this.rokZalozenia = rokZalozenia;
    }

    void wydajKsiazke(Ksiazka ksiazka) {
        System.out.println("Wydawnictwo '" + nazwa + "' (" + kraj + ", zał. " + rokZalozenia + 
                         ") wydaje książkę: " + ksiazka);
    }

    public void powiadomienie(Ksiazka ksiazka) {
        if (ksiazka.tytul.charAt(0) == this.nazwa) {
            wydajKsiazke(ksiazka);
        }
    }
}

public class Literatura {
    public static void main(String[] args) {
        Wydawnictwo wydawnictwoT = new Wydawnictwo('T', "Polska", 1990);
        Czytelnik jan = new Czytelnik("Jan", 35, "fantastyka");
        Biblioteka biblioteka = new Biblioteka("Biblioteka Narodowa", 10000);
        Krytyk krytyk = new Krytyk("Adam Nowak", "literatura fantasy"); // Nowy obserwator

        Pisarz aho = new Pisarz("Aho", 1941, "amerykańska");
        Pisarz hopcroft = new Pisarz("Hopcroft", 1939, "amerykańska");
        Pisarz ullmann = new Pisarz("Ullmann", 1942, "amerykańska");

        // Dodawanie obserwatorów w dowolnej kolejności
        aho.dodajObserwatora(jan);
        aho.dodajObserwatora(wydawnictwoT);
        aho.dodajObserwatora(biblioteka);
        aho.dodajObserwatora(krytyk); // Dodanie krytyka

        List<Pisarz> autorzy = List.of(aho, hopcroft, ullmann);
        
        // Powiadomienia będą w kolejności: Krytyk, Biblioteka, Wydawnictwo, Czytelnik
        Pisarz.napiszKsiazke("Teoria automatów", autorzy, 2001, "naukowa");
        
        Pisarz tolkien = new Pisarz("Tolkien", 1892, "brytyjska");
        tolkien.dodajObserwatora(wydawnictwoT);
        tolkien.dodajObserwatora(biblioteka);
        tolkien.dodajObserwatora(new Krytyk("Anna Kowalska", "literatura klasyczna"));
        
        // Ponownie powiadomienia w określonej kolejności
        tolkien.napisz("Władca Pierścieni", 1954, "fantasy");
    }
}*/