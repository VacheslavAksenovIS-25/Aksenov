# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения товаров на оптовой базе. Таблица Товары должна
# содержать следующие данные: Код товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.

import sqlite3 as sq
from data_items import info_items

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS items')
    cur.execute('''CREATE TABLE IF NOT EXISTS items (
                item_id INTEGER  PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                shop_name TEXT NOT NULL,
                store_request INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit TEXT NOT NULL,
                wholesale_price REAL NOT NULL  )''')

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.executemany('INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?)', info_items)

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute("INSERT INTO items VALUES (8,'Чай', 'Ашан', 60, 320, 'гр', 169.50)")

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute("INSERT INTO items VALUES (NULL,'Кофе', 'Ашан', 50, 312, 'гр', 239.50)")

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('SELECT * FROM items')
    result = cur.fetchall()
    for i in result:
       print(i)

print('\n')

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('SELECT item_id, item_name, shop_name FROM items')
    result = cur.fetchall()
    for i in result:
       print(i)

print('\n')

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('SELECT * FROM items WHERE quantity >= 300 ORDER BY item_id DESC')
    result = cur.fetchall()
    for i in result:
        print(i)


with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('UPDATE items SET  wholesale_price = 219.50 WHERE item_name LIKE "Сыр"')
    result = cur.fetchall()
    for i in result:
        print(i)

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('DELETE FROM items WHERE shop_name LIKE "Пятёрочка"')

with sq.connect('wholesale_base.db') as con:
    cur = con.cursor()
    cur.execute('DELETE FROM items WHERE store_request > 15 and store_request < 45')


