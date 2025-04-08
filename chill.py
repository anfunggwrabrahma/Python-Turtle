import turtle
import time

screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor("skyblue")
screen.title("Mountains and Sun Scene")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_sun():
    t.penup()
    t.goto(250, 150)
    t.color("yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def draw_ground():
    t.penup()
    t.goto(-400, -100)
    t.color("light green")
    t.begin_fill()
    t.forward(800)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(150)
    t.end_fill()
    t.setheading(0) 

def draw_hills():
    hill = turtle.Turtle()
    hill.hideturtle()
    hill.color("dark green")
    hill.penup()
    
    positions = [-400, -250, -100, 50, 200]
    peaks = [100, 130, 110, 140, 120]
    width = 200 

    for i in range(5):
        base_x = positions[i]
        peak_height = peaks[i]
        hill.goto(base_x, -100)
        hill.begin_fill()
        hill.pendown()
        hill.goto(base_x + width // 2, peak_height) 
        hill.goto(base_x + width, -100) 
        hill.goto(base_x, -100)
        hill.end_fill()
        hill.penup()

def draw_cloud(x, y):
    cloud = turtle.Turtle()
    cloud.hideturtle()
    cloud.penup()
    cloud.speed(0)
    cloud.color("white")
    cloud.goto(x, y)
    cloud_list.append(cloud)  # Add to cloud list
    
    # Draw 3 small white circles next to each other
    cloud.begin_fill()
    for _ in range(3):
        cloud.circle(10)
        cloud.penup()
        cloud.forward(15)
        cloud.pendown()
    cloud.end_fill()

def draw_tree(x, y):
    # Tree trunk
    t.penup()
    t.goto(x, y)
    t.color("saddle brown")
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(10)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()

    # Tree top (green circle)
    t.penup()
    t.goto(x + 5, y + 10)
    t.color("forest green")
    t.begin_fill()
    t.circle(12)
    t.end_fill()
    
def draw_road():
    t.penup()
    t.goto(-400, -160)
    t.color("dimgray")
    t.begin_fill()
    t.forward(800)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(40)
    t.end_fill()
    t.setheading(0)

    # Optional: Draw dashed white center line
    t.color("white")
    t.pensize(2)
    t.penup()
    t.goto(-390, -180)
    t.setheading(0)
    for _ in range(20):
        t.pendown()
        t.forward(15)
        t.penup()
        t.forward(25)

def draw_car(x, y):
    screen.register_shape("cz.gif")  # Register the custom shape
    car = turtle.Turtle()
    car.shape("cz.gif")              # Set the turtle shape to car
    car.penup()
    car.goto(x, y)
    return car


def draw_background():
    draw_sun()
    draw_ground()
    draw_cloud(-200, 150)
    draw_cloud(0, 170)
    draw_cloud(150, 140)
    draw_cloud(300, 200) 
    draw_hills()
    draw_road()
    tree_positions = [-400, -330, -280, -180, -100, -20, 60, 140, 230, 300, 340]
    for pos in tree_positions:
        draw_tree(pos, -90)

cloud_list = []  # To keep track of all clouds

draw_background()

# === Animate car and clouds together ===
car = draw_car(-400, -180)

for _ in range(160):
    car.forward(5)
    
    for cloud in cloud_list:
        x, y = cloud.position()
        cloud.goto(x + 0.5, y)  # Move cloud slowly to right

    screen.update()
    time.sleep(0.02)
    
turtle.done()
