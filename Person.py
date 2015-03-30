class Person(object):

    def __init__(self, health, money):
        self.health = health
        self.money = money
        self.person = None;
        self.name = None;   
 
    def get_money(self):
        return self.money

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def set_money(self, money):
        self.money = money

    def set_health(self, health):
        self.health = health

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def inc_money(self, inc):
        self.money += inc

    def inc_health(self, inc):
        self.health += inc
