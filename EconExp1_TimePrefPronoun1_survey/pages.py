from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['gender','bloodgroup','taiwanese','econ_manage','class_num','grade','guess']


page_sequence = [Survey]
