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

from EconExp1_TimePrefPronoun1_questionaire.models import (
    OptionOfGetMoney,
    WaitingPeriod,
    GainedAmount,
    Treatment,
)


author = 'Josie_NTULAB'

doc = """
決策實驗-說明部分
"""


class Constants(BaseConstants):
    name_in_url = 'EconExp1_TimePrefPronoun1_intro'
    players_per_group = None
    num_rounds = 1

    num_questions = len(WaitingPeriod) * len(GainedAmount)
    pronoun = Treatment.pronoun
    gained_amount_today = GainedAmount.get_TWD_today()


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.treatment_pronoun_included = Treatment.get_pronoun_included(p)


class Group(BaseGroup):
    pass


class Player(BasePlayer): # TODO：有空再尋找能直接繼承（重複利用）EconExp1_TimePrefPronoun1_questionaire.models 裡 Player 的方法
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


