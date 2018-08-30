## 여러 개의 태그를 한 번에 추출하고 싶을 때는 find_all() 메서드 사용
from bs4 import BeautifulSoup
html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a><li>
    </ul>
</body></html>
"""

# html 분석하기 - BeautifulSoup 인스턴스 생성
soup = BeautifulSoup(html, 'html.parser')

# find_all() 메서드로 추출하기 - find_all()를 이용해 모든 <a>태그 추출
links = soup.find_all("a")

# 링크 목록 출력하기 추출한 모든 요소를 for구문으로 반복처리한다.
# 링크의 href 속성은 attrs['href']처럼 attrs속성에서 추출한다.
# 내부 텍스트는 string속성으로 추출한다.
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text,">",href)

