# 상대경로가 http://로 시작한다면 기본URL을 무시하고, 2번째 매개변수에 지정한 URL을 리턴
from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print( urljoin(base, "/hoge.html"))
print( urljoin(base, "http://otherExample.com/wiki"))
print( urljoin(base, "//anotherExample.com/test"))