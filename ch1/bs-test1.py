# 라이브러리 읽어 들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
  <h1>스크레이핑이란?</h1>
  <p>웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석하기
# BeautifulSoup 인스턴스 생성 
# 첫번째 매개변수 : HTML, 두번쨰 매개변수 : 분석기지정 HTML 분석 시에는 html.parser
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기
h1 = soup.html.body.h1 # <html><body><h1>에 있는 요소에 접근
p1 = soup.html.body.p # <p>가 2개 있는 경우 먼저 나오는 <p>의 것을 추출
# next_sibling에서는 </p>뒤의 줄바꿈 또는 공백이 추출
# next_sibling을 2번 사용해서 2번째 <p>를 추출
p2 = p1.next_sibling.next_sibling 

# 요소의 글자 출력하기
print("h1 = "+h1.string)
print("p = " +p1.string)
print("p = " +p2.string)