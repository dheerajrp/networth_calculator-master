from django.db import models

class NetWorth(models.Model):
    liquid_money = models.FloatField()
    stocks_value = models.FloatField()
    mutual_funds = models.FloatField()
    us_stocks = models.FloatField()
    crypto = models.FloatField()
    debt_funds = models.FloatField()
    liabilities = models.FloatField()