s=input("input: ")  #input: afsfaaa -> d={'a': 4, 'f': 2, 's': 1}
d={}
for ch in s:
    if ch not in d:
        d[ch]=1
    else:
        d[ch]+=1

for k in d:
    print(k, ": ", d[k], "times" )
