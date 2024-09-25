# web2.py

import requests
from bs4 import BeautifulSoup

url = "http://www.daangn.com/fleamarket"
response = requests.get(url)

# 검색이 용이한 객체로 만들기
soup = BeautifulSoup(response.text, "html.parser")

# 상단의 <div> 태그를 모두 검색
# 파일로 저장
f = open("daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    regionElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    region = regionElem.text.strip()

    #f-string 포매팅
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")
f.close()


# <div class="card-photo ">
#         <img alt="아이폰 14 128GB" src="https://img.kr.gcp-karroter.net/origin/article/202409/ac86e73581aa8fa836a22091549d35890569c482370b28626c1eb50afd578233_0.webp?f=webp&amp;q=82&amp;s=300x300&amp;t=crop" />
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">아이폰 14 128GB</h2>
#       <div class="card-price ">
#         600,000원
#       </div>
#       <div class="card-region-name">
#         전남 순천시 용당동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 7
#           </span>
#         ∙
#         <span>
#             채팅 62
#           </span>
#       </div>
#     </div>