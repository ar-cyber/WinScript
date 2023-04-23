import tkinter
import os
import sys



import ctypes
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


args = sys.argv
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
        # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1  
def runterm():
    print("(c) Andrew R 2023")
    variables = {}
    while True:
        command = input(">>> ")
        if True:
            if "echo" in command:
                f2 = command.split(" ")
                a = listToString(s = f2[1:])
                print(a)
            elif "start" in command:
                    f2 = command.split(" ")
                    os.system(f2[1])
            elif "cmd" in command:
                f2 = command.split(" ")
                os.system(f2[1])
            elif "msgbox" in command:
                f2 = command.split(" ")
                tk = tkinter.Tk()
                label = tkinter.Label(tk, text=f[1])
                label.pack()
            elif "about" in command:
                print("""Winsc written in Python!
Original written by zvqle""")
            elif "exit" in command:
                exit()
            elif "define" in command:
                    f2 = command.split("def")
                    f2 = listToString(s = f2)
                    anothersp = f2.split(" ")
                    var1 = listToString(s = anothersp[1])

                    var2 = listToString(s = anothersp[2])
                    variables[var1] = var2
            elif "printvar" in command:
                f2 = command.split("printvar")
                f2 = listToString(s = f2)
                anothersp = f2.split(" ")
                print(variables[anothersp[1]])
            else:
                print("SyntaxError: Invalid syntax")
try:
    if ".ws" in args[1]:
        variables = {}
        new = listToString(s = args[1])
        with open("./" + new) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                if "echo" in line:
                    f2 = line.split("echo")
                    a = listToString(s = f2[1:])
                    print(a)
                elif "start" in line:
                    f2 = line.split("start")
                    os.system(f2[1])
                elif "cmd" in line:
                    f2 = line.split("cmd")
                    os.system(f2[1])
                elif "msgbox" in line:
                    f2 = line.split("msgbox")
                    tk = tkinter.Tk()
                    label = tkinter.Label(tk, text=f2[1])
                    label.pack()
                elif "about" in line:
                    print("""Winsc written in Python!
Original written by zvqle""")
                elif "exit" in line:
                    exit()
                elif "define" in line:
                    f2 = line.split("def")
                    f2 = listToString(s = f2)
                    anothersp = f2.split(" ")
                    var1 = listToString(s = anothersp[1])

                    var2 = listToString(s = anothersp[2])
                    variables[var1] = var2
                elif "printvar" in line:
                    f2 = line.split("printvar")
                    f2 = listToString(s = f2)
                    anothersp = f2.split(" ")
                    print(variables[anothersp[1]])
                else:
                    print("SyntaxError: Invalid syntax")
                line = fp.readline()
                cnt += 1
except IndexError:
    print("WinScript Terminal")
    runterm()
except FileNotFoundError:
    print("Cannot find file")

