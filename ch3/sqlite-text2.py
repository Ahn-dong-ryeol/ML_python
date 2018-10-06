import sqlite3

# 데이터베이스 연결하기
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

# 테이블 생성하기
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name    TEXT,
    price   INTEGER
    )
""")
conn.commit()

# 데이터 넣기
cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name, price) VALUES (?,?)", ("Orange", 5200)
)
conn.commit()

# 여러 데이터 연속으로 넣기
cur = conn.cursor()
data = [
    ("mango",7700),
    ("kiwi",4000),
    ("Grape",8000),
    ("Peach",9400),
    ("persimmon",7000),
    ("banana",4000)
]
cur.executemany(
    "INSERT INTO items(name, price) VALUES (?,?)", data
)

conn.commit()

cur = conn.cursor()
price_range = (4000,7000)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?", price_range
)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)