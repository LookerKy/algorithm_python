# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def my_answer():
  lottos = [0, 0, 0, 0, 0, 0]
  win_num = [31, 10, 45, 1, 6, 19]
  rank = [6,6,5,4,3,2,1]
  min_match = 0
  max_match = 0
  for i in lottos:  
    if i==0:
      max_match +=1
    for j in win_num:
      if i != 0:
        if i == j:
          min_match +=1
          max_match +=1

  answer = [rank[max_match], rank[min_match]]
  print(answer)


def refer_answer(lottos, win_nums):
  rank=[6,6,5,4,3,2,1]

  cnt_0 = lottos.count(0)
  ans = 0
  for x in win_nums:
      if x in lottos:
          ans += 1
  return rank[cnt_0 + ans],rank[ans]



    
