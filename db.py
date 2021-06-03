import sqlite3

# connect to database
conn = sqlite3.connect('contactbook.db')

# create a cursor
c = conn.cursor()

# create table
c.execute(""" CREATE TABLE IF NOT EXISTS contacts_book (
                                        number integer,
                                        name text
                                    ); """)


def save(pn, nm):
    c.execute("""INSERT INTO contacts_book(number,name) VALUES(?,?);
 """, (pn, nm))
    print('contact has been succesfully saved')
    conn.commit()


def find(nm):
    c.execute("""
    SELECT number FROM contacts_book WHERE name = (?);
    """, [nm])
    data = c.fetchall()
    print(data)
    conn.commit()


def delete(nm):
    c.execute("""
       SELECT number FROM contacts_book WHERE name = (?);
       """, [nm])
    data = c.fetchall()
    if len(data) > 0:
        c.execute("""
                       DELETE FROM contacts_book WHERE name = (?);
                       """, [nm])
        print('number deleted')
    else:
        print('contact is not present')
    conn.commit()


def update(nm, npn):
    c.execute("""UPDATE contacts_book SET number= ? WHERE name=?; """, (npn, nm))
    conn.commit()
    print('contact updated')
