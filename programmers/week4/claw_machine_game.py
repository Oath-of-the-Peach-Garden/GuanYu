#크레인 인형뽑기 게임

board=[
  [0,0,0,0,0],
  [0,0,1,0,3],
  [0,2,5,0,1],
  [4,2,4,4,2],
  [3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
result=4

result_list=[0]
cnt=0
for move in moves:
  for i in range(len(board)):
    if board[i][move-1]!=0:
      if result_list[-1]==board[i][move-1]:
        result_list.pop()
        cnt+=2
      else:
        result_list.append(board[i][move-1])
      board[i][move-1]=0
      break
print(cnt)