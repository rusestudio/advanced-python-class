import requests
import json
from bs4 import BeautifulSoup
from trafilatura import fetch_url, extract
from tqdm import tqdm

next_url="https://s.search.naver.com/p/newssearch/2/search.naver?cluster_rank=29&de=2025.04.08&ds=2025.04.07&eid=&field=0&force_original=&is_dts=0&is_sug_officeid=0&mynews=0&news_office_checked=&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22location_city%22%2C%22source%22%3A%22NLU%22%7D%2C%22sub%22%3A%5B%7B%22name%22%3A%22location%22%7D%5D%7D%7D&nso=%26nso%3Dso%3Ar%2Cp%3Afrom20250407to20250408%2Ca%3Aall&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&office_category=0&office_section_code=0&office_type=0&pd=3&photo=0&query=%EC%B6%98%EC%B2%9C%EC%8B%9C&query_original=&rev=31&service_area=0&sort=0&spq=0&start=11&where=news_tab_api&nso=so:r,p:from20250407to20250408,a:all"

news_data_list = []

for trial in tqdm(range(10)): #1-101
    response = requests.get(next_url)

    response_data = json.loads(response.text)
    li_tags = response_data["collection"][0]["html"]
    next_url = response_data["url"]

    li_tags = BeautifulSoup(li_tags, features="lxml")

    news_url_list=[]
    for li in li_tags.find_all("li",{"class":"bx"}):
        url= li.find("a",{"class":"news_tit"})["href"]
        news_url_list.append(url)

    for news_url in news_url_list:
        news_source = fetch_url(news_url_list[0])
        parsed_result= extract(news_source, with_metadata=True, output_format="json") #json string
        news_data = json.loads(parsed_result) #pass in json dict
        news_data_list.append(news_data)

with open("news_data.json", "w", encoding="utf-8") as f:
    json.dump(news_data_list, f, ensure_ascii=False)