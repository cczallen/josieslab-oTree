from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Results(Page):
    def vars_for_template(self):
        return self.participant.vars['selected_questionare']

page_sequence = [Results]
