# 1707. 이분 그래프

import sys		
from collections import deque
input = sys.stdin.read  	# 입력을 한 번에 처리

def is_bipartite(v, edges):    # 그래프를 인접 리스트로 표현하기 위해 리스트 생성
    graph = [[] for _ in range(v + 1)]  # 정점은 1번부터 v번까지 사용
    color = [0] * (v + 1)  # 각 정점의 색상을 저장 (0: 미방문, 1: 그룹1, -1: 그룹2)

    for u, v in edges:    # 간선 정보로 그래프 구성
        graph[u].append(v)
        graph[v].append(u)  # 양방향 간선 처리

    def bfs(start):	    # BFS를 사용해 그래프가 이분 그래프인지 확인하는 함수
        queue = deque([start])  # BFS 탐색을 위한 큐 초기화
        color[start] = 1  # 시작 정점을 설정
        while queue:
            node = queue.popleft()  # 큐에서 하나의 정점을 꺼냄
            for neighbor in graph[node]:  # 현재 정점과 연결된 모든 정점 확인
                if color[neighbor] == 0:  # 이웃 정점이 아직 방문되지 않은 경우
                    color[neighbor] = -color[node]  # 현재 정점과 다른 색으로 칠함
                    queue.append(neighbor)  
                elif color[neighbor] == color[node]:  # 이웃 정점이 같은 색일 경우
                    return False  # 이분 그래프가 아님
        return True  # 탐색이 끝날 때까지 문제가 없으면 이분 그래프

    for i in range(1, v + 1):    # 모든 정점에 대해 BFS 수행 
        if color[i] == 0:  # 아직 방문하지 않은 정점이 있는 경우
            if not bfs(i):  # 해당 정점에서 BFS를 수행하고 이분 그래프 여부를 확인함
                return "NO"  # 이분 그래프가 아닐 경우 "NO" 반환
    return "YES"  # 모든 정점에서 문제가 없으면 "YES" 반환

def main():
    data = input().splitlines()      # 입력 데이터를 모두 읽고 줄 단위로 나눔
    k = int(data[0])  # 첫 줄: 테스트 케이스의 개수
    results = []  # 각 테스트 케이스 결과를 저장
    idx = 1  # 현재 데이터를 읽을 위치

    for _ in range(k):	    # 테스트 케이스 수만큼 반복
        v, e = map(int, data[idx].split())        # 정점(v)과 간선(e)의 개수
        edges = [tuple(map(int, data[idx + i + 1].split())) for i in range(e)]		# 현재 그래프가 이분 그래프인지 판별하고 결과를 저장
        results.append(is_bipartite(v, edges))        # 다음 테스트 케이스의 시작 위치로 이동
        idx += e + 1

    print("\n".join(results))    # 모든 테스트 케이스 결과를 출력

if __name__ == "__main__":
    main()  # 프로그램 시작
