# Python Coursework: A Patchwork Maker
# Introduction
This coursework assignment is designed to give you practice in applying all of the main
programming concepts you’ve seen in the module so far to solve a larger and more complex
problem. The assignment will be marked out of 50 and carries 20% of the module marks (it
is assessment item 3 of the module).

# The task
Your task is to write a program to display patchworks, an example of which is illustrated
below. The actual patchworks your program will display will depend on your student number
and on the user’s inputs.

Patchworks are square and are made up of square patches. A patchwork can be of three
sizes: 5×5, 7×7 or 9×9 patches. The patchwork background should be white. Each patch can
be one of two different designs or it can be completely plain; it can be one of three different
colours. Every patch features a regular geometric design made up of lines, circles, rectangles
and/or polygons and has dimensions of 100 × 100 pixels. The two patch designs and the
layout and colouring of the patchwork are not necessarily as given in the illustration above.

It’s important that your program draws the patch designs accurately, and that it draws
the correct designs, layout and colouring – you will receive no credit for drawing the wrong
patch designs or patch arrangement.

Your program must draw the patches using the facilities provided in the graphics module
(Line, Circle etc.), and must not use bitmapped images. The designs are intended to test
algorithm development skills (e.g. they should involve the use of one or more for loops). For
some of the designs, it will be useful to remember that shapes drawn later appear on top of
those drawn earlier. You should not use parts of the Python language which we haven’t yet
covered in the module; for example, do not use exception handling and do not define your
own classes.

# Main program requirements
Your program should begin by prompting the user, using a text (shell)-based interface, to
enter, in this order:
- the patchwork size (i.e. a single figure giving the common width & height in terms of
patches);
- each of the desired three colours entered one-by-one (separate prompts); the program
should ensure that the colours are all different from each other.

The program’s user interface should be easy to use, helpful and robust; e.g., on entering
invalid data, the user should be given appropriate feedback and re-prompted until the entered
data is valid. (Valid sizes are 5, 7 and 9, and valid colours are red, green, blue, magenta,
orange, yellow and cyan.) Once these details have been entered, the patchwork should
be drawn in a graphics window of the appropriate size and with a white background. For
example, if the user enters size 5, and colours blue, then green and finally red, then (in the
case that your student number ends in 142) the patchwork shown on page 1 should be drawn
in a graphics window of width 500 pixels and height 500 pixels.
