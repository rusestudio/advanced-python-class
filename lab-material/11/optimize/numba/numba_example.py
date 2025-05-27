import time

import numba


# 순수 파이썬으로 소수 판별 함수
def is_prime_python(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # 3부터 sqrt(num)까지 홀수만 확인
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


# 순수 파이썬으로 주어진 범위까지 소수 개수 세기
def count_primes_python(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime_python(i):
            count += 1
    return count


# Numba를 사용하여 소수 판별 함수 가속
@numba.njit
def is_prime_numba(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # 3부터 sqrt(num)까지 홀수만 확인 (Numba는 math.sqrt를 지원)
    i = 3
    # Numba에서는 while 조건에 부동소수점 연산 사용 시 주의 필요.
    # 정수 곱셈으로 변경하는 것이 더 안정적일 수 있습니다. i <= int(num**0.5) 대신 i * i <= num 사용
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


# Numba를 사용하여 주어진 범위까지 소수 개수 세기 가속
@numba.njit
def count_primes_numba(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime_numba(i):  # Numba 컴파일된 함수 내부에서 다른 Numba 함수 호출
            count += 1
    return count


# 테스트 범위 설정
limit = 10000000  # 10만까지의 소수 개수 세기

print(f"주어진 범위: 2부터 {limit}까지")

# Numba 함수 실행 시간 측정
start_time = time.time()
numba_count = count_primes_numba(limit)
end_time = time.time()
print(f"Numba 소수 개수 세기 실행 시간: {end_time - start_time:.6f} 초 (개수: {numba_count})")

# 순수 파이썬 함수 실행 시간 측정
start_time = time.time()
python_count = count_primes_python(limit)
end_time = time.time()
print(f"순수 파이썬 소수 개수 세기 실행 시간: {end_time - start_time:.6f} 초 (개수: {python_count})")

# 결과 비교
print(f"결과 일치 여부: {numba_count == python_count}")
