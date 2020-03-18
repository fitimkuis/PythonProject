from faker import Faker

fake = Faker()
print("the card number: "+fake.credit_card_number(card_type=None)) #  the card number

print(fake.credit_card_provider(card_type=None)) #  card provider )

print("VISA 13 digit: "+fake.credit_card_number(card_type='visa13')) #  card provider )

print("VISA 16 digit: "+fake.credit_card_number(card_type='visa16'))


'''
        'maestro':      CreditCard('Maestro',           prefix_maestro, 12, security_code='CVV'),
        'mastercard':   CreditCard('Mastercard',        prefix_mastercard, 16, security_code='CVV'),
        'visa16':       CreditCard('VISA 16 digit',     prefix_visa),
        'visa13':       CreditCard('VISA 13 digit',     prefix_visa, 13),
        'amex':         CreditCard('American Express',  prefix_amex, 15, security_code='CID', security_code_length=4),
        'discover':     CreditCard('Discover',          prefix_discover),
        'diners':       CreditCard('Diners Club / Carte Blanche', prefix_diners, 14),
        'jcb15':        CreditCard('JCB 15 digit',      prefix_jcb15, 15),
        'jcb16':        CreditCard('JCB 16 digit',      prefix_jcb16),
        'voyager':      CreditCard('Voyager',           prefix_voyager, 15),
'''