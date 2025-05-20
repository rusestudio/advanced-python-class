import json
import re
from argparse import ArgumentParser, Namespace
from time import sleep
from typing import Dict, Union
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# fmt: off
argparse = ArgumentParser("서울대학교 의학정보 수집 스크립트입니다.")
argparse.add_argument("--output-path", type=str, default="medi_info.json", help="크롤링된 정보를 저장할 경로")
argparse.add_argument("--num-processes", type=int, default=8, help="parallel proccess number")
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

    current_page = 1
    with tqdm() as progress_bar:
        while True:
            response = requests.get(f"{ROOT_URL}/nList.do?pageIndex={current_page}")
            sleep(0.3)
            soup = BeautifulSoup(response.text, features="lxml")

            titles = soup.find_all("div", {"class": "title"})
            url_list =[]
            for title in titles:
                sub_url = title.find("a")["href"]
                url = f"{ROOT_URL}/{sub_url}"
                url_list.append(url)

            #crawlmanyargs = partial(crawl_single_page,a=10,b=5) #mul import from functool import partial
        
            #use multiprocess instead of if loop
            with Pool(args.num_processes) as pool:
                for result in pool.imap_unordered(crawl_single_page,url_list, chunksize=10):
                    #if crawlpage have many argument use function partial
                    #...imap_unordered(crawlmanyargs, url_list)
                    crawling_results.append(result)

            next_page = soup.find("a", {"class": "nextBtn"})["href"]
            next_page = re.search(r"\((\d+)\)", next_page).group(1)
            next_page = int(next_page)

            progress_bar.set_postfix({"num_medical_info": len(crawling_results)})

            if current_page == next_page:
                break

            progress_bar.update(1)
            current_page += 1

    with open(args.output_path, "w", encoding="utf-8") as f:
        json.dump(crawling_results, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    args = argparse.parse_args()

    crawl_medical_info_pages(args)
