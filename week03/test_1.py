import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = requests.get("https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo", headers=headers)

# data를 html로 분리하기 편하게 만들어 줌.
bs = BeautifulSoup(data.text, 'html.parser')

# 순위숫자
# regularTeamRecordList_table > tr:nth-child(1) > th > strong

# team_NC
#팀이름
#regularTeamRecordList_table > tr:nth-child(1) > td.tm > div >span

rank_table = bs.select("#regularTeamRecordList_table > tr")
print(rank_table)

for rank in rank_table:
   # print(rank)
    team_rank = rank.select_one('th>strong').text
    #print(team_rank)
    team_name = rank.select_one('td.tm>div>span').text
    print(team_rank,team_name)

    