from faker import Factory
fake = Factory.create()
print(fake.name())

#show providers
print(fake.get_providers())

#none type credit card 3337132030123490
print(fake.credit_card_number(card_type=None))

#expires 12/28
print(fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y'))

#VISA 16 digit Jelani Jenkins 4381669188862778 02/27 CVC: 366
print(fake.credit_card_full(card_type='visa16'))

'''
Card types:
        'maestro':      CreditCard('Maestro',           prefix_maestro, 12, security_code='CVV'),
        'mastercard':   CreditCard('Mastercard',        prefix_mastercard, 16, security_code='CVV'),
        'visa16':       CreditCard('VISA 16 digit',     prefix_visa),
        'visa13':       CreditCard('VISA 13 digit',     prefix_visa, 13),
        'amex':         CreditCard('American Express',  prefix_amex, 15, security_code='CID', security_code_length=4),
        'discover':     CreditCard('Discover',          prefix_discover),
        'diners':       CreditCard('Diners Club / Carte Blanche', prefix_diners, 14),
        'jcb15':        CreditCard('JCB 15 digit',      prefix_jcb15, 15),
        'jcb16':        CreditCard('JCB 16 digit',      prefix_jcb16),
        'voyager':
'''