from turtle import *
#sample comment
def germany(size):
  penup()
  setpos(-180, 180)
  pendown()
  fillcolor("black")
  begin_fill()
  forward(360 * size/100)
  right(90)
  forward(size)
  right(90)
  forward(360 * size/100)
  right(90)
  forward(size)
  end_fill()
  backward(size)
  fillcolor("red")
  begin_fill()
  right(90)
  forward(360 * size/100)
  right(90)
  forward(size)
  right(90)
  forward(360 * size/100)
  right(90)
  forward(size)
  end_fill()
  penup()
  backward(size)
  fillcolor("yellow")
  begin_fill()
  right(90)
  forward(360 * size/100)
  right(90)
  forward(size)
  right(90)
  forward(360 * size/100)
  right(90)
  forward(size)
  end_fill()
  forward

size = input("What size do you want? Please pick 1-100")
size = int(size)
germany(size)
