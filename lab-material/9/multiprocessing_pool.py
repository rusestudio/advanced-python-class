import os
from argparse import ArgumentParser
from multiprocessing.pool import Pool
from random import Random
from typing import Dict

import ujson
from loguru import logger
from tqdm import tqdm

argparser = ArgumentParser(description="데이터 정제 예시")
argparser.add_argument("--input-path", type=str, default="medical_info.json")
argparser.add_argument("--output-dir", type=str, default="output")
argparser.add_argument("--num-processes", type=int, default=4)
argparser.add_argument("--chunk-size", type=int, default=100)
argparser.add_argument("--seed", type=int, default=42)


def process_data(item: Dict[str, str]):
    title = item["title"]
    title = " ".join(title.split())
    meta_info = item["meta_info"]
    detail_info = item["detail_info"]

    document_string = f"제목: {title}\n\n"

    document_string += "상세 정보:\n"
    for key, value in meta_info.items():
        key = " ".join(key.split())
        value = " ".join(value.split())
        document_string += f"{key}: {value}\n"

    document_string += "\n\n상세 정보:\n"
    for key, value in detail_info.items():
        key = " ".join(key.split())
        value = " ".join(value.split())
        document_string += f"{key}: {value}\n"

    return document_string   #can return easily use pool


if __name__ == "__main__":
    args = argparser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_path, "r", encoding="utf-8") as f:
        data = ujson.load(f)

    data = data * 1000  # 데이터 양을 늘리기 위해 복사
    # 특정 프로세스에 너무 많은 데이터가 할당되지 않도록 섞기 (밸런싱 위해)
    Random(args.seed).shuffle(data)

    results = []
    with tqdm(total=len(data), desc="Processing", mininterval=1) as pbar:
        with Pool(args.num_processes) as pool: #default =4
            for result in pool.imap_unordered(process_data, data, chunksize=args.chunk_size):#default 100
                results.append(result)
                pbar.update(1)

    with open(os.path.join(args.output_dir, "result.txt"), "w", encoding="utf-8") as f:
        for item in results:
            f.write(item + "\n\n")

    logger.info("Processing completed!")
