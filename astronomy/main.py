from astroquery.simbad import Simbad

# Расширяем стандартный вывод SIMBAD, включая ID GAIA
Simbad.add_votable_fields("ids")

# Ищем звезду по популярному имени
result = Simbad.query_object("Sirius")

if result:
    print("Результат поиска в SIMBAD:")
    print(result)
else:
    print("Звезда 'Sirius' не найдена в базе SIMBAD.")
