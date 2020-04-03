from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from EconExp1_TimePrefPronoun1_questionaire.pages import GetMoneyNowOrFuture


class Intro_1(Page):
    form_model = 'player'


class Intro_2(Page):
    form_model = 'player'


class Intro_3(GetMoneyNowOrFuture):
	pass

class Intro_4(Page):
    form_model = 'player'
    
    
class Intro_5(Page):
    form_model = 'player'


page_sequence = [Intro_1, Intro_2, Intro_3, Intro_4, Intro_5]
