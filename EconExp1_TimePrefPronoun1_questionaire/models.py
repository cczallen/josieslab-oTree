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

author = 'Josie_NTULAB'

doc = """
決策實驗-問卷部分
"""


class WaitingPeriod(Enum):
    ONE_WEEK    = 1
    FOUR_WEEK   = 4
    TWELVE_WEEK = 12


class GainedAmount(Enum):
    TWD105 = 105
    TWD110 = 110
    TWD115 = 115
    # TWD120 = 120
    # TWD125 = 125
    # TWD130 = 130
    # TWD135 = 135
    # TWD145 = 145

    def get_TWD_today(): # workaround: 為了不讓 len(GainedAmount) 跟 list(GainedAmount) 會取到 TODAY 的值，所以用了 function 來取
        return 100

class Treatment(object):
    pronoun = '我'
    def get_pronoun_included(player):
        participant = player.participant
        # lazy loading: 若不存在就決定並起來，若已存在就直接取出
        if Constants.key_pronoun_included not in participant.vars:
            participant.vars[Constants.key_pronoun_included] = random.choice([True, False])
        pronoun_included = participant.vars[Constants.key_pronoun_included]
        return pronoun_included


class Constants(BaseConstants):
    name_in_url = 'EconExp1_TimePrefPronoun1_questionaire'
    players_per_group = None
    num_rounds = len(WaitingPeriod) * len(GainedAmount)
    key_q_params_pairs = 'questionare_parameters_pairs'
    key_selected_q = 'selected_questionare'
    key_pronoun_included = 'treatment_pronoun_included'
    pronoun = Treatment.pronoun


class OptionOfGetMoney(Enum):
    OPTION_NOW = '選擇今天的報酬'
    OPTION_FUTURE = '選擇未來的報酬'

    def formatted_option(player, option_enum):
        if player.treatment_pronoun_included:
            return Constants.pronoun + option_enum.value
        else:
            return option_enum.value


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment_pronoun_included = Treatment.get_pronoun_included(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 幾週後 (hidden)
    waiting_period = models.IntegerField()

    # 獲得的報償 (hidden)
    gained_amount = models.IntegerField()

    treatment_pronoun_included = models.BooleanField(initial = False)

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
    