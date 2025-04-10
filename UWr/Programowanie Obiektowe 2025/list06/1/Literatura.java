import java.util.ArrayList;
import java.util.List;

class Ksiazka {
    String tytul;
    List<Pisarz> autorzy;
    int rokWydania;  // dodane
    String gatunek;  // dodane

    Ksiazka(String tytul, List<Pisarz> autorzy, int rokWydania, String gatunek) {
        this.tytul = tytul;
        this.autorzy = autorzy;
        this.rokWydania = rokWydania;  // dodane
        this.gatunek = gatunek;        // dodane
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

interface Obserwator {
    void powiadomienie(Ksiazka k);
}

class Pisarz {
    String pseudonim;
    int rokUrodzenia;   // dodane
    String narodowosc;  // dodane
    List<Obserwator> obserwatorzy = new ArrayList<>();
    List<Ksiazka> ksiazki = new ArrayList<>();

    Pisarz(String pseudonim, int rokUrodzenia, String narodowosc) {  
        this.pseudonim = pseudonim;
        this.rokUrodzenia = rokUrodzenia;  // dodane
        this.narodowosc = narodowosc;       // dodane
    }

    void dodajObserwatora(Obserwator o) {
        obserwatorzy.add(o);
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
            for (Obserwator o : autor.obserwatorzy) {
                o.powiadomienie(ksiazka);
            }
        }
    }
}

class Czytelnik implements Obserwator {
    String imie;
    int wiek;               // dodane
    String ulubionyGatunek; // dodane

    Czytelnik(String imie, int wiek, String ulubionyGatunek) { 
        this.imie = imie;
        this.wiek = wiek;               // dodane
        this.ulubionyGatunek = ulubionyGatunek; // dodane
    }

    public void powiadomienie(Ksiazka k) {
        System.out.println(imie + " (lat " + wiek + ", lubi " + ulubionyGatunek + 
                         ") dowiedział się o nowej książce: " + k);
    }
}

class Biblioteka implements Obserwator {
    // DODANE: nowe pola
    String nazwa;           // dodane
    int liczbaKsiazek;      // dodane

    Biblioteka(String nazwa, int liczbaKsiazek) {  
        this.nazwa = nazwa;           // dodane
        this.liczbaKsiazek = liczbaKsiazek; // dodane
    }

    public void powiadomienie(Ksiazka k) {
        liczbaKsiazek++;  // dodane
        System.out.println(nazwa + " przyjmuje książkę: " + k + ". Teraz ma " + liczbaKsiazek + " książek.");
    }
}

class Wydawnictwo implements Obserwator {
    char nazwa;
    // DODANE: nowe pola
    String kraj;          // dodane
    int rokZalozenia;     // dodane

    Wydawnictwo(char nazwa, String kraj, int rokZalozenia) {  
        this.nazwa = nazwa;
        this.kraj = kraj;          // dodane
        this.rokZalozenia = rokZalozenia; // dodane
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

        Pisarz aho = new Pisarz("Aho", 1941, "amerykańska");
        Pisarz hopcroft = new Pisarz("Hopcroft", 1939, "amerykańska");
        Pisarz ullmann = new Pisarz("Ullmann", 1942, "amerykańska");

        aho.dodajObserwatora(wydawnictwoT);
        aho.dodajObserwatora(jan);
        hopcroft.dodajObserwatora(biblioteka);

        List<Pisarz> autorzy = List.of(aho, hopcroft, ullmann);
        Pisarz.napiszKsiazke("Teoria automatów", autorzy, 2001, "naukowa");
        
        Pisarz tolkien = new Pisarz("Tolkien", 1892, "brytyjska");
        tolkien.dodajObserwatora(wydawnictwoT);
        tolkien.dodajObserwatora(biblioteka);
        tolkien.napisz("Władca Pierścieni", 1954, "fantasy");
    }
}