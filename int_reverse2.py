def reverse_string(s):
	reverse = s[::-1]
	return(reverse)

def is_palindrome(s):
	reverse_string = reverse_string(s)
	return reverse_string==s

x =input("Enter the integer : ")
y = str(x)
print(y)
z=reverse_string(y)
print(z)


