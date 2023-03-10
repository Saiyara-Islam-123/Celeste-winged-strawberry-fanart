#Name: Saiyara Islam

import turtle
import math
turtle.speed("fastest")

def my_artwork():
    """(NoneType) -> NoneType
    Draws the winged strawberry from the game "Celeste" by calling several functions.
    """
    
    def left_wing():
        """ (NoneType) -> NoneType
        Draws the left wing of the winged strawberry
        
        """
        leo.fillcolor("floral white")
        leo.begin_fill()
        
        leo.left(150)
        leo.forward(80)
        leo.left(30)
        leo.forward(50)

        leo.right(270)
        leo.forward(10)
        leo.right(270)
        leo.forward(40)
        leo.right(180)
        
        leo.forward(30)
        leo.left(90)
        
        for i in range(5):
            leo.forward(10)
            leo.left(90)
            leo.forward(30)
            leo.right(180)
            leo.forward(20)
            leo.left(90)
            
        leo.left(90)
        leo.forward(30)
        leo.right(45)
        leo.forward(41.5)
        leo.left(135)
        leo.forward(50)
        
        leo.end_fill()
        
        
    left_wing()

    def strawberry():
        """ (NoneType) -> NoneType
        Draws the strawberry
        
        """
        leo.fillcolor("red3")
        leo.begin_fill()
        leo.right(30)
        leo.forward(15)
        leo.right(60)
        leo.forward(60)
        leo.right(60)
        leo.forward (15)
        leo.right(30)
        leo.forward(50)
        leo.right(45)
        leo.forward(40)
        leo.right(45)
        leo.forward(18)
        leo.right(45)
        leo.forward(40)
        leo.end_fill()
    strawberry()

    leo.right(45)
    leo.forward(50)
    leo.penup()
    leo.right(30)
    leo.forward(15)
    leo.right(60)
    leo.forward(60)
    leo.right(60)
    leo.forward(15)

    def right_wing():
        """ (NoneType) -> NoneType
        Draws the right wing after correctly positioning the turtle
        
        """
        leo.pendown()
        leo.left(90)
        leo.fillcolor("floral white")
        leo.begin_fill()
        
        leo.forward(80)
        leo.right(30)
        leo.forward(50)
        
        leo.left(270)
        leo.forward(10)
        leo.left(270)
        leo.forward(40)
        leo.left(180)
        
        leo.forward(30)
        leo.right(90)
        
        for i in range(5):
            leo.forward(10)
            leo.right(90)
            leo.forward(30)
            leo.left(180)
            leo.forward(20)
            leo.right(90)
        
        leo.right(90)
        leo.forward(30)
        leo.left(45)
        leo.forward(41.5)
        leo.right(135)
        leo.forward(50)
        
        leo.end_fill()
    right_wing()

    leo.left(30)
    leo.forward(15)
    leo.right(75)

    def leaf_1():
        """(NoneType) -> NoneType
        Draws the right most leaf

        """
        leo.fillcolor("dark olive green")
        leo.begin_fill()
        leo.forward(10 * math.sqrt(2))
        leo.left(70)
        leo.forward(10 * math.sqrt(5))
        leo.left(150)
        leo.forward(20)
        leo.right(10)
        leo.forward(10)
        leo.end_fill()
    leaf_1()

    leo.right(75)

    def leaf_2():
        """(NoneType) -> NoneType
        Draws the right most leaf
        
        """
        leo.penup()
        leo.forward(55)
        leo.fillcolor("dark olive green")
        leo.begin_fill()
        leo.pendown()
        leo.right(45)
        leo.forward(10 * math.sqrt(2))
        leo.right(70)
        leo.forward(10 * math.sqrt(5))
        leo.right(150)
        leo.forward(20)
        leo.left(10)
        leo.forward(12)
        leo.end_fill()
    leaf_2()

    leo.left(75)

    def middle_leaves(b, angle):
        """(num, num) -> NoneType
        Takes the common base and common angle of the three congruent isosceles triangles and draws them
        
        """
        leo.fillcolor("dark olive green")
        leo.begin_fill()
        
        for i in range (4):
            leo.left(angle)
            leo.forward(b)
            leo.right(2 * angle)
            leo.forward(b)
            leo.left(angle)
            
        leo.end_fill()
    middle_leaves(35, 80)

    def first_block_of_seeds():
        """(NoneType) -> NoneType
        Draws the first block of seeds of the strawberry
        
        """
        leo.penup()
        leo.goto(10, 0)
        leo.right(90)
        leo.pendown()
        leo.color("floral white")
        j = 0
        for j in range (6):
            leo.penup()
            leo.goto(10 + 10 * j , 0)
            leo.pendown()
            for i in range(3):
                leo.pensize(3)
                leo.forward(2)
                leo.penup( )
                leo.goto(10 + 10 * j , 0 - i * 20)
                leo.pendown()
                leo.forward(3)
                
    first_block_of_seeds()

    def second_block_of_seeds():
        """(NoneType) -> NoneType
        Draws the second block of seeds of the strawberry
        
        """
        leo.penup()
        leo.goto(20, -60)
        k = 0
        leo.pendown()
        for k in range(5):
            leo.forward(3)
            leo.penup()
            leo.goto(20 + 10 * k , -60)
            leo.pendown()
    second_block_of_seeds()

    leo.color("black")
    leo.penup()
    leo.goto(100 , -100)
    leo.pensize(1)
    leo.pendown()
    leo.right(90)

    for l in range(2):
        leo.forward(20)
        leo.left(90)

    for m in range(2):
        leo.forward(20)
        leo.right(90)
        
    leo.forward(20)
    leo.hideturtle()

leo = turtle.Turtle()
my_artwork()
