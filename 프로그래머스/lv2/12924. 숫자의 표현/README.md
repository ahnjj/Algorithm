# [level 2] 숫자의 표현 - 12924 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12924) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 문제 설명

<p>Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.</p>

<ul>
<li>1 + 2 + 3 + 4 + 5 = 15</li>
<li>4 + 5 + 6 = 15</li>
<li>7 + 8 = 15</li>
<li>15 = 15</li>
</ul>

<p>자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>n은 10,000 이하의 자연수 입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>15</td>
<td>4</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예#1<br>
문제의 예시와 같습니다.</p>

<hr>

## issue
가능한 경우의 수를 전부 돌렸더니 시간이 너무 소요되었다.

## Solution
요구사항 '연속된 자연수의 합' 포인트에 맞춰서 수학적으로 접근해 연산의 수를 절대적으로 줄이고 효율성을 높였다.


★ 연속된 b개의 합

![IMG_7704 Small](https://github.com/ahnjj/Algorithm/assets/23564581/b922258b-671d-4c61-b9e9-03d568cec4cc)

분배 가능하려면 n - sum(a~b)가 b로 나누어 떨어져야한다.

