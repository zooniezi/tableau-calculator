lambdas = list(map(int, input().split()))

#총 박스 개수 저장
numberOfTotalBox = sum(lambdas)

#총 몇 줄인지 저장
numberOfLambdas = len(lambdas)
lastBoxOfEachRow = []

#해당 박스가 몇 번 줄인지 저장
rowIndex= [0 for i in range(numberOfTotalBox+1)]

for thisBox in range(1,numberOfTotalBox+1):
    counter = thisBox
    for n in range(1,numberOfLambdas+1):
        if counter-lambdas[n-1] <=0:
            rowIndex[thisBox] = n
            break
        else:
            counter = counter-lambdas[n-1]


tableau = [0 for i in range(numberOfTotalBox)]
#연결여부 확인용 리스트 생성
connection = [[] for i in range(numberOfTotalBox+1)]


temprow = 0

#마지막칸에 관한 정보 리스트 만들기
temp = 0
for linenum in range(numberOfLambdas):
    temp += lambdas[linenum]
    lastBoxOfEachRow.append(temp)

print("The last box of each row is : ", lastBoxOfEachRow)

for thisBox in range(1, numberOfTotalBox+1):
    if thisBox not in lastBoxOfEachRow:
        connection[thisBox].append(thisBox+1)
    if rowIndex[thisBox] != numberOfLambdas and thisBox+lambdas[rowIndex[thisBox]-1] <= lastBoxOfEachRow[rowIndex[thisBox]]:
        connection[thisBox].append(thisBox+lambdas[rowIndex[thisBox]-1])

    
def tableauAvilable(connection, nowBox, nowTableau, nowNum):
    for i in nowTableau[connection[nowBox]]:
        if nowNum > i:
            return False
    return True

def tableauDraw(nowTableau, nowBox, nowNum):
    nowTableau[nowBox] = nowNum
    return nowTableau

print("The connection graph of this tableau is : ",connection)

#첫 칸은 1로 고정이므로 미리 대입  
def dfsRecursive(connection, start, visited = []):
    visited.append(start)
    print(visited)
    #현재 노드와 연결된 각 노드 마다
    for node in connection[start]:
        #현재 노드와 연결된 곳이 빈 경우
        
        if node not in visited:
            #연결된 곳과 연결된 곳도 모두 빈 경우
            for nodenode in connection[node]:
                if nodenode not in visited:
                    dfsRecursive(connection, node, visited)
    return visited



route = dfsRecursive(connection, 1)
print(route)