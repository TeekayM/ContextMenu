from re import L
import sys
import os
os.system("mode con: cols=50 lines=1")
from tkinter import Tk, simpledialog
application_window = Tk()
application_window.withdraw()
answer = simpledialog.askstring("Input", "New extension",
                                parent=application_window)
suffix = "." + answer
argv = sys.argv

path = argv[1].replace("\\", "/")
rawpath = path[:len(path) - len(path.split("/")[len(path.split("/")) - 1])]

withsuffix = path[len(rawpath):]
print(withsuffix)

_nosuffix = withsuffix.split('.')
nosuffix = withsuffix[:len(withsuffix) - len(_nosuffix[len(_nosuffix) - 1]) - 1]
print('rename \"' + withsuffix + "\" \"" + nosuffix + suffix + "\"")
os.system("pushd \"" + rawpath + "\"" + ' && rename \"' + withsuffix + "\" \"" + nosuffix + suffix + "\"")