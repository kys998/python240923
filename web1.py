# web1.py

#크롤링 선언
from bs4 import BeautifulSoup

#html 파일 읽기
with open("Chap09_test.html", "r", encoding="utf-8") as f:
    html = f.read()

#html 문서를 파싱
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())

# 문서에 있는 모든 <p> 태그를 검색
# print(soup.find_all("p"))

# 첫번째 <p> 태그를 검색
# print(soup.find("p"))

# 첫번째 <p> 태그의 텍스트를 검색
# print(soup.find("p").text)

# 조건에 맞는 태그 검색
# print(soup.find_all("p", class_="outer-text"))

# 조건에 맞는 태그의 텍스트 검색
# print(soup.find_all('p', class_='outer-text'))


# 찾은 결과를 루프를 돌면서 출력
for tag in soup.find_all("p"):
    #태그 내부의 컨텐츠만 출력          
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

# 태그 속성 검색











