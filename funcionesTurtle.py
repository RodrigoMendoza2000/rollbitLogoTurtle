from turtle import *

def square():
    for x in range(5):
        forward(20)
        right(90)
    left(90)

def square10():
    for x in range(5):
        forward(10)
        right(90)
    left(90)

def leftSquare():
    for x in range(5):
        backward(20)
        left(90)
    right(90)

def leftSquare10():
    for x in range(5):
        backward(10)
        left(90)
    right(90)

def downRight(derecha, abajo):
    begin_fill()
    right(90)
    forward(20)
    for x in range(abajo):
        square()
    end_fill()
    left(180)
    forward(20)
    right(90)
    begin_fill()
    for x in range(derecha):
        square()
    end_fill()

def downRight10(derecha, abajo):
    begin_fill()
    right(90)
    forward(10)
    for x in range(abajo):
        square10()
    end_fill()
    left(180)
    forward(10)
    right(90)
    begin_fill()
    for x in range(derecha):
        square10()
    end_fill()

def upRight(derecha, arriba):
    begin_fill()
    for x in range(derecha):
        square()
    end_fill()

    backward(20)
    left(90)
    begin_fill()
    for x in range(arriba):
        square()
    end_fill()
    right(90)
    forward(20)

def upRight10(derecha, arriba):
    begin_fill()
    for x in range(derecha):
        square10()
    end_fill()

    backward(10)
    left(90)
    begin_fill()
    for x in range(arriba):
        square10()
    end_fill()
    right(90)
    forward(10)

def upLeft(izquierda, arriba):
    begin_fill()
    right(90)
    for x in range(arriba):
        leftSquare()
    end_fill()

    left(90)
    backward(20)
    begin_fill()
    for x in range(izquierda):
        leftSquare()
    end_fill()
    forward(20)

def upLeft10(izquierda, arriba):
    begin_fill()
    right(90)
    for x in range(arriba):
        leftSquare10()
    end_fill()

    left(90)
    backward(10)
    begin_fill()
    for x in range(izquierda):
        leftSquare10()
    end_fill()
    forward(10)

def downLeft(izquierda, abajo):
    begin_fill()
    left(90)
    backward(20)
    for x in range(abajo):
        leftSquare()
    end_fill()
    right(180)
    backward(20)
    left(90)
    begin_fill()
    for x in range(izquierda):
        leftSquare()
    end_fill()

def downLeft10(izquierda, abajo):
    begin_fill()
    left(90)
    backward(10)
    for x in range(abajo):
        leftSquare10()
    end_fill()
    right(180)
    backward(10)
    left(90)
    begin_fill()
    for x in range(izquierda):
        leftSquare10()
    end_fill()
