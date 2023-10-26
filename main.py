def euclidA(a, b):
  if a%b !=0:
    remlist = []
    while a%b > 0:
      rem=a%b
      a=b
      b=rem
      remlist.append(rem)
    return remlist[len(remlist)-1]
  else:
    return b

print(euclidA(999999,123123123123123123))
