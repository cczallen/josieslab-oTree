from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
驗證問題
"""


class Constants(BaseConstants):
    name_in_url = 'authentication_survey'
    players_per_group = None
    num_rounds = 99


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    authentication_question = models.BooleanField(
        label="驗證問題：請回答 30 x 2 - 4 = ?", 
        widget=widgets.RadioSelect, 
        choices=[
            [False, '1'],
            [False, '26'],
            [True, '56'],
            [False, '64'],
            ]
        )

