class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

root = TreeItem(10)
root.left = TreeItem(5)
root.right = TreeItem(15)
root.left.left = TreeItem(7)
root.left.right = TreeItem(3)
root.left.right.right = TreeItem(8)
root.right.right = TreeItem(20)

def zlicz(t):
    if t is None:
        return 0
    return 1 + zlicz(t.left) + zlicz(t.right)

def wysokosc(t):
    if t is None:
        return 0

    prawe = wysokosc(t.right)
    lewe = wysokosc(t.left)

    if prawe > lewe:
        return 1 + prawe
    else:
        return 1 + lewe

def wypisz_dodatnie(t):
    if t is None:
        return

    # Przechodzimy do lewego poddrzewa
    wypisz_dodatnie(t.left)

    # Wypisujemy tylko dodatnie wartości
    if t.val > 0:
        print(t.val)

    # Przechodzimy do prawego poddrzewa
    wypisz_dodatnie(t.right)

def is_bst(t, low, high):
    # Jeśli węzeł jest pusty, to jest to drzewo BST (pusty węzeł jest zawsze zgodny z warunkami)
    if t is None:
        return True

    # Sprawdzamy, czy wartość węzła mieści się w dozwolonym zakresie
    if t.val <= low or t.val >= high:
        return False

    # Rekurencyjnie sprawdzamy lewe i prawe poddrzewo
    return (is_bst(t.left, low, t.val) and  # Lewa strona: wartości muszą być mniejsze niż t.val
            is_bst(t.right, t.val, high))  # Prawa strona: wartości muszą być większe niż t.val


def rotate_left(u):
    """
    Wykonaj rotację w lewo wokół węzła u, zakładając, że u ma lewe dziecko v.
    """
    v = u.left

    if v is None:
        return u  # Jeśli nie ma lewego dziecka, nie wykonujemy rotacji

    # Przypadek, gdy v ma prawe dziecko
    u.left = v.right
    v.right = u

    return v

t = rotate_left(root.left.left)
print(is_bst(t, -10**6, 10**6))