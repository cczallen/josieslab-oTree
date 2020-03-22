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


author = 'NTUECON'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'time_money'
    players_per_group = None
    num_rounds = 1
    
    subject = "我"
        
    week_num1 = 4
    week_num2 = 8
    week_num3 = 24

    money_num1 = 105
    money_num2 = 110
    money_num3 = 115
    money_num4 = 120
    money_num5 = 125
    money_num6 = 130
    money_num7 = 135
    money_num8 = 140
    money_num9 = 145
    money_num10 = 150


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    accept1 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept2 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept3 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept4 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept5 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept6 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept7 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept8 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept9 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept10 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])

    accept11 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept12 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept13 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept14 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept15 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept16 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept17 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept18 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept19 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept20 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    
    accept21 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept22 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept23 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept24 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept25 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept26 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept27 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept28 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept29 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    accept30 = models.StringField(label="請問您是否要將報酬更換為上述選項", widget=widgets.RadioSelect, choices=["要","不要"])
    
    gender = models.StringField(label="1.您的性別是", widget=widgets.RadioSelect, choices=["男","女"])
    bloodgroup = models.StringField(label="2.您的血型是", widget=widgets.RadioSelect, choices=["A型","B型","AB型","O型","未知","以上皆非"])
    taiwanese = models.StringField(label="3.您是否為台灣本地生", widget=widgets.RadioSelect, choices=["台灣本地生","非台灣本地生（例如僑生、外籍交換生學生）"])
    econ_manage = models.StringField(label="4.您是否是經濟系或管理學院的學生", widget=widgets.RadioSelect, choices=["是","否"])
    class_num = models.StringField(label="5.您修過多少門經濟學的課程", widget=widgets.RadioSelect, choices=["1門","2門","3門","4門","5門","超過5門"])
    grade = models.StringField(label="6.您的系級是", widget=widgets.RadioSelect, choices=["大學部1年級","大學部2年級","大學部3年級","大學部4年級","大學部5年級以上","碩士班學生"])
    guess = models.LongStringField(label="7.請您猜測本實驗的目的為何", )
    
    listenTime1 = models.IntegerField(initial=0)
    listenTime2 = models.IntegerField(initial=0)
    listenTime3 = models.IntegerField(initial=0)
    listenTime4 = models.IntegerField(initial=0)
    listenTime5 = models.IntegerField(initial=0)
    listenTime6 = models.IntegerField(initial=0)
    listenTime7 = models.IntegerField(initial=0)
    listenTime8 = models.IntegerField(initial=0)
    listenTime9 = models.IntegerField(initial=0)
    listenTime10 = models.IntegerField(initial=0)
    
    listenTime30 = models.IntegerField(initial=0)

    decisionduration1 = models.IntegerField(initial=0)
    decisionduration2 = models.IntegerField(initial=0)
    decisionduration3 = models.IntegerField(initial=0)
    decisionduration4 = models.IntegerField(initial=0)
    decisionduration5 = models.IntegerField(initial=0)
    decisionduration6 = models.IntegerField(initial=0)
    decisionduration7 = models.IntegerField(initial=0)
    decisionduration8 = models.IntegerField(initial=0)
    decisionduration9 = models.IntegerField(initial=0)
    decisionduration10 = models.IntegerField(initial=0)
    
    decisionduration30 = models.IntegerField(initial=0)

    testanscorrect = models.IntegerField(initial=1)
