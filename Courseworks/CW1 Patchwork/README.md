Python Coursework: A Patchwork Maker
Introduction
This coursework assignment is designed to give you practice in applying all of the main
programming concepts you’ve seen in the module so far to solve a larger and more complex
problem. The assignment will be marked out of 50 and carries 20% of the module marks (it
is assessment item 3 of the module).
You need to submit your program via the module’s Moodle site by the deadline of 4.00pm,
Monday 11th December 2023, and are required to demonstrate your submitted program
in your 2-hour practical class timetabled in the period 12th-15th December 2023. Study
this handout thoroughly in order to understand exactly what is expected from you for the
coursework.
Your task
Your task is to write a program to display patchworks, an example of which is illustrated
below. The actual patchworks your program will display will depend on your student number
and on the user’s inputs.
Patchworks are square and are made up of square patches. A patchwork can be of three
sizes: 5×5, 7×7 or 9×9 patches. The patchwork background should be white. Each patch can
be one of two different designs or it can be completely plain; it can be one of three different
colours. Every patch features a regular geometric design made up of lines, circles, rectangles
1
and/or polygons and has dimensions of 100 × 100 pixels. The two patch designs and the
layout and colouring of the patchwork are not necessarily as given in the illustration above.
They are determined by the final three digits of your student number, and are displayed in
the tables on the final two pages. The layout and colouring of the patchwork are given by the
antepenultimate (third last) digit of your student number. The two patch designs are given
by the penultimate and final digits of your student number. For example, if your student
number was 2000142, the patch designs and patch arrangement for a 5 × 5 patchwork with
colours blue, green and red are those illustrated on page 1.
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
Main program requirements
Your program should begin by prompting the user, using a text (shell)-based interface, to
enter, in this order:
• the patchwork size (i.e. a single figure giving the common width & height in terms of
patches);
• each of the desired three colours entered one-by-one (separate prompts); the program
should ensure that the colours are all different from each other.
The program’s user interface should be easy to use, helpful and robust; e.g., on entering
invalid data, the user should be given appropriate feedback and re-prompted until the entered
data is valid. (Valid sizes are 5, 7 and 9, and valid colours are red, green, blue, magenta,
orange, yellow and cyan.) Once these details have been entered, the patchwork should
be drawn in a graphics window of the appropriate size and with a white background. For
example, if the user enters size 5, and colours blue, then green and finally red, then (in the
case that your student number ends in 142) the patchwork shown on page 1 should be drawn
in a graphics window of width 500 pixels and height 500 pixels.
Challenge feature
The above requirements are what we expect most students to attempt, and carry the vast majority of the marks for functionality. If you would like a further challenge for a few additional
marks, then we encourage you to attempt this additional feature.
After the patchwork design has been drawn, you should allow the user to edit the patchwork using the mouse and the keyboard. Your program should be in one of the following two
modes at any time:
• selection mode will allow the user to select and deselect patches using the mouse;
• edit mode will allow the user to edit selected patches using the keyboard.
2
The program should begin in selection mode. Whilst in this mode, a 30 × 30 pixel ‘OK button’
(a black-filled rectangle containing the white text ‘OK’), should appear in the top-left corner of
the window and a similar ‘Close’ button should appear in the top-right corner of the window.
The user should be able to select any number of patches by clicking on them with the mouse;
selected patches should be displayed with thick black borders. Selecting a currently selected
patch should deselect it. Clicking on the OK button should cause the program to enter edit
mode (without selecting/deselecting the top-left patch) and the OK and Close buttons should
disappear. Clicking the Close button should cause the window to close (i.e. and the program
to end).
In edit mode, the user should be able to choose various options by pressing particular keys
(on the window, not the shell):
• ‘s’ should enter selection mode.
• ’d’ should deselect all patches.
• ‘p’ should change all selected patches to the ‘penultimate’ digit design, keeping their
colours the same.
• ‘f’ should change all selected patches to the ‘final’ digit design, keeping their colours the
same.
• ‘q’ should change all selected patches to be plain, keeping their colours the same.
• The initial letter of any valid colour (‘r’, ‘g’, ‘b’, ‘m’, ‘o‘, ‘y’ or ‘c’) should change all
selected patches to that colour, keeping their designs the same.
• ‘x’ is reserved for your own operation — use your imagination to create a useful/interesting feature.
• all other should keys have no effect.
Note that keys should not have any effect in selection mode and mouse clicks should have
no effect in edit mode. As an example, to re-colour two patches cyan, starting in selection
mode, the user will click on the two patches (to select them), click in the OK button (to enter
edit mode), press ‘c’ to colour the patches cyan, then press ‘d’ to deselect the patches. Then
to change another patch to be plain, the user will press ‘s’ (to enter selection mode), click
the patch (to select it), click the OK button (to enter edit mode) press ‘q’ (to make the patch
plain), then press ‘d’ to deselect it.
The user should be able to repeatedly choose these options to make as many edits as they
wish. The operations should remove and recreate, or recolour, the graphics objects that make
up patch designs, rather than drawing new objects on top of existing ones.
Moodle Submission
You should submit your program via the module’s Moodle site by the deadline specified
above. Make sure that your program file is named using your student number, and that
it has a .py suffix; for example, 2012345.py. Click on the link labelled Item 3 - Python Patchwork Assignment Dropbox (in the Assessment tab) and upload your program. If you miss
the deadline, you will need to upload it using the late submissions link – your mark will be
capped according to University regulations unless you have a valid EC.
Demonstration & Mark Allocation
You need to demonstrate your program to a member of staff in your Programming practical session timetabled in the period 12th-15th December. We will execute your submitted
program, and we will ask you question(s) about how you wrote it and how it works.
3
All the marks for the assignment will be awarded during the demonstration, so you must
attend: failure to attend the demonstration will result in your work being recorded as a nonsubmission, and demonstrating your program late may result in your mark for the assignment
being capped under University rules. If you wish to organise a late demonstration outside a
timetabled session, please email Matthew—you must have given your demonstration by 2nd
February 2024 or your work will be recorded as a non-submission.
Formal written feedback and your assignment mark will be sent to you via email immediately after your demonstration has been completed. If you do not receive this email, then
your mark may not have been recorded and it is your responsibility to inform Matthew if this
happens.
Functionality [38 marks]
In the demonstration, we will first assess the completeness and correctness of the operation
of your program, and the quality and robustness of its user interface. The main program
requirements will carry 30 marks (8 marks for each of the two patch designs, 8 marks for
the patchwork layout and colouration, and 6 marks for the user interface), and the challenge
(optional) feature will carry 8 marks.
Program code quality [10 marks]
After demonstrating the program’s functionality, the member of staff will give you some feedback on the quality of your program code. Your program will be awarded marks based on: (i)
its overall structure (how well it has been designed using the principles of top-down design—
see lecture 8); (ii) its readability (see lecture 3.2); and (iii) the quality of the algorithms used
(e.g. the control structures it employs to draw the patchwork).
Make sure that your program uses good, uncomplicated, algorithms. Also, try to ensure
that your program would require minimal changes if the requirements were changed so that
more colours were included as being valid, and extra patchwork sizes (11, 13, . . .) were
allowed. Often, repetitive code is a sign of poor algorithm design (e.g. don’t use 25 lines of
code to draw 25 circles!). Even if your program appears to work well, the code may obtain
very few marks if it is poorly written.
Note that assessment of code quality will not apply to the challenge feature.
Explanation of program features [2 marks]
We will award up to 2 marks for your responses to the question(s) we ask you in the demo,
independently of the other marks your submission receives. You will receive:
• 2 marks if you give clear/correct responses to the questions;
• 1 mark if you give less than clear/correct responses;
• 0 marks if your responses are poor and lead the marker to suspect that you did not
write the complete program yourself; in such an event, your work will be investigated
for academic misconduct after the demonstration.
4
General advice
Most importantly, start early and do not leave finishing the work until just before the deadline. Your work will almost always suffer if you leave it until too late. Furthermore, technical
problems are likely to be overcome if encountered early, and do not usually constitute an
acceptable reason for lateness.
If you find the task very difficult, remember that you do not have to provide a complete
solution to achieve a pass mark. Make sure that your program executes and gives some
graphical output, and that you demonstrate what your program does. To make things easier,
you might choose to write a program which, for example:
• draws a patchwork containing just one of the patch designs;
• attempts to draw both patch designs but not in the correct arrangement;
• ignores colours.
If you don’t know how to start, ask for help as early as possible (see the Support section).
Hint
If well designed, your program will consist of a few functions including a main function and
three patch-drawing functions – one for each design and one for plain patches. (In a good
solution there will be other functions.) Each patch drawing function might need parameters
representing the graphics window on which to draw the patch, the x- and y-coordinates of
the top-left corner of the patch, and the patch colour. Make sure that you have completed
exercises 9 and 10 on worksheet 6, as well as the first few exercises on worksheet 8, before
attempting the coursework.
Support
The last few practicals before the deadline can be used for getting help with the coursework.
Academic Tutors Simon Jones and Eleni Noussi are also able to give advice on the coursework
via one-to-one support sessions.
Other queries should be addressed to Matthew by email. Any reported errors on this handout, or other common issues, will be communicated via the Python Patchwork Coursework
Frequently Asked Questions document in the General section on Moodle, so please check
there before asking a question.
You are allowed to ask others for limited help, but you must write your own code. You
should not, therefore, make extensive use of AI assistance (ChatGPT, Bing, Bard, Copilot Chat
etc.). Remember that anything you submit must be your own work and you will be asked in
the demonstration to explain parts of your code.
Patchwork layout and patch designs
Make sure that your program draws patchworks determined by the final three digits of your
student number. The patch colour shown on the final page is red (but will in general depend
on the user’s inputs). Note the colour of the outline of the shapes – sometimes this is the
patch colour, sometimes it is black. We are not concerned too much if the edges of patches
‘collide’ with other patches or the edge of the window by one pixel. If you wish, you can draw
black borders around patches in order to separate them, but this is not necessary.

Antepenultimate digit of student number
The tables below describe how patches should be arranged and coloured as determined by
the antepenultimate digit of your student number for 5 × 5 and 7 × 7 patchworks. The tables
assume that the first chosen colour is blue, the second is orange and the third colour is red.
It is important that the order of the inputted colours is used correctly. Notice that the top-left
patch always takes the first inputted colour, and the next colour you see if you scan from
left-to-right starting from this patch (continuing scanning from the left of the next row if
required) will be the second inputted colour. Patches labelled with a black ‘F’ should have the
final digit design; patches labelled with a white ‘P’ should have the penultimate digit design;
the unlabelled patches should be plain. Note that the arrangement and colouring is regular
so you should be able to determine what it would look like for patchworks of size 9 × 9.

Penultimate digit of student number
Note that all coordinates should be multiples of 10 except in designs 3, 5, 7 and 8 where
some are multiples of 5; the circles in designs 2 and 3 have radius 5.
Final digit of student number
Note that all coordinates should be multiples of 10 except in designs 0 and 4 where some
are multiples of 5; the circles in design 4 have radii that are multiples of 5. Patch design 5 is
made up of 20 straight lines (there are no curved lines).
