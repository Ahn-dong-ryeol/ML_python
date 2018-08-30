## id로 원하는 요소 찾기
# 라이브러리 읽어 들이기
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
  <h1 id="title">스크레이핑이란?</h1>
  <p id="body">웹 페이지를 분석하는 것</p>
  <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석하기
# BeautifulSoup 인스턴스 생성 
# 첫번째 매개변수 : HTML, 두번쨰 매개변수 : 분석기지정 HTML 분석 시에는 html.parser
soup = BeautifulSoup(html, 'html.parser')

# find() 메서드로 원하는 부분 추출하기
title = soup.find(id="title")
body = soup.find(id="body")

# 텍스트 부분 출력하기
print("#title=" + title.string)
print("#body=" + body.string)