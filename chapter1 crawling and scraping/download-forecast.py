# URL에 매개변수를 추가해 요청을 전송하는 방법
# 기상청에 지역코드를 매개변수로 보내서 해당 지역의 날씨정보 수집
import urllib.request
# 파이썬으로 요청전용 매개변수를 만들 때는 urllib.parse모듈의 urlencode()함수를 이용해 URL인코딩을 한다.
import urllib.parse 
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL인코딩한다.
values = {
        'stnId': '109'
}
params = urllib.parse.urlencode(values)

# 요청 전용 URL을 생성한다.
url = API + "?" + params
print("url=",url)

# 다운로드 한다.
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)