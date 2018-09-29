import openpyxl

# 엑셀 파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨앞 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[10].value
    ])

# 필요없는 줄(헤더, 연도, 계) 제거
del data[0]
del data[0]
del data[0]
del data[-1]
del data[-1]

for i in range(len(data)):
    data[i][1]=int(data[i][1].replace(',',''))

# 데이터를 인구 순서로 정렬
data = sorted(data, key=lambda x:x[1], reverse=True)

# 하위 5위를 출력
for i, a in enumerate(data):
    if (i < 9): 
        print(i+1, "",a[0], a[1])
    else:
        print(i+1, a[0], a[1])
    