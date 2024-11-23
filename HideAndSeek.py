# 1697. 숨바꼭질

from collections import deque

def find_fastest_time(N, K):  # 수빈이가 동생을 찾는 가장 빠른 시간을 계산하는 함수

    MAX = 100000      # 최대 위치 범위
    
    visited = [-1] * (MAX + 1)      # 방문 여부와 시간을 저장할 배열 / 위치 i를 방문했을 때 걸린 최소 시간을 -1로 초기화하여 방문하지 않은 상태를 나타냄
    
    # BFS를 위한 큐 초기화
    queue = deque([N])
    visited[N] = 0  # 시작 위치 방문 처리 
    
    while queue:      # BFS 탐색 시작
          current = queue.popleft    # 현재 위치를 큐에서 꺼냄
        
        if current == K:    # 동생 위치에 도달했을 경우 시간 반환
            return visited[current]
        
        for next_pos in (current - 1, current + 1, current * 2):    # 현재 위치에서 이동할 수 있는 세 가지 경우를 탐색
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:    # 유효한 위치(0 <= next_pos <= MAX)이며, 방문하지 않은 위치인 경우
                visited[next_pos] = visited[current] + 1    # 다음 위치의 방문 시간을 현재 위치의 시간 + 1로 설정
                queue.append(next_pos)    # 다음 위치를 큐에 추가하여 탐색을 계속

N, K = map(int, input().split())    # N: 수빈이의 현재 위치 / K: 동생의 위치

print(find_fastest_time(N, K))    # 동생을 찾는 가장 빠른 시간을 계산하여 출력
