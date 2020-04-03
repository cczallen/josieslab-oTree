from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from EconExp1_TimePrefPronoun1_questionaire.models import GainedAmount


class Results(Page):
    def vars_for_template(self):
        vars = self.participant.vars['selected_questionare'].copy()
        vars['gained_amount_today'] = GainedAmount.get_TWD_today()
        return vars

page_sequence = [Results]
