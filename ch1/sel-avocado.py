from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

# CSS 선택자로 추출하기
# 모든 <li> 태그 중 8번쨰 요소를 추출
print(soup.select_one("li:nth-of-type(8)").string)
# 야채를 나타내는 id가 ve-list인 요소 바로 아래에 있는 <li>태그 중에서 4번째 요소를 추출하는 것
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
# select()를 이용해 id가 ve-list인 요소 바로 아래에 있는 <li>태그 중에서 data-lo속성이 "us"
# 인 것을 모두 추출하고 그 중 [1]인 요소를 추출(0부터 시작하므로 2번째)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

# find 메서드로 추출하기
cond = {"data-lo":"us", "class":"black"}
print(soup.find("li", cond).string)

# find 메서드를 연속적으로 사용하기
print(soup.find(id="ve-list").find("li", cond).string)