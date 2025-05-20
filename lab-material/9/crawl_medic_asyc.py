import json
import re
from argparse import ArgumentParser, Namespace
from time import sleep
from typing import Dict, Union

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm import tqdm

# fmt: off
argparse = ArgumentParser("서울대학교 의학정보 수집 스크립트입니다.")
argparse.add_argument("--output-path", type=str, default="medi_info.json", help="크롤링된 정보를 저장할 경로")
# fmt: on

ROOT_URL = "http://www.snuh.org/health/nMedInfo"

#change def to corutine 
#if use client session- it keep the same session when request, doesnt need to request many times
async def fetch_url(session: aiohttp.ClientSession, url: str)-> str:
    async with session.get(url) as response:
        return await response.text() 


async def crawl_single_page(session: aiohttp.ClientSession, page_url: str) -> Dict[str, Union[str, Dict]]:
    response = await fetch_url(session, page_url)
    sleep(0.3)
    soup = BeautifulSoup(response, features="lxml")

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



async def crawl_medical_info_pages(args: Namespace):
    crawling_results = []

    current_page = 1

    async with aiohttp.ClientSession() as session:
        with tqdm() as progress_bar:
            while True:
                response = await fetch_url(session, f"{ROOT_URL}/nList.do?pageIndex={current_page}")
                sleep(0.3)
                soup = BeautifulSoup(response, features="lxml")

                titles = soup.find_all("div", {"class": "title"})
                urls = []
                for title in titles:
                    sub_url = title.find("a")["href"]
                    url = f"{ROOT_URL}/{sub_url}"
                    urls.append(url)

                coroutines = [crawl_single_page(url) for url in urls]
                results = await asyncio.gather(*coroutines)
                crawling_results.extend(results)

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

    asyncio.run(crawl_medical_info_pages(args))
