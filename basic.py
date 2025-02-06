# # print("hello guys")
# # print(5+6).



# # string 
# # seq of char that is called know as a string 
# # " "
# # name = "rohit "
# # print(name)
# # print(type(name))
# # print(len(name))


# # string 
# # seq of char



# # name = "rohit"
# # print(name)
# # print(type(name))
# # typ=type(name)
# # print(typ)
# # print(len(name))
# # a = "Hello"
# # b = "World"
# # print("a is sting :-",type(a))
# # print("b is sting :-",type(b))
# # print(a+" "+ b)
# # print(a*3)


# # a = "Hello"
# # indexing 
# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[3])
# # print(a[4])
# # print(a[5])


# # slicing
# # a = "Hello"
# # print(a[0:5])


# # name = "ROHIT"
# # # upername =name.upper()
# # # print(upername)
# # lower_name =name.lower()
# # print(lower_name)

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.list <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# lst = [1,2,3,4,5,6,7]
# # print(lst)
# # type 
# # print(type(lst))
# # indexing 
# # print(lst[0])
# # print(lst[2])
# # print(lst[3])
# # print(lst[4])
# # print(lst[5])
# # lst[0]
# # lst[0]


# # slicing 
# # print(lst[0:4])


# # operation 
# # append
# # lst.append("hello") 
# # print(lst)


# # lst1 = [1,2,3,4,5,6,7]
# # lst2 = ['hello',"hii","hey"]
# # lst1.extend(lst2)
# # print(lst1)

# # insert method 
# # mylist.insert(1,"Govind")
# # print(mylist)


# # Remove  method 
# # mylist = [1, 2, 3, 4, 5, 6, 7, 'hello', 'hii', 'hey']
# # mylist.remove(7)
# # print(mylist)

# # pop operation 
# # mylist.pop()
# # print("the last item is :-",mylist[-1])
# # mylist.pop()
# # print(mylist)


# # count function 
# # mylist.pop()

# mylist = [1, 2, 3, 4, 5, 6,6, 7, 'hello', 'hii']
# # print(mylist.count(6))
# # print(len(mylist))
# mylist.reverse()
# print(mylist)



# >>>>>tuple >>>>>>>

# print(type(tpl))
# indexing in tuple 
# print(tpl[1])
# slicing in tuple 
# print(tpl[0:4])

# >>>>>>>>count funtion >>>>>>>>>>>>>>
# print(tpl.count(4))
# print(tpl.index(32))

# print(max(tpl) ,min(tpl) ,sum(tpl) ,len(tpl)) 



# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)

# tpl = (1,2,32,4,4)
# tpl2 = ("hello","hii","bye")
# # merge = tpl+tpl2
# # print(merge)
# for x in tpl2:
#     print(x)


# >>>>>>>>set in python >>>>>>>>>>>>>>>>


# 1.Creating a Set
# 2.Adding Elements (add())
# 3.Removing Elements (remove() & discard()) 
# 4.Checking Membership (in, not in) 
# 5.Union (| or union()) 
# 6.Converting List to Set (Remove Duplicates)
# 7.Difference (- or difference()) 
# 8.Intersection (& or intersection()) 
# 8.Checking Subset & Superset
# 9.Clearing a Set (clear()) 



# 1.Creating a Set
# my_set = {1,2,3,4}
# print(type(my_set))
# print(len(my_set))

# 2.Adding Elements (add())
# my_set = {1,2,3,4}
# my_set.add(5)
# print(my_set)


# 3.Removing Elements (remove() & discard()) 
# my_set={1, 2, 3, 4, 5}
# # my_set.remove(2)
# my_set.discard(5)
# print(my_set)



# 4.Checking Membership (in, not in) 
# my_set = {1,2,3,4}
# print(66 in my_set )


# 5.Union (| or union()) 

# a = {1,2,3,4}
# b ={5,6,7,8}
# print(a.union(b))


# 6.Converting List to Set (Remove Duplicates)
# my_list = [1,2,3,54,1,2,1,2]
# # convert into a set 
# print(my_list)
# my_set=set(my_list)
# print(my_set)



# 7.Difference (- or difference()) 
# a = {1,2,3}
# b ={1,2,3,4,5,3}
# print(a.difference(b))



# 8.Intersection (& or intersection()) 
# print(b.intersection(a))

# 8.Checking Subset & Superset
# print(b.issubset(a))
# print(b.issuperset(a))

# 9.Clearing a Set (clear()) 
# n=myset.clear()
# print(n)

# new_set=myset.copy()
# print(new_set)

# myset = {1, 2, 3,4,5,6,7,8,9}

# print(sum(myset),min(myset),max(myset))




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Dictionary<<<<<<<<<<<<<<<<<<<<<<<<<<
# ✅ Operations:
# Create a Dictionary
# Access Values using Keys
# Use get() Method to Access Values
# Add or Update Key-Value Pairs
# Remove an Element using pop()
# Delete a Key using del
# Clear All Elements using clear()
# Retrieve All Keys using keys()
# Retrieve All Values using values()
# Retrieve All Key-Value Pairs using items()
# Loop Through Dictionary using a Loop
# Check if a Key Exists using in Operator 


# Create a Dictionary
# my_dict = {"name":"Ritik","class":"second year"}
# print(my_dict)
# print(type(my_dict))   name is key and ritik is value of name 


# Access Values using Keys
# print(my_dict['name'])


# Use get() Method to Access Values
# print(my_dict.get('name'))
# print(my_dict.get('class'))

# Add or Update Key-Value Pairs
# my_dict = {"name":"Ritik","class":"second year"}
# my_dict['add']="jaipur"
# print(my_dict)

# Remove an Element using pop()
# my_dict.pop('name') ### 
# print(my_dict)

# Clear All Elements using clear()
# my_dict.clear()
# print("dict is clear",my_dict)

# Retrieve All Keys using keys()
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())


# for loop 
# lst = [1,2,3,4,5]
# for x in lst:
#     print(x)


# my_dict = {"name":"Ritik","class":"second year"}
# for x in my_dict.values():
#     print(x)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.conditional statment >>>>>>>>>>>>>>>>
# if 
# elif
# else

# x = 3 
# if x>10:  # condition 
#     print("x bda hai 10 se ")
# # elif condition 
# elif x ==5:
#     print("x is equal to 5 ")
# else:
#     print("x bda nhi hai ")


# nested condition 
# if :
#     if 
# x = 5 
# y = 5
# if x>1:
#     if y>2:
#         print("x is greater then 1 and y is greater then 2 ")









