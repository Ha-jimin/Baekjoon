#1차 배열
a = int(input())
if (a<1) or (a>100):
  exit()
arr=list(map(int, input().split()))
check = int(input())
if (check < -100) or (check > 100):
  exit()
num = 0
for i in range(a):
  if arr[i]==check:
    num += 1
print(num)

#배열
arr = []
for i in range(9):
  arr.append(int(input()))

max = 0
idx = 0
for i in range(9):
  if(max < arr[i]):
    max = arr[i]
    idx = i+1

print(max)
print(idx)

#배열(6/8)
n, m = map(int, input().split())
if (n<1) or (n > 100) or (m < 1) or (m > 100):
  exit()

arr = []
num = 1
for i in range(n):
  arr.append(num)
  num += 1
arr1 = arr.copy()
while True:
  try:
    a, b = map(int, input().split())
    if(a > b) or (a < 1) or (b >n):
      break
    for i in range(b-a+1):
      arr[b-1-i] = arr1[a-1+i]
    arr1 = arr.copy()
  except:
    break

for i in range(n):
  print(arr[i], end= ' ') # print(*arr)
