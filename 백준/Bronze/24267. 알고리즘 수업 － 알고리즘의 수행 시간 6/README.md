# [Bronze II] 알고리즘 수업 - 알고리즘의 수행 시간 6 - 24267 

[문제 링크](https://www.acmicpc.net/problem/24267) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 수학, 시뮬레이션

### 제출 일자

2025년 1월 7일 01:13:46

### 문제 설명

<p>오늘도 서준이는 알고리즘의 수행시간 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p>입력의 크기 <em>n</em>이 주어지면 MenOfPassion 알고리즘 수행 시간을 예제 출력과 같은 방식으로 출력해보자.</p>

<p>MenOfPassion 알고리즘은 다음과 같다.</p>

<pre>MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}</pre>

### 입력 

 <p>첫째 줄에 입력의 크기 <em>n</em>(1 ≤ <i>n</i> ≤ 500,000)이 주어진다.</p>

### 출력 

 <p>첫째 줄에 코드1 의 수행 횟수를 출력한다.</p>

<p>둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.</p>

###  문제분석 & 이유
---

이 또한 3중 루프 문제이다.
첫번째루프는 1부터 n-3까지 이므로 n-2번 수행되고
두번째 루프는 i+1부터 n-2까지 이므로 n-1-i 번 수행된다
세번째 루프는 j+1부터 n-1까지 이므로 n-j번 수행된다.

따라서 (n * (n-1) * (n-2)) // 6 의 횟수로 실행된다
여기서 최고차항의 차수가 3임을 알수있다.

###  Pseudo Code

---

```
n받기
(n * (n-1) * (n-2)) // 6 출력하기
3 출력하기
```


### 문제 해결 및 배운 점
---
횟수를 정확히 따지는 것이 헷갈렸다. 

### 최종 코드
---

```
#코드 1의 수행횟수
n = int(input())
print((n * (n-1) * (n-2)) // 6)

#최고 차항의 차수
print(3)
```
