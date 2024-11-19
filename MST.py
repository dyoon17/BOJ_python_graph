#1197. 최소 스패닝 트리

# 간선의 가중치 합이 최소가 되는 스패닝 트리에 대한 문제
# 크루스칼 알고리즘을 사용해 MST를 구함
import sys
input = sys.stdin.read  # 여러 줄의 입력을 한 번에 읽어오는 함수(정점, 간선 수와 간선 데이터를 모두 읽어옴)
sys.setrecursionlimit(100000)  # 밑에서 호출될 유니온-파인드에서 부모를 찾을 때 재귀 호출을 많이 쓰기 때문에 필요함
# 재귀 함수 호출 횟수 제한을 100,000(십만)으로 늘림

# 유니온-파인드 : 사이클을 판별하거나 집합 관리가 필요한 알고리즘에서 사용됨 -> 필요할 때 노드를 이어줘야 하므로..
# 유니온: 두 정점이 다른 집합에 속해 있다면, 두 집합을 하나로 합침
# 파인드: 얘가 먼저 -> 같은 집합에 속해있는지 확인함
def find(parent, x):  # x의 부모를 찾는 함수
    if parent[x] != x:  # x가 자신의 부모(루트 노드)가 아니라면
        parent[x] = find(parent, parent[x])  # 부모를 재귀적으로 찾아 경로 압축 수행 -> 빠르게 찾을 수 있음
    return parent[x]

def union(parent, a, b):  # 두 정점을 같은 집합으로 합치는 함수
    rootA, rootB = find(parent, a), find(parent, b)  # 각각의 부모(루트 노드)를 찾음
    if rootA != rootB:  # 두 노드가 다른 집합에 속해 있을 경우
        parent[rootB] = rootA  # 한쪽 루트를 다른 쪽 루트로 설정해 두 집합을 합침


def main():  # 최소 스패닝 트리를 구하는 크루스칼 알고리즘을 구현
    data = input().splitlines()  
    V, E = map(int, data[0].split())  # 첫 줄에서 정점(V)과 간선(E)의 개수를 읽음
    edges = []  # 간선 정보를 저장할 리스트 생성
  
    for i in range(1, E + 1):
        a, b, c = map(int, data[i].split())  # 간선 정보(시작점, 끝점, 가중치)를 읽음
        edges.append((a, b, c))   # 간선 정보를 튜플로 저장
    
    # 간선을 가중치 기준으로 오름차순 정렬(가중치 작은 것부터 처리)
    # 크루스칼 알고리즘에서는 가중치가 작은 간선부터 처리하기 때문
    edges.sort(key=lambda x: x[2])

  
    parent = list(range(V + 1))  # 각 노드의 부모를 자기 자신으로 초기화(처음에는 모든 정점은 자기 자신만 가지고 있기 때문)
    mst_weight = 0  # 최소 스패닝 트리의 가중치 합을 저장할 변수도 초기화함
    
    # 크루스칼 알고리즘에 대한 for문으로 최소 스패닝 트리 구성
    for a, b, weight in edges:  # 모든 간선을 순회
        if find(parent, a) != find(parent, b):  # 두 정점이 같은 집합에 속하지 않는 경우(사이클이 아니면)
            union(parent, a, b)                # 두 정점을 같은 집합으로 합침
            mst_weight += weight               # 최소 스패닝 트리의 가중치를 합산함

    # 결과 출력
    print(mst_weight)  # 최소 스패닝 트리의 총 가중치 출력

if __name__ == "__main__":  # 이 조건문은 "이 파일이 직접 실행될 때만" 실행됩니다.
    # 다른 파일에서 이 파일을 가져오면 아래 main()은 실행되지 않습니다.
    
    main()  # 이 조건이 만족될 때만 main() 함수를 실행합니다.
