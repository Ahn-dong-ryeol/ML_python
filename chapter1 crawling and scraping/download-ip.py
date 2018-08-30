# IP주소, UserAgent 등의 클라이언트 접속정보를 출력하는 "IP확인 API"에 접근해서 정보를 추출하는 프로그램
# 모듈 읽어들이기
import urllib.request

# 데이터 읽어들이기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리를 문자열로 변환하기(read()로 읽어들인 데이터는 바이너리이다.)
text = data.decode("utf-8")
print(text)