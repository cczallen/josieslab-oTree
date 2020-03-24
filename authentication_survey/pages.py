from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class TPage(Page):
    def is_displayed(self):
        key = 'auth_question_passed'
        if key in self.participant.vars:
            return self.participant.vars[key] == False
        return True

class testquestion(TPage):
    form_model = 'player'
    form_fields = ['authentication_question']
    def before_next_page(self):
        if self.player.authentication_question == True:
            self.participant.vars['auth_question_passed'] = True

class testquestion_failed(TPage):
    form_model = 'player'


page_sequence = [testquestion, testquestion_failed]
