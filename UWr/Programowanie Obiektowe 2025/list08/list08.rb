############################################
# gra_war_ruby: Prosta gra "Wojna" (War) 2-osobowa w Ruby
############################################

# Klasa Karta: implementuje wzorzec "multiton" aby nie tworzyć duplikatów kart
class Karta
  include Comparable

  RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, :J, :Q, :K, :A]
  SUITS = [:kier, :karo, :pik, :trefl]
  SUIT_SYMBOLS = { kier: "♡", karo: "♢", pik: "♠", trefl: "♣" }
  @@instances = {}

  attr_reader :rank, :suit

  # Ukrywamy .new, używamy Karta.instance(rank, suit)
  private_class_method :new

  def self.instance(rank, suit)
    key = [rank, suit]
    @@instances[key] ||= new(rank, suit)
  end

  def initialize(rank, suit)
    @rank = rank
    @suit = suit
  end

  # Porównanie wg siły kart (tylko ranga)
  def <=>(other)
    RANKS.index(rank) <=> RANKS.index(other.rank)
  end

  # Reprezentacja tekstowa, np. "A♠"
  def to_s
    "#{rank}#{SUIT_SYMBOLS[suit]}"
  end
end

# Klasa Talia: tworzy 52 karty, tasuje i rozdaje
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

  # Rozdaj po kolei po jednej karcie każdemu graczowi aż talia pusta
  def deal(players)
    while @cards.any?
      players.each do |p|
        break if @cards.empty?
        p.receive_cards([@cards.shift])
      end
    end
  end
end

# Interfejs gracza: wymagane metody:
#   - receive_cards(array_of_cards)
#   - play_card -> karta
#   - collect_cards(array_of_cards)
#   - has_cards? -> boolean
#   - nick

# Gracz konsolowy (człowiek)
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

# Gracz komputerowy (losowa strategia)
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

# Klasa Gra: implementuje prostą grę "Wojna"
class Gra
  def initialize(players)
    @players = players
  end

  def play
    talia = Talia.new
    talia.shuffle!
    talia.deal(@players)

    round = 0
    until @players.any? { |p| !p.has_cards? }
      round += 1
      puts "\n=== Runda #{round} ==="
      table = []

      # Każdy gracz zagrywa kartę
      plays = @players.map { |p| [p, p.play_card] }
      table.concat plays.map { |_, card| card }

      # Porównanie kart
      best = plays.max_by { |_, card| card }
      winners = plays.select { |_, card| card == best[1] }.map(&:first)

      if winners.size > 1
        puts "Remis tej rundy pomiędzy: #{winners.map(&:nick).join(', ')}"
        # W razie remisu zwracamy karty graczom
        plays.each { |p, card| p.collect_cards([card]) }
      else
        winner = best[0]
        puts "Wygrywa rundę: #{winner.nick}"
        winner.collect_cards(table)
      end
    end

    # Ogłoszenie zwycięzcy: gracz, który ma karty
    victor = @players.find(&:has_cards?)
    puts "\nKoniec gry! Zwycięzca: #{victor.nick}" if victor
  end
end

# Przykładowe uruchomienie: człowiek vs komputer
if __FILE__ == $0
  puts "Podaj swój nick:"
  nickname = gets.chomp
  human = HumanPlayer.new(nickname)
  computer = ComputerPlayer.new("Komputer")
  gra = Gra.new([human, computer])
  gra.play
end
