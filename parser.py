import sqlite3 as sq


# eng_name, rus_name, date_zodiac, mini_info, temperament, jobs
def return_dict():
    with open('db.txt') as f:
        s = f.read().split('@')
        s = [x.split('*')[1:] for x in s]
        s = [{'eng_name': x[0][:-1],
              'rus_name': x[1][:-1],
              'date_zodiac': x[2][:-1],
              'mini_info': x[3][:-1],
              'temperament': x[4][:-1],
              'jobs': x[5][:-1]
              } for x in s]
    return s


def create_table():
    with sq.connect('zodiac.db') as connection:
        cur = connection.cursor()
        cur.execute("""DROP TABLE If EXISTS zodiacs""")
        cur.execute("""CREATE TABLE IF NOT EXISTS zodiacs (
            eng_name TEXT,
            rus_name TEXT,
            date_zodiac TEXT,
            mini_info TEXT,
            temperament TEXT,
            jobs TEXT
            )""")


def insert_table():
    with sq.connect('zodiac.db') as connection:
        cur = connection.cursor()
        for d in return_dict():
            request = f"""INSERT INTO zodiacs VALUES ('{d["eng_name"]}', '{d["rus_name"]}', '{d['date_zodiac']}', '{d['mini_info']}', '{d['temperament']}', '{d['jobs']}')"""
            cur.execute(request)


if __name__ == "__main__":
    create_table()
    insert_table()
