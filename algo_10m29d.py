def my_answer():
  new_id = "...!@BaT#*..y.abcdefghijklm"

  new_id = new_id.lower()
  new_id = new_id
  print(new_id)


my_answer()

# https://programmers.co.kr/learn/courses/30/lessons/77485
def my_answer2():
  input = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
  row = 3
  col = 3
  answer = []
  # [[0 for i in range(COLUM)] for j in range(ROW)] 
  arr = [[0 for col in range(col+1)] for row in range(row+1)]
  print(arr)
  for k in range(len(input)):
    x1,y1,x2,y2 = input[k]
    if arr[x1][y1] == 0:
      min_value = (x1 - 1) * col + y1
    else:
      print(arr[x1][y1])
      min_value = arr[x1][y1]
    print(min_value)
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        print("i: {}, j {}".format(i,j))
        if(i == x1 or i == x2 or j == y1 or j == y2):  
          if arr[i][j] == 0:
            value = (i - 1) * col + j
            if min_value > value:
              min_value = value
            if i == x1 and j != y2:
              arr[i][j+1] = value
            elif i == x2 and j != y1:
              arr[i][j-1] = value
            elif i != x1 and j == y1:
              arr[i-1][j] = value
            elif i != x2 and j == y2:
              arr[i+1][j] = value
          else:
            value = arr[i][j]
            if min_value > value:
              min_value = value
            if i == x1 and j != y2:
              arr[i][j+1] = value
            elif i == x2 and j != y1:
              arr[i][j-1] = value
            elif i != x1 and j == y1:
              arr[i-1][j] = value
            elif i != x2 and j == y2:
              arr[i+1][j] = value
    answer.append(min_value)
     

          # i가 x1 와 같은경우 right(j+1) but y2와 같지 않아야함
          # i가 x2 와 같은경우 left (j-1) but y1과 같지 않아야함
          # j가 y1 과 같은 경우 up (i-1) but x1과 같지 않아야함
          # j가 y2 와 같은 경우 down(i+1) but x2와 같지않아야함 
          # next_value 를 알아야 하는 경우-> 1번째 돌고나면 

  
  print(answer)

my_answer2()

    