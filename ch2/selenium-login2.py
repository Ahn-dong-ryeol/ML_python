from selenium import webdriver
USER="sasa2982"
PASS="dksehdfuf13579"

# PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 로그인 페이지에 접근하기
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")
browser.save_screenshot("Website_login_20180903.png")
# 텍스트 박스에 아이디와 비밀번호 입력하기
element_id = browser.find_element_by_id("id") # 아이디 텍스트 입력상자
element_id.clear() #텍스트 상자 내 입력된 글자 삭제
element_id.send_keys("sasa2982")
element_pw = browser.find_element_by_id("pw") # 아이디 텍스트 입력상자
element_pw.clear() #텍스트 상자 내 입력된 글자 삭제
element_pw.send_keys("dksehdfuf13579")

# 입력양식 전송해서 로그인하기
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

# 쇼핑페이지의 데이터 가져오기
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
browser.save_screenshot("Website_20180903.png")
# 쇼핑목록가져오기
products = browser.find_elements_by_css_selector(".p_info span")
#print(products)
seqno=1
for product in products:
    print(seqno,"-", product.text)
    seqno+=1
    
