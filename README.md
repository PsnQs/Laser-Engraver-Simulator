# Laser-Engraver-Simulator

This is a project that takes G-code as input and creates a visual simulation of a laser engraver that draws the G-code. 

The prograrm starts with converting the xy coordinates of the G-code into angles, because the angle of the laser beam is being controlled. This is done with the convertToAngle.ipynb jupyter notebook which imports from the StepperMotorControllerModule.py python file. Then, the simulation.ipynb jupyter notebook is run to create the simulation, importing from the StepperMotor.py python file. 
The code visualizes the laser engraving process using the ipyvolume package: https://ipyvolume.readthedocs.io/en/latest/install.html#

G-code can be created from an image file, for example, with the Inkscape extension here: https://github.com/arpruss/gcodeplot
This code by arpruss can be used in inkscape to convert svg files to G-code.

