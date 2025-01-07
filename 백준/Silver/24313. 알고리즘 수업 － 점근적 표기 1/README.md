# [Silver V] 알고리즘 수업 - 점근적 표기 1 - 24313 

[문제 링크](https://www.acmicpc.net/problem/24313) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

수학

### 제출 일자

2025년 1월 7일 01:26:01

### 문제 설명

<p>오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>알고리즘의 소요 시간을 나타내는 O-표기법(빅-오)을 다음과 같이 정의하자.</p>

<p>O(<em>g</em>(<em>n</em>)) = {<em>f</em>(<em>n</em>) | 모든 <em>n</em> ≥ <em>n<sub>0</sub></em>에 대하여 <em>f</em>(<em>n</em>) ≤ <em>c</em> × <em>g</em>(<em>n</em>)인 양의 상수 <em>c</em>와 <em>n<sub>0</sub></em>가 존재한다}</p>

<p>이 정의는 실제 O-표기법(<a href="https://en.wikipedia.org/wiki/Big_O_notation">https://en.wikipedia.org/wiki/Big_O_notation</a>)과 다를 수 있다.</p>

<p>함수 <em>f</em>(<em>n</em>) = <em>a<sub>1</sub>n </em>+ <em>a<sub>0</sub></em>, 양의 정수 <em>c</em>, <em>n<sub>0</sub></em>가 주어질 경우 O(<em>n</em>) 정의를 만족하는지 알아보자.</p>

### 입력 

 <p>첫째 줄에 함수 <em>f</em>(<em>n</em>)을 나타내는 정수 <em>a<sub>1</sub></em>, <em>a</em><sub><em>0</em></sub>가 주어진다. (0 ≤ |<em>a<sub>i</sub></em>| ≤ 100)</p>

<p>다음 줄에 양의 정수 <em>c</em>가 주어진다. (1 ≤ <em>c</em> ≤ 100)</p>

<p>다음 줄에 양의 정수 <em>n<sub>0</sub></em>가 주어진다. (1 ≤ <em>n<sub>0</sub></em> ≤ 100)</p>

### 출력 

 <p><em>f</em>(<em>n</em>), <em>c</em>, <em>n<sub>0</sub></em>가 O(<em>n</em>) 정의를 만족하면 1, 아니면 0을 출력한다.</p>

###  문제분석 & 이유
---
빅오 표기법에 대해 물어보는 문제이다. 

O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}

라는 전제인데, n0보다 큰 모든 n에 대해서 f(n) <= c * g(n) 을 만족해야한다. 
하지만 모든 n0보다 큰 모든 n을 확인할수없으므로 어느정도의 범위를 잡고 시험한다.


###  Pseudo Code

---

```
a1과 a0를 받는다
c를 받는다
n0를 받는다

condition을 flag로 둔다.

범위를 n0~n0+1000으로 두고 테스트를 한다.
만약 조건에 부합하지 않는다면 flag를 False로 바꾼다.

모든 검사가 끝나고도 condition이 True라면 1을 출력하고
아니라면 0을 출력한다.
```


### 문제 해결 및 배운 점
---
빅오표기법의 범위를 임의로 설정하는 크기를 고민했다.
1000 정도면 충분한 것같다.

### 최종 코드
---

```
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

condition = True

for n in range(n0, 1001):
    if a1*n + a0 > c * n :
        condition = False
        break

if condition :
    print(1)
else :
    print(0)
```
