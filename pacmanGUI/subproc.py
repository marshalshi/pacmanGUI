from subprocess import *

def noSudoList(lst):
    lst = lst.split()
    if not check_call(lst):
        return check_output(lst)
    else:
        return False

def man(lst):
    lst = lst.split()
    return check_output(lst)

def SudoList(lst, psw):
    lst = lst.split()
    proc1 = Popen(lst , stdin = PIPE, stdout = PIPE)
    return proc1.communicate(psw+'\n')[0]

def SudoY(lst):
    lst = lst.split()
    proc2 = Popen(lst, stdin = PIPE, stdout = PIPE)
    return proc2.communicate('y\n')[0]
