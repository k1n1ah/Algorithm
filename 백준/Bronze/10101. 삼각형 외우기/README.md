# [Bronze IV] 삼각형 외우기 - 10101 

[문제 링크](https://www.acmicpc.net/problem/10101) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

기하학, 구현

### 제출 일자

2025년 1월 5일 15:21:08

### 문제 설명

<p>창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.</p>

<p>삼각형의 세 각을 입력받은 다음, </p>

<ul>
	<li>세 각의 크기가 모두 60이면, Equilateral</li>
	<li>세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles</li>
	<li>세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene</li>
	<li>세 각의 합이 180이 아닌 경우에는 Error</li>
</ul>

<p>를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.</p>

### 출력 

 <p>문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.</p>

###  문제분석 & 이유
---

3각의 합을 구하여 원하는 조건에 맞게 출력하는 문제이다
어떠한 순서로 적어야 else로 넘어갔을때 원하는 조건으로 출력될지
순서를 따져볼수있는지 물어보는 문제같다.

###  Pseudo Code

---

```
각 줄에 3개의 입력을 받는다

합이 180도에 해당하고
    각도가 60도로 같다면
        equilateral을 출력
    두개의 각만 같다면
        Isosceles를 출력
    다 다르다면
        Scalene을 출력
180도가 아니라면
    Error를 출력
```


### 문제 해결 및 배운 점
---
처음에는 != 180을 최상위 조건으로 뒀다가 == 180으로 바꿨다.
걸러지는 순서에 좀 더 집중을 해야한다.

### 최종 코드
---

```
a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 + a2 + a3 == 180 :
    if a1 == a2 == a3 == 60 :
        print("Equilateral")
    elif a1 == a2 or a2 == a3 or a1 == a3 :
        print("Isosceles")
    else :
        print("Scalene")
else :
    print("Error")
```
