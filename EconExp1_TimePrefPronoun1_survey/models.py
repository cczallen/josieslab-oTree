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


author = 'Josie_NTULAB'

doc = """
決策實驗-問卷調查部分
"""


class Constants(BaseConstants):
    name_in_url = 'EconExp1_TimePrefPronoun1_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.StringField(label = "1.您的性別是", widget = widgets.RadioSelect, choices = ["男", "女", "不指定"])
    bloodgroup = models.StringField(label = "2.您的血型是", widget = widgets.RadioSelect, choices = ["A型", "B型", "AB型", "O型", "未知", "以上皆非"])
    taiwanese = models.StringField(label = "3.您是否為台灣本地生", widget = widgets.RadioSelect, choices = ["台灣本地生", "非台灣本地生（例如僑生、外籍交換生學生）"])
    econ_manage = models.StringField(label = "4.您是否是經濟系或管理學院的學生", widget = widgets.RadioSelect, choices = ["是", "否"])
    class_num = models.StringField(label = "5.您修過多少門經濟學的課程", widget = widgets.RadioSelect, choices = ["1門", "2門", "3門", "4門", "5門", "超過5門"])
    grade = models.StringField(label = "6.您的系級是", widget = widgets.RadioSelect, choices = ["大學部1年級", "大學部2年級", "大學部3年級", "大學部4年級", "大學部5年級以上", "碩士班學生"])
    guess = models.LongStringField(label = "7.請您猜測本實驗的目的為何", )
    
