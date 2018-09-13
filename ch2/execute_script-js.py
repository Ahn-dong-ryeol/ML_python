from selenium import webdriver

# phantomJS 드라이버 추출하기
brower = webdriver.PhantomJS()
brower.implicitly_wait(3)

# 적당한 웹 페이지 열기
brower.get("https://google.com")

# 자바스크립트 실행하기
r = brower.execute_script("return 100+50")
print(r)
