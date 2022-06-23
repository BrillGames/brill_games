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

    def setQuestion(self, x):
        self.__question = x

    def setPoints(self, x):
        self.__points = x


class Board:
    def __init__(self, answers, columns, players):
        self.__answers = answers
        self.__columns = columns
        self.__players = players

    def getAnswers(self):
        return self.__answers

    def getColumns(self):
        return self.__columns

    def getPlayers(self):
        return self.__players

    def setAnswers(self, x):
        self.__answers = x

    def setColumns(self, x):
        self.__columns = x

    def setPlayers(self, x):
        self.__players = x


if __name__ == "__main__":
    pass
