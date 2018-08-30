# books.html을 10가징 방법으로 원하는 태그를 추출하기
from bs4 import BeautifulSoup
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSS 선택자로 검색하는 방법
sel = lambda q : print(soup.select_one(q).string)
sel("#nu") # id로 추출하기
sel("li#nu") # id로 추출하는데, <li>태그라는 것을 추가
sel("ul > li#nu") # <lu>의 자식이라는 것을 추가
sel("#bible #nu") # id속성을 이용해 #bible아래의 #nu를 선택하게 한 것
sel("#bible > #nu") # 위 방법에서 태그들이 직접적인 부모자식 관계를 가지고 있다는 것을 나타냄
sel("ul#bible > li#nu") # id가 bible인 <ul>태크 바로 아래에 있는 id가 nu인 <li>태그를 선택하는 것
sel("li[id='nu']") # 속성 검색을 이용해 id가 nu인 <li>태그를 지정하는 것
sel("li:nth-of-type(4)") # 4번째 <li>태그를 추출하는 것

# 그 밖의 방법
print(soup.select("li")[3].string) # select()을 이용해 <li>태그를 모두 추출하고, 3번째(0부터 4번째)
print(soup.find_all("li")[3].string) # find_all()을 이용해 <li>태그를 모두 추출하고, 3번째(0부터 4번째)