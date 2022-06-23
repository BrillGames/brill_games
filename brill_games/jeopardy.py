from tkinter import *

class Answer:
    def __init__(self, answer, question, points):
        self.__answer = answer
        self.__question = question
        self.__points = points

    def getAnswer(self):
        return self.__answer

    def getQuestion(self):
        return self.__question

    def getPoints(self):
        return self.__points

    def setAnswer(self, x):
        self.__answer = x

    def setQuestion(self, y):
        self.__question = y

    def setPoints(self, z):
        self.__points = z

if __name__ == "__main__":
    pass