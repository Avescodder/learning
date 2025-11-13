# # x = 10
# # for i in range(0, 100, 5):
# #     print(x+i)

# myList = ['Seva', 'Murat', 1]

# myList[len(myList) + 1] = 2

# A “special number” is defined as follows:
# 	•	A number n is special if it is 1, or
# 	•	If n is even, it is special if n/2 is special, or
# 	•	If n is odd, it is special if 3n + 1 is special.

# 	1.	Write a recursive function is_special(n) that returns True if n is special, False otherwise.
# 	2.	Analyze the time complexity of your function.

def special_number(n):
    if n == 1:
        return True
    elif  n % 2 == 0:
        return special_number(n // 2)
    else:
        return special_number(3*n+1)
        
print(special_number(5))
