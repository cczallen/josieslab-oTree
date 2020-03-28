from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class GetMoneyNowOrFuture(Page):
    form_model = 'player'
    form_fields = [
    	'waiting_period',
    	'gained_amount',
    	'get_money_now_or_future', 
    	'num_listen_times', 'decision_duration',
    	]


class Results(Page):
    pass

page_sequence = [GetMoneyNowOrFuture, Results]
