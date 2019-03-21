#!/usr/bin/python3
target=40
act0=+7
act1=-3
a=0
while 1:
  a+=1
  b = bin(a)[2:]
  c = 0
  for q in b:
    if q=='0':
      c+=act0
    else:
      c+=act1
  if c==target:
    print(b)
