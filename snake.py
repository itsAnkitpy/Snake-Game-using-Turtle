from turtle import Turtle

# Initializing starting coordinates of our 3 turtle squares to form a snake
starting_positions = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # Referring to the first square turtle in snake
        self.head = self.segments[0]
    
    def create_snake(self):
        # Forming a complete snake using starting coordinates
        for positions in starting_positions:
            self.add_segment(positions)
            

    def add_segment(self,positions):
        # Properties of each turtle square body
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

    # To extend snake body on food consumption. Snake grows by adding a square turtle to end position or tail of snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # To move the snake body we need to know that head square is the most important one to turn a snake along with other 
    # squares.But to achive this we need to start from the last segment.
    # Example - Initially I have 3 squares - For their movement first 
        # 3rd square moves to 2nd square
        # 1st square moves forward
        # 2nd square moves to 1st location
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Distance a snake covers in one movement 
        self.segments[0].forward(MOVE_DISTANCE)


    # Creating four sides of movement and preventing movement in reverse direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):    
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

    