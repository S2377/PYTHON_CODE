

lst = [[1,2,3],[4,5,6],[7,8,9]]
# print(lst[1][2])


# b = [[9,6],[4,5],[7,7]]
# a = b

# a[1][0]=3
# print(b[1][0])
# x = b[:2]        # yaha par shallo slicing ho raha hai 
# print(x)
# x[1].append(10)  # sliced list me change kiye but 
     
# print(x)

# print(b)       # but 'b'  me bhi reflect ho raha hai,This is called shallow slicing




# import copy
# a = [[1,2],[2,3]]
# b = a[:]                # Shallow copy
# c = copy.deepcopy(a)    # Deep copy

# b[0].append(10)        # isme b me append karne ke bad 'a' me effect dikh raha hai
#                        # This is called  shallow copy
# c[1].append(10)
# print(a)
# print(b)
# print(c)


# lst = [[1,2,3],[4,5,6],[7,8,9]]
# y=[]
# for x in lst:                       # only for 2D lists
# 	for i in x:
# 		y.append(i)     
# print(y)



# for x in lst:
# 	for i in x:                    # row wise
# 		print(i)


# for x in range(len(lst[0])):     # column wise
# 	for i in lst :
# 		print(i[x])
		

# lst = [1,[1,2,3],[4,[5,6,4]],[7,8,9]]
# y=[]
# def flattend(lst):                    # for any multidimensional list
# 	global y
# 	#for x in lst:                       
# 	for i in lst:
# 		if type(i) == list :
# 			#y.append(i)
# 			flattend(i)
# 		else:
# 			#flattend(i)              # recursion me base case hit hona chaiye no matter kahi bhi ho
# 			y.append(i)

# 	return y


# print(flattend(lst))



# def all_nums(table):
# 	'''Return true if table contains only numbers(int/float),false otherwise

# 	Example:
# 	>>> all_nums([[1,2,3],[4,5,6],[7,8,9]])
# 	True
# 	>>> all_nums([[1,2.0,3],[4,5,6],[7,8,9]])
# 	True
# 	>>> all_nums([[1,'shivam',3],[4,5,6],[7,8,9]])
# 	False

# 	precondition : table is a (non-ragged)2d list'''

	# result = True
	# for x in table:
	# 	for i in x:
	# 		if  not type(i) == int or float:
	# 			result = False
	# return result

	# 		#if not type(i) == int or float:           # optimum solution best hai
	# 			#return False

	#return True

				

			
#print(all_nums([[1,2,3],[4,5,6],[7,8,9]]))
#print(all_nums([[1,2.0,3],[4,5,6],[7,8,9]]))
#print(all_nums([[1,'shivam',3],[4,5,6],[7,8,9]]))



# def transpose(table):
# 	''' Returns : copy of table with rows and column swapped 

# 	precondition : table is a(non-ragged)2d list'''

# 	result = []
# 	for x in range(len(table[0])):
# 		column = []
# 		for i in table:
# 			column.append(i[x])    # doubt hai clear ho gaya
# 		result.append(column)

# 	return result

# print(transpose([[1,2,3],[4,5,6],[7,8,9]]))



# def add_ones(table):
# 	'''Adds one to every number in the table
# 	precondition : table is a 2d list
# 	all table elements are int '''

# 	for x in range(len(table)):
# 		for i in table:
# 			i[x] += 1

# 	print(table)

# add_ones([[1,2],[4,5]])



def strip(table,col):
	''' Removes column col from the the givn table

	precondition : table is a(non-ragged) 2d list,

	col valid column  '''

	for x in range(len(table)):
		# table[x]=table[x][:col]+table[x][col+1:]
		table[x].remove(table[x][col])
	print(table)	

strip([[1,2,3],[4,5,6],[7,8,9]],1)


		
