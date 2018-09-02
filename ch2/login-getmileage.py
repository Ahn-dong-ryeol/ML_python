# 로그인을 위한 모듈 추출하기
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호 지정하기
USER = "sasa2982"
PASS = "zx12qwas"

# 세션 시작하기
session = requests.session() # requests.session을 이용하면 쿠키를 사용하는 회원제 사이트에 로그인 가능
#로그인하기 - 이전에 입력한 id, password를 이용해 로그인
login_info = {
    "m_id": USER,
    "m_passwd" : PASS
}
# 로그인 전용 URL에 POST요청을 수행
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 로그인이 완료되면, 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기 - 마이페이지의 내용 출력
soup = BeautifulSoup(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지 : "+mileage)
print("이코인 : "+ecoin)