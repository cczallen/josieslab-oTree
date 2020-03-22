from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class TPage(Page):
    def is_displayed(self):
        # return self.player.testQ_passed == False
        if 'testQ_passed' in self.participant.vars:
            return self.participant.vars['testQ_passed'] == False
        return True

class testquestion(TPage):
    form_model = 'player'
    form_fields = ['testQ']
    def before_next_page(self):
        if self.player.testQ == '56':
            # self.player.testQ_passed = True
            self.participant.vars['testQ_passed'] = True

class testquestion_failed(TPage):
    form_model = 'player'


page_sequence = [testquestion, testquestion_failed]
