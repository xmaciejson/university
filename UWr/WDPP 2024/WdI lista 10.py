class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


# ZAD1
def dodaj_na_koniec(head, val):
    new_item = ListItem(val)

    # Sprawdzamy czy lista jest pusta
    if head is None:
        return new_item

    # Szukamy ostatniego elementu
    current = head
    while current.next is not None:
        current = current.next

    current.next = new_item
    return head


# ZAD2
def usun_ostatni(head):
    if head is None or head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None
    return head


# ZAD3
def dolacz_liste(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    current = head1
    while current.next is not None:
        current = current.next

    current.next = head2
    return head1


# ZAD4
def usun_wartosci(head, val):
    while head is not None and head.val == val:
        head = head.next

    current = head

    while current is not None and current.next is not None:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# ZAD6
def wypisz_odwrotnie(head):
    if head is None:
        return

    wypisz_odwrotnie(head.next)
    print(head.val)


# ZAD7
def odwroc_liste(head):
    prev = None
    current = head

    while current is not None:
        next_el = current.next  # Zapamietujemy nastepny element
        current.next = prev  # Odwracamy wskaznik
        prev = current  # Przesuwamy prev na biezacy element
        current = next_el  # Przesuwamy current na nastepny element

    # Nowa glowa listy to poprzedni element
    return prev


# ZAD8
def rozdziel_liste(head):
    dodatnie_head = dodatnie_tail = None
    ujemne_head = ujemne_tail = None
    current = head

    while current is not None:
        next_el = current.next
        current.next = None

        if current.val > 0:
            if dodatnie_head is None:
                dodatnie_head = dodatnie_tail = current
            else:
                dodatnie_tail.next = current
                dodatnie_tail = current
        elif current.val < 0:
            if ujemne_head is None:
                ujemne_head = ujemne_tail = current
            else:
                ujemne_tail.next = current
                ujemne_tail = current

        current = next_el

    return dodatnie_head, ujemne_head


# ZAD10
def scal_listy(l1, l2):
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    current = head
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is not None:
        current.next = l1
    if l2 is not None:
        current.next = l2

    return head

l1 = ListItem(10)
l1.next = ListItem(20)
l2 = ListItem(5)
l2.next = ListItem(15)
head = scal_listy(l1, l2)

current = head
while current is not None:
    print(current.val)
    current = current.next
