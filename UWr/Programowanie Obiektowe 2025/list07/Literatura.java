import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;
import java.util.List;

public class Literatura {

    public static class Ksiazka implements Serializable {
        String tytul;
        String autor;
        int rok;

        public Ksiazka(String tytul, String autor, int rok) {
            this.tytul = tytul;
            this.autor = autor;
            this.rok = rok;
        }

        public String toString() {
            return tytul + " (" + autor + ", " + rok + ")";
        }
    }

    public static class Pisarz implements Serializable {
        String imie;
        String nazwisko;
        int wiek;

        public Pisarz(String imie, String nazwisko, int wiek) {
            this.imie = imie;
            this.nazwisko = nazwisko;
            this.wiek = wiek;
        }

        public String toString() {
            return imie + " " + nazwisko + " (" + wiek + " lat)";
        }
    }

    public static class Wydawnictwo implements Serializable {
        String nazwa;
        String miasto;

        public Wydawnictwo(String nazwa, String miasto) {
            this.nazwa = nazwa;
            this.miasto = miasto;
        }

        public String toString() {
            return nazwa + " (" + miasto + ")";
        }
    }

    static class KsiazkaEditor extends JPanel {
        JTextField tytulField = new JTextField(20);
        JTextField autorField = new JTextField(20);
        JTextField rokField = new JTextField(5);

        public KsiazkaEditor() {
            setLayout(new GridLayout(3, 2));
            add(new JLabel("Tytuł:"));
            add(tytulField);
            add(new JLabel("Autor:"));
            add(autorField);
            add(new JLabel("Rok:"));
            add(rokField);
        }

        public void load(Ksiazka k) {
            tytulField.setText(k.tytul);
            autorField.setText(k.autor);
            rokField.setText(String.valueOf(k.rok));
        }

        public void save(Ksiazka k) {
            k.tytul = tytulField.getText();
            k.autor = autorField.getText();
            k.rok = Integer.parseInt(rokField.getText());
        }
    }

    static class PisarzEditor extends JPanel {
        JTextField imieField = new JTextField(20);
        JTextField nazwiskoField = new JTextField(20);
        JTextField wiekField = new JTextField(5);

        public PisarzEditor() {
            setLayout(new GridLayout(3, 2));
            add(new JLabel("Imię:"));
            add(imieField);
            add(new JLabel("Nazwisko:"));
            add(nazwiskoField);
            add(new JLabel("Wiek:"));
            add(wiekField);
        }

        public void load(Pisarz p) {
            imieField.setText(p.imie);
            nazwiskoField.setText(p.nazwisko);
            wiekField.setText(String.valueOf(p.wiek));
        }

        public void save(Pisarz p) {
            p.imie = imieField.getText();
            p.nazwisko = nazwiskoField.getText();
            p.wiek = Integer.parseInt(wiekField.getText());
        }
    }

    static class WydawnictwoEditor extends JPanel {
        JTextField nazwaField = new JTextField(20);
        JTextField miastoField = new JTextField(20);

        public WydawnictwoEditor() {
            setLayout(new GridLayout(2, 2));
            add(new JLabel("Nazwa:"));
            add(nazwaField);
            add(new JLabel("Miasto:"));
            add(miastoField);
        }

        public void load(Wydawnictwo w) {
            nazwaField.setText(w.nazwa);
            miastoField.setText(w.miasto);
        }

        public void save(Wydawnictwo w) {
            w.nazwa = nazwaField.getText();
            w.miasto = miastoField.getText();
        }
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Podaj nazwę klasy do edycji: Ksiazka, Pisarz lub Wydawnictwo");
            return;
        }

        String typ = args[0];
        String filename = "literatura_" + typ + ".ser";

        SwingUtilities.invokeLater(() -> {
            try {
                List<Object> obiekty;
                File file = new File(filename);
                if (file.exists()) {
                    ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file));
                    obiekty = (List<Object>) ois.readObject();
                    ois.close();
                } else {
                    obiekty = new ArrayList<>();
                    if (typ.equals("Ksiazka")) {
                        obiekty.add(new Ksiazka("Lalka", "Prus", 1890));
                        obiekty.add(new Ksiazka("Quo Vadis", "Sienkiewicz", 1896));
                    } else if (typ.equals("Pisarz")) {
                        obiekty.add(new Pisarz("Adam", "Mickiewicz", 56));
                        obiekty.add(new Pisarz("Juliusz", "Słowacki", 40));
                    } else if (typ.equals("Wydawnictwo")) {
                        obiekty.add(new Wydawnictwo("PWN", "Warszawa"));
                        obiekty.add(new Wydawnictwo("Znak", "Kraków"));
                    }
                }

                JFrame frame = new JFrame("Edycja " + typ);
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setSize(400, 300);
                frame.setLayout(new BorderLayout());

                JComboBox<Object> combo = new JComboBox<>(obiekty.toArray());
                frame.add(combo, BorderLayout.NORTH);

                JPanel editorPanel = new JPanel();
                frame.add(editorPanel, BorderLayout.CENTER);

                JButton saveButton = new JButton("Zapisz");
                frame.add(saveButton, BorderLayout.SOUTH);

                Runnable[] updater = new Runnable[1];

                combo.addActionListener(e -> {
                    Object selected = combo.getSelectedItem();
                    editorPanel.removeAll();
                    if (typ.equals("Ksiazka")) {
                        KsiazkaEditor editor = new KsiazkaEditor();
                        editor.load((Ksiazka) selected);
                        editorPanel.add(editor);
                        updater[0] = () -> editor.save((Ksiazka) selected);
                    } else if (typ.equals("Pisarz")) {
                        PisarzEditor editor = new PisarzEditor();
                        editor.load((Pisarz) selected);
                        editorPanel.add(editor);
                        updater[0] = () -> editor.save((Pisarz) selected);
                    } else if (typ.equals("Wydawnictwo")) {
                        WydawnictwoEditor editor = new WydawnictwoEditor();
                        editor.load((Wydawnictwo) selected);
                        editorPanel.add(editor);
                        updater[0] = () -> editor.save((Wydawnictwo) selected);
                    }
                    editorPanel.revalidate();
                    editorPanel.repaint();
                });

                combo.setSelectedIndex(0);

                saveButton.addActionListener(e -> {
                    if (updater[0] != null) updater[0].run();
                    try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
                        oos.writeObject(obiekty);
                        JOptionPane.showMessageDialog(frame, "Zapisano pomyślnie!");
                    } catch (IOException ex) {
                        ex.printStackTrace();
                        JOptionPane.showMessageDialog(frame, "Błąd zapisu.");
                    }
                });

                frame.setVisible(true);

            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }
}
