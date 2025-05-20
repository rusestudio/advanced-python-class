import json
from argparse import ArgumentParser
from typing import Any, Dict, List
from urllib.parse import quote
#can use sleep to slow down server req
#from time import sleep

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from trafilatura import extract, fetch_url

#fmt :off - can uuse to off format for unwanted format line
argparser = ArgumentParser("naver news crawling script")
argparser.add_argument("--query", type=str, help="crawling query")
argparser.add_argument("--date-start", type=str, help="date start", default="2025.04.07")
argparser.add_argument("--date-end",type=str, help="date end", default="2025.04.08")
#fmt : on

#date_start = "2025.04.07"
#date_end = "2025.04.08"
#query = "춘천시"
#query= quote(query)

def crawl_news(next_url: str)-> List[Dict[str, Any]]: #coz we dont know the type of dict
    news_data_list = []

    with tqdm() as progress_bar:
        while next_url:
            response = requests.get(next_url)
            #sleep(0.3) so sleep for a while after req in server

            response_data = json.loads(response.text)
            li_tags = response_data["collection"][0]["html"] #use[0] coz data in dict type so wanna get the first in list
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

            progress_bar.set_postfix({"num_articles": len(news_data_list)})
            progress_bar.update(1)

    return news_data_list #dict list data type



if __name__ == "__main__":

    args = argparser.parse_args()

    next_url=f"https://s.search.naver.com/p/newssearch/2/search.naver?cluster_rank=29&de={args.date_end}&ds={args.date_start}&field=0&is_dts=0&is_sug_officeid=0&mynews=0&office_category=0&office_section_code=0&office_type=0&pd=3&photo=0&{quote(args.query)}&rev=31&service_area=0&sort=0&spq=0&start=11&where=news_tab_api"

    news_data_list = crawl_news(next_url)

    with open("news_data.json", "w", encoding="utf-8") as f:
        json.dump(news_data_list, f, ensure_ascii=False)

#run isort to organize code
#black
#flake8

#crawling from mobile page can  be faster
#coz its small and compact for webpage info to be share