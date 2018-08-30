# <a> 태그가 상대 경로로 주어졌을 떄, 절대경로로 변환하기
from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print( urljoin(base, "b.html"))
print( urljoin(base, "sub/c.html") )
print( urljoin(base, "../index.html") )
print( urljoin(base, "../img/hoge.png") )
print( urljoin(base, "../css/hoge.css") )
