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


author = 'Josie_NTULAB'

doc = """
決策實驗-結果部分
"""


class Constants(BaseConstants):
    name_in_url = 'EconExp1_TimePrefPronoun1_selection_result'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
