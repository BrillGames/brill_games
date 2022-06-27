#!/usr/bin/env python3


class Answer:
    def __init__(self, answer, question, points):
        self.__answer = answer
        self.__question = question
        self.__points = points

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, x):
        self.__answer = x

    @property
    def question(self):
        return self.__question

    @question.setter
    def question(self, x):
        self.__question = x

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, x):
        self.__points = x


class Board:
    def __init__(self, answers, columns, players):
        self.__answers = answers
        self.__columns = columns
        self.__players = players

    @property
    def answers(self):
        return self.__answers

    @answers.setter
    def answers(self, x):
        self.__answers = x

    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, x):
        self.__columns = x

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, x):
        self.__players = x
