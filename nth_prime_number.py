n=int(input("Enter the number : "))
i = 2
if i == 2:
    print(str(i))
    i = i+1
c=1
while c<n:
    for j in range(2, i):
        if i%j==0:
            break
    if i == j+1:
        print(str(i))
        c=c+1
    i=i+1
d=i-1
print(c,"th prime number is ")
print(d)
