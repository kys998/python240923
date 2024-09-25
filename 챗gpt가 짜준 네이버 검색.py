# 네이버에서 반도체 검색하는 url 에서 제목만 크롤링 하는 프로그램 짜줘 
# 위에 크롤링한 결과를 relust.xlsx로 저장하도록 코드를 수정해줘.
# 
# 

import requests
from bs4 import BeautifulSoup
import openpyxl

# 검색어와 검색 URL
query = "반도체"
url = f"https://search.naver.com/search.naver?query={query}"

# 네이버에서 검색 결과 페이지 가져오기
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url, headers=headers)

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "News 크롤링"

# 첫 번째 행에 헤더 추가
ws.append(["No.", "Title"])

# 응답이 성공적으로 왔는지 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 검색 결과에서 제목 추출 (네이버 뉴스 섹션의 제목들)
    titles = soup.select("a.news_tit")

    # 제목 엑셀 파일에 저장
    for i, title in enumerate(titles, 1):
        ws.append([i, title.get_text()])

    # 엑셀 파일 저장
    wb.save("result.xlsx")
    print("result.xlsx 파일이 생성되었습니다.")
else:
    print(f"Error: {response.status_code}")
