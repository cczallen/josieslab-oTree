from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import random


class Intro(Page):
    form_model = 'player'

class QPage(Page):
    pass

class Q1(QPage):
    form_model = 'player'
    form_fields = ['accept1', 'listenTime1', 'decisionduration1']


class Q2(QPage):
    form_model = 'player'
    form_fields = ['accept2', 'listenTime2', 'decisionduration2']


class Q3(QPage):
    form_model = 'player'
    form_fields = ['accept3', 'listenTime3', 'decisionduration3']


class Q4(QPage):
    form_model = 'player'
    form_fields = ['accept4', 'listenTime4', 'decisionduration4']


class Q5(QPage):
    form_model = 'player'
    form_fields = ['accept5', 'listenTime5', 'decisionduration5']


class Q6(QPage):
    form_model = 'player'
    form_fields = ['accept6', 'listenTime6', 'decisionduration6']


class Q7(QPage):
    form_model = 'player'
    form_fields = ['accept7', 'listenTime7', 'decisionduration7']


class Q8(QPage):
    form_model = 'player'
    form_fields = ['accept8', 'listenTime8', 'decisionduration8']


class Q9(QPage):
    form_model = 'player'
    form_fields = ['accept9', 'listenTime9', 'decisionduration9']


class Q10(QPage):
    form_model = 'player'
    form_fields = ['accept10', 'listenTime10', 'decisionduration10']

class Q30(QPage):
    form_model = 'player'
    form_fields = ['accept30', 'listenTime30', 'decisionduration30']

class Survey(QPage):
    form_model = 'player'
    form_fields = ['gender','bloodgroup','taiwanese','econ_manage','class_num','grade','guess']

intro = [Intro]
list = [Q1, Q2]
random.shuffle(list)
intro.extend(list)
intro.append(Survey)
page_sequence = intro
