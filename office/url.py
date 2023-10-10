from random import choice


def from_example_to_email(mail):
    return mail.split('@')[0]+'@'+choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'yandex.ru', 'mail.ru', 'bk.ru'])