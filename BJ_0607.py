#반복문(6/7)
a = int(input())
for i in range(a//4): #for float type
  print('long ', end='')
print('int')

#반복문(6/7)
a, b = map(int, input().split())
list = []
i = 0
while a !=0 and b!=0:
  list.append(a+b)
  i+=1
  a, b = map(int, input().split())

for b in range(i): #for b in list -> print(b)
  print(list[b])

#반복문(6/7)
a, b = map(int, input().split())
list = []
i = 0
while True:
  try:
    list.append(a+b)
    i+=1
    a, b = map(int, input().split())
  except:
    break

for b in range(i): #for b in list -> print(b)
  print(list[b])
