from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, WaitingPeriod, GainedAmount
from random import randint
import random

class GetMoneyNowOrFuture(Page):
    form_model = 'player'
    form_fields = [
    	'waiting_period',
    	'gained_amount',
    	'get_money_now_or_future', 
    	'num_listen_times', 'decision_duration',
    	]

    def generate_questionare_parameters_pairs(self):
        q_params_pairs = []
        # 產生所有週數和金額的組合
        for each_waiting_period in list(WaitingPeriod):
          for each_gained_amount in list(GainedAmount):
            q_params_pairs.append(
              dict(
                waiting_period = each_waiting_period,
                gained_amount = each_gained_amount,
              )
            )
        return q_params_pairs

    def setup_questionare_parameters_pairs(self):
        # 如果還不存在，就現在產生「週數和金額的組合」並存起來
        # 如果已經存在，就取出
        if Constants.key_q_params_pairs not in self.participant.vars: 
            pairs = self.generate_questionare_parameters_pairs()
            random.shuffle(pairs) # 打亂順序
            self.participant.vars[Constants.key_q_params_pairs] = pairs
        q_params_pairs = self.participant.vars[Constants.key_q_params_pairs]

        # 設定每一 round 的參數，並寫入 db
        idx = self.round_number - 1 # list 從0開始 但 round_bnumber 從1開始
        pair = q_params_pairs[idx]
        self.player.waiting_period = pair['waiting_period'].value
        self.player.gained_amount = pair['gained_amount'].value

    def select_questionare(self):
        q_params_pairs = self.participant.vars[Constants.key_q_params_pairs]
        selected_idx = randint(1, Constants.num_rounds) - 1 # list 的 index 從0開始 但 round_bnumber 從1開始
        selected_q_parama_pair = q_params_pairs[selected_idx]
        selected_player = self.player.in_all_rounds()[selected_idx]
        selected_player.is_selected = True
        self.participant.vars[Constants.key_selected_q] = dict(
            selected_round_number = selected_idx + 1,
            selected_waiting_period = selected_q_parama_pair['waiting_period'].value,
            selected_gained_amount = selected_q_parama_pair['gained_amount'].value,
            selected_get_money_now = selected_player.get_money_now_or_future == 'now',
            )

    def is_displayed(self):
        # 設定每一 round 的參數（如週數和金額）
        self.setup_questionare_parameters_pairs()
        return True

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            # 只在最後一回合才抽結果
            self.select_questionare()


class Results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return self.participant.vars[Constants.key_selected_q]

    def is_displayed(self):
        # 只在最後一回合才顯示
        return self.round_number == Constants.num_rounds

page_sequence = [GetMoneyNowOrFuture, Results]
