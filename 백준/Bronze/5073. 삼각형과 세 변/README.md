# [Bronze III] 삼각형과 세 변 - 5073 

[문제 링크](https://www.acmicpc.net/problem/5073) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

기하학, 구현, 수학

### 제출 일자

2025년 1월 5일 15:30:19

### 문제 설명

<p>삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.</p>

<ul>
	<li>Equilateral :  세 변의 길이가 모두 같은 경우</li>
	<li>Isosceles : 두 변의 길이만 같은 경우</li>
	<li>Scalene : 세 변의 길이가 모두 다른 경우</li>
</ul>

<p>단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.</p>

<p>세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.</p>

### 입력 

 <p>각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.</p>

### 출력 

 <p>각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.</p>

###  문제분석 & 이유
---
이번에는 세변의 길이로 삼각형 유효성 여부를 따지는 문제다.


###  Pseudo Code

---

```
무한 루프를 돌린다:
    세개의 변 길이를 동시에 받는다
    중단 여부를 검사한다
    
    3개의 변을 리스트에 넣고
    sort로 정리한다
    
    만약 가장 긴변의 길이가 나머지 변의 길이와 같거나 크다면
        Invalid를 출력한다
    아니면
        다 같으면
            Equilateral 출력
        두개만 같다면
            Isosceles 출력
        다 다르다면
            Scalene 출력
```


### 문제 해결 및 배운 점
---
삼각형의 가장 긴 변은 나머지 두개의 변보다 작아야한다. 
라는 조건을 까먹고 있었다.

### 최종 코드
---

```
while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break
    sides = [a1, a2, a3]
    sides.sort()  
    if sides[2] >= sides[0] + sides[1]:  
        print("Invalid")
    else:
        if a1 == a2 == a3:
            print("Equilateral")
        elif a1 == a2 or a1 == a3 or a2 == a3:
            print("Isosceles")
        else:
            print("Scalene")

```
