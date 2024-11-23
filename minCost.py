# 1916. 최소비용 구하기

import heapq  # 우선순위 큐 사용을 위한 heapq 모듈
import sys  # 입력 속도를 빠르게 하기 위한 sys 모듈
from collections import defaultdict  # 그래프 초기화

input = sys.stdin.read  # 한 번에 입력받아 처리
data = input().splitlines()  # 각 줄을 개행 문자로 구분하여 리스트로 변환

N = int(data[0])  # 도시의 개수 (1 ≤ N ≤ 1,000)
M = int(data[1])  # 버스의 개수 (1 ≤ M ≤ 100,000)

graph = defaultdict(list)  # 그래프 초기화 (출발 도시를 키로 하고, 도착 도시와 비용을 값으로 저장)
for i in range(2, M + 2):
    u, v, cost = map(int, data[i].split())  # u: 출발 도시, v: 도착 도시, cost: 버스 비용
    graph[u].append((v, cost))  # 출발 도시 u에서 도착 도시 v까지의 비용 cost를 추가

start, end = map(int, data[M + 2].split())  # 구간의 출발 도시와 도착 도시 정보

def dijkstra(start, end):  # 다익스트라 알고리즘 정의 (최소 비용 계산)
    distances = [float('inf')] * (N + 1)  # 각 도시까지의 최소 비용을 저장 (1-indexed)
    distances[start] = 0  # 시작 도시의 비용은 0으로 설정

    queue = []      # 우선순위 큐를 이용해 처리할 노드를 관리
    heapq.heappush(queue, (0, start))  # (현재 비용, 현재 도시)를 큐에 삽입

    while queue:
        current_cost, current_node = heapq.heappop(queue)    # 우선순위 큐에서 최소 비용 노드 꺼내기

        if current_cost > distances[current_node]:    # 이미 처리된 노드(더 적은 비용으로 방문한 적이 있는 경우)는 무시
            continue

        for neighbor, weight in graph[current_node]:    # 현재 노드에서 인접한 모든 노드 확인
            new_cost = current_cost + weight  # 새로운 비용 계산
            if new_cost < distances[neighbor]:    # 새로운 비용이 기존 저장된 비용보다 더 작은 경우
                distances[neighbor] = new_cost  # 최소 비용 갱신
                heapq.heappush(queue, (new_cost, neighbor))  # 갱신된 노드를 큐에 추가

    return distances[end]  # 도착 도시까지의 최소 비용 반환

print(dijkstra(start, end))    # 결과 출력 (출발점에서 도착점까지의 최소 비용)

