ms= [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
r=0
c=0
d=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
total=0
while i<len(ms):
	r=r1=r1+ms[i][0]
	r2=r2+ms[i][1]
	r3=r3+ms[i][2]
	c=c1=c1+ms[i][0]
	c2=c2+ms[i][1]
	c3=c3+ms[i][2]
	d=d1=d1+ms[i][0]
	d2=d2+ms[i][1]
	total=total+r+c+d
	i+=1
if r1==r2==r3==c1==c2==c3==d1==d2:
	print(d,"magic square")
else:
	print("not")

    
