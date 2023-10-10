import faker, random

from db import DataBase
from url import *


def main():
    sql = DataBase(db_config)

    fake = faker.Faker(locale="ru_RU")

    lim = int(input('>>> '))
    i = 0

    while True:

        if i == lim:
            break

        company_name = fake.company()
        company_ceo = fake.name()
        company_phone = fake.phone_number()
        company_email = fake.email()
        office_address = fake.address()

        sql.insert_company(company_name, company_ceo, company_email, company_phone)
        sql.insert_office(office_address, company_ceo, company_email, company_phone)
        sql.update_main_office_id()

        print(f"Company name: {company_name}, company_ceo: {company_ceo}")

        for _ in range(int(random.randint(0, 10)**2)):

            office_address = fake.address()
            office_ceo = fake.name()
            office_phone = fake.phone_number()
            office_email = fake.email()

            sql.insert_office(office_address, office_ceo, office_email, office_phone)
            print(f"Office address: {office_address}, office_ceo: {office_ceo}")

        i += 1


if __name__ == '__main__':
    main()
