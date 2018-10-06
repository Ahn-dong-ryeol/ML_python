import pandas as pd

# 엑셀 파일 읽기
filename = "stat_104102.xlsx"
sheet_name = "stat_104102"
book = pd.read_excel(filename, sheet_name=sheet_name, header=1)

# 2015년 인구로 정렬
book = book.sort_values(by=2015, ascending=False)
print(book)