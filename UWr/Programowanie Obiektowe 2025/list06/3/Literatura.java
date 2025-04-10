import java.io.*;
import java.util.*;

interface Obserwator extends Serializable {
    void powiadomienie(Ksiazka k);
    int getPriority();
}

abstract class AbstractObserver implements Obserwator {
    private static final long serialVersionUID = 1L;
    private final int priority;
    
    protected AbstractObserver(int priority) {
        this.priority = priority;
    }
    
    @Override
    public int getPriority() {
        return priority;
    }
}

class Ksiazka implements Serializable {
    private static final long serialVersionUID = 1L;
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
        return "\"" + tytul + "\" (" + gatunek + ", " + rokWydania + "), autorzy: " + autorzy;
    }
}

class Pisarz implements Serializable {
    private static final long serialVersionUID = 1L;
    String pseudonim;
    int rokUrodzenia;
    String narodowosc;
    List<Obserwator> obserwatorzy = new ArrayList<>();
    transient List<Ksiazka> ksiazki = new ArrayList<>(); // transient - nie serializujemy

    Pisarz(String pseudonim, int rokUrodzenia, String narodowosc) {
        this.pseudonim = pseudonim;
        this.rokUrodzenia = rokUrodzenia;
        this.narodowosc = narodowosc;
    }

    void dodajObserwatora(Obserwator o) {
        obserwatorzy.add(o);
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
            for (Obserwator o : autor.obserwatorzy) {
                o.powiadomienie(ksiazka);
            }
        }
    }

    @Override
    public String toString() {
        return pseudonim + " (ur. " + rokUrodzenia + ")";
    }
}

class Krytyk extends AbstractObserver {
    private static final long serialVersionUID = 1L;
    String imie;
    String specjalizacja;

    Krytyk(String imie, String specjalizacja) {
        super(1);
        this.imie = imie;
        this.specjalizacja = specjalizacja;
    }

    @Override
    public void powiadomienie(Ksiazka k) {
        System.out.println("[KRYTYK] " + imie + " (" + specjalizacja + ") recenzuje: " + k.tytul);
    }
}

class Czytelnik extends AbstractObserver {
    private static final long serialVersionUID = 1L;
    String imie;
    int wiek;
    String ulubionyGatunek;

    Czytelnik(String imie, int wiek, String ulubionyGatunek) {
        super(3);
        this.imie = imie;
        this.wiek = wiek;
        this.ulubionyGatunek = ulubionyGatunek;
    }

    @Override
    public void powiadomienie(Ksiazka k) {
        System.out.println("[CZYTELNIK] " + imie + " (lat " + wiek + ") - nowa książka: " + k.tytul);
    }
}

class Biblioteka extends AbstractObserver {
    private static final long serialVersionUID = 1L;
    String nazwa;
    int liczbaKsiazek;

    Biblioteka(String nazwa, int liczbaKsiazek) {
        super(2);
        this.nazwa = nazwa;
        this.liczbaKsiazek = liczbaKsiazek;
    }

    @Override
    public void powiadomienie(Ksiazka k) {
        liczbaKsiazek++;
        System.out.println("[BIBLIOTEKA] " + nazwa + " - nowa książka: " + k.tytul + " (łącznie: " + liczbaKsiazek + ")");
    }
}

class Wydawnictwo extends AbstractObserver {
    private static final long serialVersionUID = 1L;
    String nazwa;
    String kraj;
    int rokZalozenia;

    Wydawnictwo(String nazwa, String kraj, int rokZalozenia) {
        super(2);
        this.nazwa = nazwa;
        this.kraj = kraj;
        this.rokZalozenia = rokZalozenia;
    }

    @Override
    public void powiadomienie(Ksiazka k) {
        System.out.println("[WYDAWNICTWO] " + nazwa + " (" + kraj + ") - propozycja wydania: " + k.tytul);
    }
}

public class Literatura {
    private static final String DATA_FILE = "literatura_data.ser";

    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        // Próba wczytania danych
        Map<String, Object> data = (Map<String, Object>) wczytajDane();

        List<Pisarz> pisarze;
        List<Ksiazka> ksiazki;
        List<Obserwator> obserwatorzy;

        if (data != null) {
            System.out.println("Wczytano dane z pliku");
            pisarze = (List<Pisarz>) data.get("pisarze");
            ksiazki = (List<Ksiazka>) data.get("ksiazki");
            obserwatorzy = (List<Obserwator>) data.get("obserwatorzy");
        } else {
            System.out.println("Tworzenie nowych danych...");
            
            // Tworzenie obserwatorów
            obserwatorzy = new ArrayList<>();
            obserwatorzy.add(new Krytyk("Jan Kowalski", "fantastyka"));
            obserwatorzy.add(new Czytelnik("Anna Nowak", 25, "fantastyka"));
            obserwatorzy.add(new Biblioteka("Biblioteka Miejska", 1000));
            obserwatorzy.add(new Wydawnictwo("Fantastyka Press", "Polska", 1980));

            // Tworzenie pisarzy
            pisarze = new ArrayList<>();
            Pisarz tolkien = new Pisarz("J.R.R. Tolkien", 1892, "brytyjska");
            Pisarz sapkowski = new Pisarz("Andrzej Sapkowski", 1948, "polska");
            pisarze.add(tolkien);
            pisarze.add(sapkowski);

            // Dodawanie obserwatorów
            tolkien.dodajObserwatora(obserwatorzy.get(0));
            tolkien.dodajObserwatora(obserwatorzy.get(1));
            sapkowski.dodajObserwatora(obserwatorzy.get(2));
            sapkowski.dodajObserwatora(obserwatorzy.get(3));

            // Tworzenie książek
            ksiazki = new ArrayList<>();
            Pisarz.napiszKsiazke("Władca Pierścieni", Collections.singletonList(tolkien), 1954, "fantastyka");
            Pisarz.napiszKsiazke("Wiedźmin", Collections.singletonList(sapkowski), 1990, "fantastyka");

            // Zapis danych
            Map<String, Object> newData = new HashMap<>();
            newData.put("pisarze", pisarze);
            newData.put("ksiazki", ksiazki);
            newData.put("obserwatorzy", obserwatorzy);
            zapiszDane(newData);
        }

        // Przykładowe użycie
        System.out.println("\nLista pisarzy:");
        pisarze.forEach(System.out::println);

        System.out.println("\nLista książek:");
        ksiazki.forEach(System.out::println);

        System.out.println("\nPrzykładowe powiadomienia:");
        pisarze.get(0).napisz("Hobbit", 1937, "fantastyka");
    }

    private static void zapiszDane(Map<String, Object> data) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(DATA_FILE))) {
            oos.writeObject(data);
            System.out.println("Zapisano dane do pliku " + DATA_FILE);
        } catch (IOException e) {
            System.err.println("Błąd zapisu danych: " + e.getMessage());
        }
    }

    private static Object wczytajDane() {
        File file = new File(DATA_FILE);
        if (!file.exists()) {
            return null;
        }

        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(DATA_FILE))) {
            return ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Błąd wczytywania danych: " + e.getMessage());
            return null;
        }
    }
}