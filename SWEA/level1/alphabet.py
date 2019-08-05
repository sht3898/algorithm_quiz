a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = { a[i]:i+1 for i in range(len(a))}
 
x =input()
xlist = [ str(alpha[j]) for j in x ]
print(' '.join(xlist))
