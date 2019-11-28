This program's main function is to calculate a new value 
from a given set of points. Which are going to beused to 
generate a polynomy of at much n-1 grade.

In order to use this program there are ceratin constraints 
about the libraries that were used to develop this program, 
such as:
	- Tkinter
	- MatPlotLib

The instructions for installing these two libraries are 
quite simple.

Tkinter is installed as you install Python 3.
But for installing matplotlib, you'll need to enter these
2 commands in a cmd:

python -m pip install -U pip
python -m pip install -U matplotlib

Once the process is finished, the program is ready to run. 
And for running it you must run "GUI.py" in the root folder.
Then a new window will appear as shown on the "gui.JPG" file

This window contains 4 data entries. The first 2 (the blue 
ones) are for solving for a single polinomy and an x value.
The other 2 are for directory paths used in the file
input/output feature.

Now, how to use it:

It's quite simple. For the first mode, the manual input,
you'll have to fill 2 data entries. The first is the value
of x to obtain within the function that passes through the
points that you must capture in order for the program to 
use the Newton-Interpolation method to find the polynomy of
(n-1)th power where n is the number of points in the data set.
Then, push the "evaluate" button at the bottom left and in the
white squares the desired answer shall be shown. As well as
it will appear its corresponding point graph at the right side.


For the second mode, the file one, you'll need a file with
written data in an specific format, shown ahead, and a
directory output path for the program to generate the answers.
The input file path it's selected by clicking the "Open" button
which will appear a file browser. Then you shall click on
"Generate Solutions" and select a path where the "result.txt"
file will be written.

Last but not least, the format of the input file.
It's also very simple, every line should be an input data set
in this format:

x1,y1 x2,y2 x3,y3 ... xn,yn|xe,ye

Every set of points shall be separated from each other with a
blank space and the point's values must be separated only by a
comma.
The suffix element (at the side of x or y) is the subindex
xe = desired x value, ye = expected y value
