from selenium import webdriver

url = "https://nid.naver.com/nidlogin.login"
# PhantomJS 드라이버 추출하기 --- (※1)
browser = webdriver.PhantomJS()

# 3초 대기하기 --- (※2)
browser.implicitly_wait(3)

# 로그인
# URL 읽어 들이기 --- (※3)
browser.get(url)
element_id = browser.find_element_by_id("id") # 아이디 텍스트 입력상자
element_id.clear() #텍스트 상자 내 입력된 글자 삭제
element_id.send_keys("sasa2982")
element_pw = browser.find_element_by_id("pw") # 아이디 텍스트 입력상자
element_pw.clear() #텍스트 상자 내 입력된 글자 삭제
element_pw.send_keys("dksehdfuf13579")

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()
browser.save_screenshot("Website_C.png")
# 메일 페이지 열기
browser.get("https://mail.naver.com")
browser.save_screenshot("Website_D.png")
titles = browser.find_elements_by_css_selector("strong.mail_title")
for title in titles:
    print("-", title.text)

# 브라우저 종료하기 --- (※5)
browser.quit()
# --> 모든 웹 사이트에서 캡쳐 가능