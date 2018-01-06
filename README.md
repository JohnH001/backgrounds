# backgrounds
Hi everyone, this is my first contribution on GitHub.  I'm a **newb** at Python, so **please** take it easy on me.
I made this script after doing a tutorial on the os module.  You'll also see I had recently learned about list
comprehensions, so I used them to practice.

## About this Script / Why was it made?
Windows 10 has some attractive backgrounds on the login screen.  The problem is that the backgrounds are stored 
with no file extension and in a directory with lots of other images.
**Note: This script is only relevant for Windows 10 users!**

### This script: 
  - locates the 'ContentsDeliverySystem' directory on the computer, 
  - creates a new directory called AutoBackgrounds in the user's 'Pictures' directory, then
  - moves the login backgrounds to the AutoBackgrounds directory and adds a '.bmp' file extension.
  
The script also checks the image size to ensure it's an image of reasonable size, and that it's in landscape format.  It also
checks to ensure that the image hasn't already been moved over in the past.

## When to Run
It's recommended that the user runs the script whenever they see new login backgrounds that they want available to them.

## Initial Set-Up: Using the Backgrounds
Once you've run the script, you'll have to do the following only once:
In order to use the backgrounds,
  - right click on the desktop, select Personalize,
  - in the Background drop-down select Slideshow,
  - under Choose albums for your slideshow click the Browse button,
  - navigate to the AutoBackgrounds directory (it's under This PC > Pictures > AutoBackgrounds)
  - choose how often to change the backgrounds (shuffle is recommended)

