import re

import dateparser


def get_eating_account(from_user, description, time=None):
    return 'Expenses:Food'

def get_credit_return(from_user, description, time=None):
    for key, value in credit_cards.items():
        if key == from_user:
            return value
    return "Unknown"


public_accounts = [
    'Liabilities:CreditCard:SPDB'
]

credit_cards = {
    '中信银行': 'Liabilities:CreditCard:CITIC',
    '广发银行': 'Liabilities:CreditCard:CMB',
    '浦发银行': 'Liabilities:CreditCard:SPDB',
}

accounts = {
    "余额宝": 'Assets:Alipay:MonetaryFund',
    '花呗': 'Liabilities:Alipay:Huabei',
    '浦发银行(4666)': 'Liabilities:CreditCard:SPDB',
    '广发银行(1725)': 'Liabilities:CreditCard:CMB',
    '零钱通': 'Assets:WeChat:Cash',
    '零钱': 'Assets:WeChat:Cash',
}

descriptions = {
    #'滴滴打车|滴滴快车': get_didi,
    '余额宝.*收益发放': 'Assets:Alipay:MonetaryFund',
    # '转入到余利宝': 'Assets:Alipay:MonetaryFund',
    '花呗收钱服务费': 'Expenses:Fee',
    '自动还款-花呗.*账单': 'Liabilities:Alipay:Huabei',
    '信用卡自动还款|信用卡还款': get_credit_return,
    '外卖订单': get_eating_account,
    '美团订单': get_eating_account,
    '上海交通卡发行及充值': 'Expenses:Transport:Card',
    '地铁出行': 'Expenses:Traffic',
    '火车票': 'Expenses:Traffic',
    '单车': 'Expenses:Traffic',
    '滴滴': 'Expenses:Traffic',
    '蚂蚁财富.*': 'Assets:Fund',
}

anothers = {
    '上海拉扎斯': get_eating_account,
    '包子': get_eating_account,
    '好口福': get_eating_account,
    '家饭香': get_eating_account,
    '麦当劳': get_eating_account,
    '每日优鲜': get_eating_account,
    '小遛': "Expenses:Traffic",
    '摩拜': "Expenses:Traffic",
}

incomes = {
    '余额宝.*收益发放': 'Income:PnL:MonetaryFund',
    '蚂蚁财富.*': 'Assets:Cash',
}

description_res = dict([(key, re.compile(key)) for key in descriptions])
another_res = dict([(key, re.compile(key)) for key in anothers])
income_res = dict([(key, re.compile(key)) for key in incomes])
