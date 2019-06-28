from cursesmenu import *
from cursesmenu.items import *
menu = CursesMenu("SACK Panic Scanner", " Please choo choo choose an option ")
command_item = CommandItem("Scan internet for CVE-2019-11477", "gtimeout 9s python matrix.py;mplayer -fs -vo matrixview 23.avi")
menu.append_item(command_item)
menu.show()