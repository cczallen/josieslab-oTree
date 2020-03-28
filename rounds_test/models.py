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

from enum import Enum


author = 'Your name here'

doc = """
Your app description
"""


class StringEnum(Enum):
    def __str__(self):
        return str(self.value)


class WatingPeriod(StringEnum):
    ONE_WEEK    = 1
    FOUR_WEEK   = 2
    TWELVE_WEEK = 3


class GainedAmount(StringEnum):
    TWD105 = 105
    TWD110 = 110
    TWD115 = 115
    TWD120 = 120
    TWD125 = 125
    TWD130 = 130
    TWD135 = 135
    TWD145 = 145


class Constants(BaseConstants):
    name_in_url = 'rounds_test'
    players_per_group = None
    num_rounds = len(WatingPeriod) * len(GainedAmount) #3 #24

    subject = '我'


class OptionOfGetMoney(Enum):
    OPTION_NOW = '選擇今天的報酬'
    OPTION_FUTURE = '選擇未來的報酬'

    def formatted_option(option_enum):
        treatment_subject_included = True # TODO
        if treatment_subject_included:
            return Constants.subject + option_enum.value
        else:
            return option_enum.value


class Subsession(BaseSubsession):
    def generate_question_parameters_pairs(self):
        question_parameters_pairs = []
        for each_waiting_period in list(WatingPeriod):
          for each_gained_amount in list(GainedAmount):
            question_parameters_pairs.append(
              dict(
                waiting_period = each_waiting_period,
                gained_amount = each_gained_amount,
              )
            )
        return question_parameters_pairs

    def creating_session(self):
        question_parameters_pairs = self.generate_question_parameters_pairs()
        for p in self.get_players():
            if self.round_number == 1:
                import random
                random.shuffle(question_parameters_pairs)
            idx = self.round_number - 1 # list 從0開始 但 round_bnumber 從1開始
            pair = question_parameters_pairs[idx]
            p.waiting_period = pair['waiting_period'].value
            p.gained_amount = pair['gained_amount'].value


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    get_money_now_or_future = models.StringField(
        label = '請選擇您要今天或未來的報酬', 
        widget = widgets.RadioSelect, 
        choices = [
            ['now', OptionOfGetMoney.formatted_option(OptionOfGetMoney.OPTION_NOW)],
            ['future', OptionOfGetMoney.formatted_option(OptionOfGetMoney.OPTION_FUTURE)],
            ]
        )


    # 聽了幾次，單位為次數 (hidden，根據使用者行為紀錄)
    num_listen_times = models.IntegerField(initial = 0)

    # 決策時長，單位為秒數 (hidden，根據使用者行為紀錄)
    decision_duration = models.FloatField(initial = 0)
    
    
