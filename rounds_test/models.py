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
import random

author = 'Your name here'

doc = """
Your app description
"""


class WaitingPeriod(Enum):
    ONE_WEEK    = 1
    FOUR_WEEK   = 4
    TWELVE_WEEK = 12


class GainedAmount(Enum):
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
    num_rounds = len(WaitingPeriod) * len(GainedAmount) #3 #24
    gained_amount_now = 100
    key_q_params_pairs = 'questionare_parameters_pairs'
    key_selected_q = 'selected_questionare'
    subject = '我'


class OptionOfGetMoney(Enum):
    OPTION_NOW = '選擇今天的報酬'
    OPTION_FUTURE = '選擇未來的報酬'

    def formatted_option(player, option_enum):
        if player.treatment_subject_included:
            return Constants.subject + option_enum.value
        else:
            return option_enum.value


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            if self.round_number == 1:
                p.treatment_subject_included = random.choice([True, False])
            else:
                previous_player = p.in_round(self.round_number - 1)
                p.treatment_subject_included = previous_player.treatment_subject_included


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    treatment_subject_included = models.BooleanField(initial = False)

    get_money_now_or_future = models.StringField(
        label = '請選擇您要今天或未來的報酬', 
        widget = widgets.RadioSelect, 
        )
    def get_money_now_or_future_choices(self):
        return [
            ['now', OptionOfGetMoney.formatted_option(self, OptionOfGetMoney.OPTION_NOW)],
            ['future', OptionOfGetMoney.formatted_option(self, OptionOfGetMoney.OPTION_FUTURE)],
            ]

    # 聽了幾次，單位為次數 (hidden，根據使用者行為紀錄)
    num_listen_times = models.IntegerField(initial = 0)

    # 決策時長，單位為秒數 (hidden，根據使用者行為紀錄)
    decision_duration = models.FloatField(initial = 0)

    # 是否為最後電腦選中的 round (hidden，最後一回合會抽出並寫入)
    is_selected = models.BooleanField(initial = False)
    