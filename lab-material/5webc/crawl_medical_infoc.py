import json
import re
from argparse import ArgumentParser, Namespace
from time import sleep
from typing import Dict, Union

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# fmt: off
argparse = ArgumentParser("서울대학교 의학정보 수집 스크립트입니다.")
argparse.add_argument("--output-path", type=str, default="medi_info.json", help="크롤링된 정보를 저장할 경로")
# fmt: on

ROOT_URL = "http://www.snuh.org/health/nMedInfo"


def crawl_single_page(page_url: str) -> Dict[str, Union[str, Dict]]:
    response = requests.get(page_url)
    sleep(0.3)
    soup = BeautifulSoup(response.text, features="lxml")

    title = soup.find("div", {"class": "viewTitle"}).text
    title = " ".join(title.split())

    medi_info_view = soup.find("div", {"class": "mediInfoView"})
    meta_info = {}

    for sub_info in medi_info_view.find("div", {"class": "clearFix"}).find_all(
        "div", {"class": "viewRow"}
    ):
        key = sub_info.find("em")
        span = key.find("span")
        if span:
            span.extract()

        value = sub_info.find("p")
        key = " ".join(key.text.split())
        value = " ".join(value.text.split())
        value = value.replace(" ,", ",")
        meta_info[key] = value

    detail_wrap = medi_info_view.find("div", {"class": "detailWrap"})
    keys = detail_wrap.find_all("h5")
    values = detail_wrap.find_all("p")
    detail_info = {}

    for key, value in zip(keys, values):
        key = " ".join(key.text.split())
        value = " ".join(value.text.split())
        detail_info[key] = value

    single_page_info = {
        "title": title,
        "meta_info": meta_info,
        "detail_info": detail_info,
    }

    return single_page_info


def crawl_medical_info_pages(args: Namespace):
    crawling_results = []
    
    # Instead of looping over all pages, crawl just the first page.
    current_page = 1
    
    # Construct the URL for the first page
    url = f"{ROOT_URL}/nList.do?pageIndex={current_page}"
    
    response = requests.get(url)
    sleep(0.3)
    soup = BeautifulSoup(response.text, features="lxml")
    
    titles = soup.find_all("div", {"class": "title"})
    for title in titles:
        sub_url = title.find("a")["href"]
        url = f"{ROOT_URL}/{sub_url}"
        single_page_info = crawl_single_page(url)
        crawling_results.append(single_page_info)
    
    # Save the results to a JSON file
    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(crawling_results, f, ensure_ascii=False, indent=2)

    print(f"Data from {current_page} page has been crawled and saved.")

if __name__ == "__main__":
    args = argparse.parse_args()

    crawl_medical_info_pages(args)
