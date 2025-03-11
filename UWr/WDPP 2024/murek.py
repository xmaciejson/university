from turtle import *


def kwadrat(bok):
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()


def murek(s, bok):
    kolory = ["yellow", "blue", "red", "green", "purple", "orange", "cyan", "pink", "brown", "black"]
    kolor = kolory[0]

    for a in s:
        if a == 'f':
            color('black', kolor)
            kwadrat(bok)
            fd(bok)
        elif a == 'b':
            color('black', kolor)
            kwadrat(bok)
            bk(bok)
        elif a == 'l':
            lt(90)
            bk(bok)
        elif a == 'r':
            rt(90)
            fd(bok)
        elif a.isdigit():
            kolor = kolory[int(a) % len(kolory)]


def rysuj_kwadrat_kolorowy():
    program=""
    for i in range(4):
        program+=str(i)+"fr"
    murek(program, 20)

ht()
tracer(0, 0)

rysuj_kwadrat_kolorowy()

penup()
fd(100)
pendown()


program=""

for i in range(14):
    for j in range(i):
        k=j
        if i > 9:
            k -= 10
        program+=str(k)+"f"
    program += "r"

murek(program, 10)

update()
done()
