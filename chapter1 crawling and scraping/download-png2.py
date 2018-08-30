import urllib.request

#url과 저장경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
# urlopen()으로 png파일의 URL리소스를 연다.
# read() 메소드로 데이터를 읽어들인다.
mem = urllib.request.urlopen(url).read() 

# open()함수로 파일을 연다. mode는 wb(w:쓰기, b:바이너리)
# write()함수로 다운받은 바이너리 데이터를 파일에 저장한다.
with open(savename, mode="wb") as f :
    f.write(mem)
    print("저장되었습니다.")