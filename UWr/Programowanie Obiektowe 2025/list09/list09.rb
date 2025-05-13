# Mixin do zapisu i odczytu obiektów
module Persistable
  def zapisz_do_pliku(nazwa)
    File.open(nazwa, "wb") { |f| Marshal.dump(self, f) }
  end

  def self.wczytaj_z_pliku(nazwa)
    File.open(nazwa, "rb") { |f| Marshal.load(f) }
  end
end

# Klasa Karta: implementuje wzorzec "multiton"
class Karta
  include Comparable

  RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, :J, :Q, :K, :A]
  SUITS = [:kier, :karo, :pik, :trefl]
  SUIT_SYMBOLS = { kier: "♡", karo: "♢", pik: "♠", trefl: "♣" }
  @@instances = {}

  attr_reader :rank, :suit

  private_class_method :new

  def self.instance(rank, suit)
    key = [rank, suit]
    @@instances[key] ||= new(rank, suit)
  end

  def initialize(rank, suit)
    @rank = rank
    @suit = suit
  end

  def <=>(other)
    RANKS.index(rank) <=> RANKS.index(other.rank)
  end

  def to_s
    "#{rank}#{SUIT_SYMBOLS[suit]}"
  end
end

# Klasa Talia
class Talia
  def initialize
    @cards = []
    Karta::RANKS.each do |r|
      Karta::SUITS.each do |s|
        @cards << Karta.instance(r, s)
      end
    end
  end

  def shuffle!
    @cards.shuffle!
  end

  def deal(players)
    while @cards.any?
      players.each do |p|
        break if @cards.empty?
        p.receive_cards([@cards.shift])
      end
    end
  end
end

# Gracz konsolowy
class HumanPlayer
  attr_reader :nick

  def initialize(nick)
    @nick = nick
    @hand = []
  end

  def receive_cards(cards)
    @hand.concat(cards)
  end

  def play_card
    puts "\n#{nick}, Twoje karty:"
    @hand.each_with_index { |c, i| puts "  [#{i}] #{c}" }
    idx = nil
    loop do
      print "Wybierz indeks karty do zagrania: "
      idx = gets.chomp.to_i
      break if idx >= 0 && idx < @hand.size
      puts "Nieprawidłowy indeks, spróbuj ponownie."
    end
    @hand.delete_at(idx)
  end

  def collect_cards(cards)
    @hand.concat(cards)
  end

  def has_cards?
    !@hand.empty?
  end
end

# Gracz komputerowy
class ComputerPlayer
  attr_reader :nick

  def initialize(nick)
    @nick = nick
    @hand = []
  end

  def receive_cards(cards)
    @hand.concat(cards)
  end

  def play_card
    card = @hand.delete_at(rand(@hand.size))
    puts "#{nick} zagrał #{card}"
    card
  end

  def collect_cards(cards)
    @hand.concat(cards)
  end

  def has_cards?
    !@hand.empty?
  end
end

# Klasa Gra
class Gra
  include Persistable

  def initialize(players)
    @players = players
  end

  def play
    if @players.any? { |p| p.respond_to?(:receive_cards) && p.instance_variable_get(:@hand).empty? }
      talia = Talia.new
      talia.shuffle!
      talia.deal(@players)
    end

    round = 0
    while @players.all?(&:has_cards?)
      round += 1
      puts "\n=== Runda #{round} ==="
      table = []

      plays = @players.map { |p| [p, p.play_card] }
      table.concat plays.map { |_, card| card }

      best = plays.max_by { |_, card| card }
      winners = plays.select { |_, card| card == best[1] }.map(&:first)

      if winners.size > 1
        puts "Remis tej rundy pomiędzy: #{winners.map(&:nick).join(', ')}"
        plays.each { |p, card| p.collect_cards([card]) }
      else
        winner = best[0]
        puts "Wygrywa rundę: #{winner.nick}"
        winner.collect_cards(table)
      end

      puts "\nCzy chcesz kontynuować grę? (t/n) Możesz też wpisać 'zapisz' aby zapisać i wyjść:"
      choice = gets.chomp.downcase
      if choice == "zapisz"
        zapisz_do_pliku("save.dat")
        puts "Gra została zapisana do pliku 'save.dat'."
        return
      elsif choice == "n"
        puts "Gra została przerwana bez zapisu."
        return
      end
    end

    victor = @players.find(&:has_cards?)
    puts "\nKoniec gry! Zwycięzca: #{victor.nick}" if victor
  end
end

# Uruchomienie
if __FILE__ == $0
  if File.exist?("save.dat")
    puts "Wczytać zapisaną grę? (t/n):"
    if gets.chomp.downcase == "t"
      gra = Persistable.wczytaj_z_pliku("save.dat")
      puts "Gra została wczytana."
      gra.play
      exit
    end
  end

  puts "Nowa gra. Podaj swój nick:"
  nickname = gets.chomp
  human = HumanPlayer.new(nickname)
  computer = ComputerPlayer.new("Komputer")
  gra = Gra.new([human, computer])
  gra.play
end
