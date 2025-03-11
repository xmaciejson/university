

class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

l = ListItem(10)
l.next = ListItem(20)
l.next.next = ListItem(20)

def dolacz(lista, value):
    nowy = ListItem(value)
    if lista is None:
        return nowy

    current = lista
    while current.next is not None:
        current = current.next

    current.next = nowy
    return lista

def usun(lista):
    if lista is None or lista.next is None:
        return None

    current = lista
    while current.next.next is not None:
        current = current.next
    current.next = None

    return lista

def dolacz_liste(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    current = l1
    while current.next is not None:
        current = current.next

    current.next = l2

    return l1

def usunOstPar(lista):
    if lista.val % 2 == 0 and lista.next is None:
        return None
    wartosc = 0
    i = 0
    current = lista
    while current is not None:
        if current.val % 2 == 0:
            wartosc = current.val
            i += 1
        current = current.next

    current = lista
    j = 0
    while current is not None and current.next is not None:
        if current.next.val == wartosc and j == i:
            current.next = current.next.next
        j += 1
        current = current.next

    return lista



d = usun(l)
current = d
while current is not None:
    print(current.val)
    current = current.next
