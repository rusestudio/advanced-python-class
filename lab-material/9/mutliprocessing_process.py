import os
from argparse import ArgumentParser
from functools import partial
from multiprocessing import Process
from random import Random
from typing import Dict, List

import ujson
from loguru import logger
from tqdm import tqdm

argparser = ArgumentParser(description="데이터 정제 예시")
argparser.add_argument("--input-path", type=str, default="medical_info.json")
argparser.add_argument("--output-dir", type=str, default="output")
argparser.add_argument("--num-processes", type=int, default=8)
argparser.add_argument("--seed", type=int, default=42)


def process_data(process_id: int, data: List[Dict[str, str]], output_dir: str = "output"):
    logger.info(f"Process {process_id} started processing {len(data)} items.")

    output = []

    # 첫번째 프로세스에서만 tqdm을 사용하여 진행 상황을 표시
    with tqdm(
        total=len(data),
        desc=f"Process {process_id}",
        disable=False if process_id == 0 else True,
        mininterval=1,
    ) as pbar:
        for item in data:
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

            output.append(document_string)
            pbar.update(1)

    logger.info(f"Process {process_id} finished processing {len(data)} items.")
    with open(os.path.join(output_dir, f"result-{process_id:02d}.txt"), "w", encoding="utf-8") as f:
        for item in output:
            f.write(item + "\n\n")


if __name__ == "__main__":
    args = argparser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_path, "r", encoding="utf-8") as f:
        data = ujson.load(f)

    data = data * 1000  # 데이터 양을 늘리기 위해 복사
    # 특정 프로세스에 너무 많은 데이터가 할당되지 않도록 섞기 (밸런싱 위해)
    Random(args.seed).shuffle(data)

    # 데이터를 프로세스 수에 맞게 나누기
    chunks = [data[i :: args.num_processes] for i in range(args.num_processes)]

    process_data_with_default_args = partial(process_data, output_dir=args.output_dir) #tie up function with many agrument

    processes = []
    for i in range(args.num_processes): #default 4
        process = Process(target=process_data_with_default_args, args=(i, chunks[i]))
        processes.append(process)     #main (parent) process have child process.
        process.start()               #after each child process finish it wait. then go to join
                                     #process more faster than pool, coz it send all data direct but pool it find the rest process in pool and use it

    for process in processes:
        process.join()

    logger.info("모든 프로세스가 완료되었습니다.")

