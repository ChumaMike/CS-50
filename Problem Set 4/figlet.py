from pyfiglet import Figlet
import sys

"""
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.

Two if the user would like to output text in a specific font, 
in which case the first of the two should be -f or --font, and 
the second of the two should be the name of the font.

Prompts the user for a str of text.
Outputs that text in the desired font.




"""
figlet = Figlet()
fontss = figlet.getFonts()

if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] in fontss:
        figlet.setFont(font=sys.argv[2])
        iform = input("string: ")
        print(figlet.renderText(iform))
    else:
        sys.exit("Invalid usage ")
else:
    sys.exit("Invalid usage ")


    