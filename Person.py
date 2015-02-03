class Person(object):

    def __init__(self, health, money):
        self.health = health
        self.money = money
        self.gender = None
        self.factory = None

    def get_money(self):
        return self.money

    def get_health(self):
        return self.health

    def get_gender(self):
        return self.gender

    def get_factory(self):
        return self.factory

    def set_money(self, money):
        self.money = money

    def set_health(self, health):
        self.health = health

    def set_gender(self, gender):
        self.gender = gender

    def set_factory(self, factory):
        self.factory = factory

    def inc_money(self, inc):
        self.money += inc

    def inc_health(self, inc):
        self.health += inc
