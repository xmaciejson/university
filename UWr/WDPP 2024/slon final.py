import turtle

def rysuj_sloni():
    # Ustawienia początkowe
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Tworzenie obiektu turtle
    slon = turtle.Turtle()
    slon.fillcolor("gray")
    slon.pensize(3)

    # Rysowanie ciała
    slon.begin_fill()
    slon.circle(100)  # Ciało
    slon.end_fill()

    # Rysowanie głowy
    slon.penup()
    slon.goto(-40, 100)
    slon.pendown()
    slon.begin_fill()
    slon.circle(60)  # Głowa
    slon.end_fill()

    # Rysowanie trąby
    slon.penup()
    slon.goto(-30, 70)
    slon.pendown()
    slon.fillcolor("gray")
    slon.begin_fill()
    slon.setheading(-30)
    slon.forward(40)  # Długość trąby
    slon.circle(-20, 180)  # Zagięcie trąby
    slon.forward(40)  # Powrót do głowy
    slon.end_fill()

    # Rysowanie uszu
    slon.penup()
    slon.goto(-80, 130)
    slon.pendown()
    slon.begin_fill()
    slon.circle(30)  # Lewy uchu
    slon.end_fill()

    slon.penup()
    slon.goto(40, 130)
    slon.pendown()
    slon.begin_fill()
    slon.circle(30)  # Prawy uchu
    slon.end_fill()

    # Rysowanie nóg
    for x in [-60, 60]:
        slon.penup()
        slon.goto(x, -100)
        slon.pendown()
        slon.begin_fill()
        slon.setheading(-90)  # Ustawienie kierunku w dół
        slon.forward(80)  # Noga
        slon.right(90)
        slon.forward(30)  # Szerokość nogi
        slon.right(90)
        slon.forward(80)  # Wysokość nogi
        slon.right(90)
        slon.forward(30)  # Szerokość nogi
        slon.end_fill()

    # Rysowanie ogona
    slon.penup()
    slon.goto(100, -40)
    slon.pendown()
    slon.setheading(-150)  # Ustawienie kierunku ogona
    slon.fillcolor("gray")
    slon.begin_fill()
    slon.forward(40)  # Długość ogona
    slon.right(120)
    slon.forward(15)  # Rysowanie końca ogona
    slon.right(120)
    slon.forward(15)
    slon.end_fill()

    slon.hideturtle()  # Ukryj kursor

    # Zakończenie rysowania
    turtle.done()

rysuj_sloni()
