from tkinter import *
from tkinter import messagebox
import random

class board:
    background_color={
        '2':'',
        '4':'',
        '8':'',
        '16':'',
        '32':'',
        '64':'',
        '128':'',
        '256':'',
        '512':'',
        '1024':'',
        '2048':'',
    }

    foreground_color={
          '2':'',
        '4':'',
        '8':'',
        '16':'',
        '32':'',
        '64':'',
        '128':'',
        '256':'',
        '512':'',
        '1024':'',
        '2048':'',
    }

    def __init__(self) -> None:
        self.n = 4
        self.window.Tk()
        self.window.title("2048 by AlexisKay")
        self.gameArea=Frame(self.window,background=('azure3'))
        self.board=[]


        pass