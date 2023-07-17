#Write a python script to enter any number and print the sum of its digit.
n=int(input("enter any number"))
sum=0
while (n!=0):
	a=n%10
	sum=sum+a
	n=n/10
print(sum)