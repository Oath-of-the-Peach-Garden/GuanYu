# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent=[ i for i in range(n) ]
    answer = 0
    for a,b,c in costs:
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent, a, b)
            answer+=c
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))