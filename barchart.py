# This module contains a function for drawing the barchart

def draw_bar(chart,key,value):
    chart.forward(20)                # Leave small gap before each bar
    chart.begin_fill()               # Start to fill the bar
    chart.left(90)
    chart.forward(value)             # Draw up at the left side
    chart.write(key+" "+str(value))  # Print item name and their quantity
    chart.right(90)
    chart.forward(40)                # Width of bar, along the top
    chart.right(90)
    chart.forward(value)             # And draw downward at right side
    chart.left(90)                   # Put the turtle facing the way we found it
    chart.end_fill()                 # Stop to fill the bar (end)
    chart.forward(20)                # Leave small gap after each bar
