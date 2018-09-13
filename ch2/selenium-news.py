from selenium import webdriver

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기
url_login = "https://news.naver.com/main/ranking/popularDay.nhn"
browser.get(url_login)
print("뉴스 페이지에 접근합니다.")

# 쇼핑목록가져오기
for no in 1,2:
    news = browser.find_elements_by_class_name("ranking_section")
    seqno=1
    for seqno in 1,2,3,4,5:
        print("-", browser.find_elements_by_class_name("num",seqno).text)
        seqno+=1
        
