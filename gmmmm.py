mca=int(input())
cse=0
lit=[]
for i in range(1,mca+1):
  lit.append(i)
for i in range(len(lit)):
  for i in range(i+1,len(lit)):
    cse+=1
print(cse)
