import json
from argparse import ArgumentParser
from time import sleep
from typing import Dict, Union

import requests
from bs4 import BeautifulSoup
from tqdm import Tqdm

#fmt: off #no format for code between off n on
argparse = ArgumentParser()
argparse.add_argument("")
#fmt: on

ROOT_URL = "http://www.snuh.org/health/nMedInfo"

def crawl_single_page(page_url: str) -> Dict[str, Union[str, Dict]]:
    response = requests.get(page_url)
    sleep(0.3)
    soup = BeautifulSoup(response.text, features="lxml")

    # get title
    title = soup.find("div", {"class": "viewTitle"}).text
    title = " ".join(title.split())  # remove all space or \n

    medi_info_view = soup.find("div", {"class": "mediInfoView"})
    meta_info = {}  # save in dict

    for sub_info in medi_info_view.find("div", {"class": "clearFix"}).find_all(
        "div", {"class": "viewRow"}
    ):
        key = sub_info.find("em")
        span = key.find("span")
        if span:
            span.extract()  # to remove span that have unwanted text ,use extract to remove that text

        value = sub_info("p")
        key = " ".join(key.text.split())
        value = " ".join(value.text.split())
        value = value.replace(" ,", ",")
        meta_info[key] = value  # put data in dict

    # get explaination detail
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


def crawl_medical_info_pages():
    crawling_results = []

    current_page = 1

    with tqdm() as progress_bar:
        while True:
            response = requests.get(f"{ROOT_URL}/nList.do?pageIndex={current_page}")
            sleep(0.3)
            soup = BeautifulSoup(response.text, features="lxml")

            titles = soup.find_all("div", {"class": "title"})
            for title in titles:
                sub_url = title.find("a")["href"]
                url = f"{ROOT_URL}/{sub_url}"
                single_page_info = crawl_single_page(url)
                crawling_results = crawling_results.append(single_page_info)

            next_page = soup.find("a", {"class": "nextBtn"})[
                "href"
            ]  # get page number in link
            next_page = re.search(r"\((\d+)\)", next_page).group(
                1
            )  # get only number without ()
            next_page = int(next_page)  # change the strin to int

            progress_bar.set_postfix({"num_medical_info": len(crawling_results)})

            if current_page == next_page:  # to get all page
                # if current page same with next page means it reach the last page already
                break
                # else increase the to next page
            progress_bar.update(1)
            current_page += 1

    with open("medi_info.json", "w", encoding="utf-8") as f:
        json.dump(crawling_results, f, ensure_ascii=False, indent=2)


if __name__("__main__"):
    crawl_medical_info_pages()
