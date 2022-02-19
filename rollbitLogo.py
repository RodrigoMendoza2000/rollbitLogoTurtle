from turtle import *
from funcionesTurtle import *

screensize(1000, 1000)

speed(0)
bgcolor('black')
penup()
setpos(-300, 370)
pendown()

color('yellow', 'yellow')
#Cola superior
begin_fill()
for x in range(27):
    square()
end_fill()

leftSquare()

left(90)
begin_fill()
square()
right(90)
forward(20)
for x in range(5):
    square()
end_fill()

#Parte derecha arriba
downRight(3,1)
downRight(2,1)
downRight(2,1)
downRight(1,1)
downRight(2,1)

downRight(1,2)
downRight(1,1)
downRight(1,2)
downRight(1,2)
downRight(1,3)

downRight(0,7)


begin_fill()
leftSquare()
end_fill()


#Parte derecha abajo
downLeft(1,3)
downLeft(1,2)
downLeft(1,2)
downLeft(1, 1)
downLeft(2,2)

downLeft(1, 1)
downLeft(2, 1)
downLeft(2,1)
downLeft(3,1)

downLeft(5,1)

#Pata inferior
left(90)
begin_fill()
square()
end_fill()
right(90)

begin_fill()
for x in range(27):
    leftSquare()
end_fill()
for x in range(24):
    square()

forward(20)

"""begin_fill()
right(90)
for x in range(2):
    leftSquare()
end_fill()"""

upLeft(2,1)
upLeft(2,1)
upLeft(1,1)
upLeft(2,1)

upLeft(1,2)
upLeft(1,1)
upLeft(1,2)
begin_fill()
for x in range(9):
    leftSquare()
end_fill()
for x in range(9):
    square()
upLeft(1,2)
upLeft(1,3)

upLeft(0, 7)

#square()
upRight(1, 3)
upRight(1, 2)
begin_fill()
for x in range(9):
    leftSquare()
end_fill()
for x in range(9):
    square()
upRight(1, 2)
upRight(1, 1)
upRight(1, 2)

upRight(2, 1)
upRight(1, 1)

upRight(2, 1)
upRight(2, 1)

penup()
for x in range(3):
    square()
square10()
right(90)
forward(20)
pendown()

penup()
forward(160)
pendown()
left(90)

begin_fill()
for x in range(6):
    square10()
end_fill()

downRight10(3,1)
downRight10(2,1)
downRight10(2,1)
downRight10(1,1)
downRight10(2,1)

downRight10(1,2)
downRight10(1,1)
downRight10(1,2)
downRight10(1,2)
downRight10(1,3)

downRight10(0,7)

begin_fill()
leftSquare10()
end_fill()

downLeft10(1,3)
downLeft10(1,2)
downLeft10(1,2)
downLeft10(1, 1)
downLeft10(2,2)

downLeft10(1, 1)
downLeft10(2, 1)
downLeft10(2,1)
downLeft10(3,1)

downLeft10(5,1)


forward(10)

upLeft10(3,1)
upLeft10(2,1)
upLeft10(2,1)
upLeft10(1,1)
upLeft10(2,1)

upLeft10(1,2)
upLeft10(1,1)
upLeft10(1,2)

upLeft10(1,2)
upLeft10(1,3)

upLeft10(0, 7)

upRight10(1, 3)
upRight10(1, 2)

upRight10(1, 2)
upRight10(1, 1)
upRight10(1, 2)

upRight10(2, 1)
upRight10(1, 1)

upRight10(2, 1)
upRight10(2, 1)
upRight10(3, 1)

done()