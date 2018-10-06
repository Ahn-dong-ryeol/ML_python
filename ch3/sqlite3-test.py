import sqlite3

# sqlite 데이터베이스 연결하기
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블 생성하고 데이터 넣기
cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items(name, price) VALUES ('Apple',800);
INSERT INTO items(name, price) VALUES ('Orange',780);
INSERT INTO items(name, price) VALUES ('Banana',430);
""")

conn.commit()
# DB를 조작하는 커서를 추출
cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items") # execute() : 1줄 명령, executescript() : 여러 줄의 명령
item_list = cur.fetchall() # fetchall : 모든 행 추출, fetchone : 1개 행 추출

for it in item_list:
    print(it)