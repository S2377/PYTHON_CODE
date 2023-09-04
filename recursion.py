# import sys
# sys.setrecursionlimit(99999)

# def factorial(n):
# 	'''   '''

# 	assert type(n) == int ,'Not an int'
# 	assert n > 0,str(n)
# 	#if n==0:                 # Base case
# 	   #	return 1

# 	return n*factorial(n-1)   #  Recursive case 

# print(factorial(5))

# factorial(123)


# def fibbonaci(n):
#     if n <= 1:
#         return n

#     else:

#         return (fibbonaci(n-1)  +  fibbonaci(n-2))


#     for i in range(n):
#         print(fibbonaci(i))



# Q. count the number of 'e ' in the string  using recursion 

# def count_e(s):
#     '''    '''
#     # Base case
#     if s == '':

#         return 0

#     elif len(s) == 1:
#         return 1 if s[0]  == 'e'else 0



#     # Break into two parts        # ye ultra important hai
#     left = count_e(s[0])
#     right = count_e(s[1:])

#     # combining part

#     return left + right

# print(count_e('abeeedrjkjlklj'))



# def commafy(s):
#     '''  '''

#     if len(s) <= 3:
#         return s


#     left = commafy(s[:-3])
#     right = commafy(s[-3:])

#     return left + ','+right

# print(commafy('1234556'))





# def exp(b,c):
#     ''' Return : b**c'''

#     if c == 0:
#         return 1

#     #elif c == 1:
#         #return b

#     else:
#         return b*exp(b,c-1)


    

# print(exp(3,3))





#Q.1

# count_frame =0

# def max_in_list(lst):

#     global count_frame
    

#     '''Returns the value of the maximum element in the list
#          '''




#     assert len(lst) > 0 ,'lst' + ' is a empty list' 

#     if lst[0] == max(lst):
        # count_frame = count_frame+1              # base case
        #return lst[0]
        #count_frame = count_frame+1
    #x =max_in_list(lst[1:])

    #return x                # recursive call


# print(max_in_list([18]))
#print(max_in_list([300,0,-1,34,78]))
# print(max_in_list([12,3,5,6,7,-1,-2,-3]))
#print(count_frame)


# count_frame = 0
# def max_in_list2(lst):
#     global count_frame
#     '''  '''
    
#     if len(lst) == 1:
#         return lst[0]
#     count_frame+=1
#     left = max_in_list2(lst[:1])
#     right = max_in_list2(lst[1:])
#     #count_frame+=1


#     return left if left > right else right

# print(max_in_list2([23,45,67,-45,-100]))
# print(count_frame)





# count_frame = 0
# def reverse(s):
#     global count_frame

#     '''Returns true if s is palindrome otherwise false'''

#     assert type(s) == str,repr(s) + 'is not a string'

#     if len(s) == 1:
#         return s

#     # elif s[0] == s[-1]:
#     #     return True
#     else:
#         return s[-1]+reverse(s[:-1])
    
# def is_palindrome(s):
#     return s == reverse(s)       
# print(is_palindrome('MeaM'))
# print(count_frame)

def is_palindrome1(s):

    if len(s) == 1 or 0:
        return True

    return s[0]==s[-1] and is_palindrome1(s[1:])

print(is_palindrome1('MaaaaM'))



# count_frame=0
# def is_sorted(lst):
#     global count_frame
#     '''Returns True if it is sorted otherwise False

#     precondition : only integers are allowed in list'''

#     #assert
#     if len(lst)== 1 or 0:
#         return True

#     elif lst[0]<=lst[1] and is_sorted(lst[1:]):     # doubt is case  me count_frame kaha insert kare
#         return True

#     else:
#         return False
    
    
    

# print(is_sorted([1,2,3]))

# print(count_frame)


# count_frame=0
# def gcd(a,b):
#     global count_frame
#     '''Returns greatest common factor using euclid algorithm
#     precondition : a and b should be non-negative'''

#     if a == 0 :
#         return b
#     elif b==0:
#         return a

#     elif a>=b:
#         x=a%b
#         return gcd(b,x)

#     else:
#         x = b%a
#         return gcd(a,x)
# print(gcd(1,10))













