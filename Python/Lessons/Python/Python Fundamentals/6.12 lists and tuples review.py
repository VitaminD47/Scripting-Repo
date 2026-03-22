#1 Consider the code : 

devices = [{"hostname": "router1", "ip": "192.168.1.1", "type": "router"}, {"hostname": "switch2", "ip": "192.168.1.2", "type": "switch"},]
for device in devices:
    if device["type"] =="router":
        print(device["hostname"])


# What is the output of the code? 
# Answer: router1





#2 Consider the below code : 

ip_addresses_string = "192.168.1.1, 192.168.1.2, 192.168.1.3,192.168.1.4"
ip_addresses_list = list(ip_addresses_string.split(','))
print(ip_addresses_list)

# What is the value of ip_addresses_list

# The above code is creating a string of IP addresses, then turning it into a list using the list function, then within input of the function, adding a .split method
# The .split method with (',') is the separator, which will will separate each value at the commas , to produce a more readable output.





# 3) Which Python collection is best suited for storing an ordered sequence of elements that can be changed?
# Answer : Lists. Lists are ordered, mutable sequences making them suitable for storing an ordered sequence of elements that can be changed.



#4) In Python, if there is a list called fruits with the elements ['apple', 'banana', 'cherry', 'date', 'elderberry'], what will be the output of print(fruits[-3])?

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[-3])

# Output is cherry due to negative indexing. -3 corresponds to the third from the last element.



#5) Consider a list numbers = [0, 1, 2, 3, 4, 5]. What will be the output of numbers[::2]?

# Answer : [0, 2, 4] because ::2 slice means start fromt he beginning, end at the end, and our steps are 2. Think of it like intervals.




#6 ) Consider a string s = "Python". What will be the output of s[-3:-1]?

# Answer = "ho" because -3 index refers to the third from last item which is 'h' and -1 index refers to the last item 'n'. 
#So, it will return everything up to the last (not including the last) which is 'h' and 'o'.


#7 ) Consider a tuple t = (1, 2, 3, 4, 5). What will the output be of 6 in t?

t = (1, 2, 3, 4, 5)
print(6 in t)

#The in keyword checks if a specified item is present in an iterable object. Since 6 is not in the tuple t, it returns False


#8) Consider the python code : 
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
print(fruits)

 # What will be the value of fruits after executing the code? 

# Answer ) The value at index 1 has been changed from ‘banana’ to ‘blueberry’ so it will output ['apple', 'blueberry', 'cherry']


#9 Consider the python code :

numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [7,8]

# What will the value be after executing the code?

# Answer )  numbers = [1, 7, 8, 4, 5] due to modifying values at index 1 and 2. Not at 3, just up to 3 so all included before then.

# 10 ) Consider the following Python code:

colors = ['red', 'blue', 'green']
colors.insert(1, 'yellow')
 #   What will be the value of colors after executing this code?

# Answer ) ['red', 'yellow', 'blue', 'green'] because the 'yellow' element is inserted at index 1, shifting 'blue' and 'green' to the right.



# 11 ) Consider the following Python code:

animals = ['cat', 'dog', 'bird']
animals.append('fish')
 # What will be the value of animals after executing this code? 

 # Answer ) ['cat', 'dog', 'bird', 'fish'] because 'fish' element has been appended (added) to the end of the list. It does this by default

# 12)
# Consider the following Python code:

letters = ['a', 'b', 'c']
letters.extend(['d', 'e'])
print(letters)

# What will be the value of letters after executing this code? 

# Answer ) ['a', 'b', 'c', 'd', 'e'] The elements ‘d’ and ‘e’ have been appended to the end of the list, after ‘c’

# Important note for .append() and .extend() :

# .append() adds one item to the end of the list (even if that item is another list).

# .extend() adds each item from an iterable (like a list) to the list.

# Example : 

a = [1, 2]
a.append([3, 4])
# a is now [1, 2, [3, 4]] ← note the nested list

a = [1, 2]
a.extend([3, 4])
# a is now [1, 2, 3, 4] ← no nesting



#13 ) Consider the following Python code:

numbers = [1, 2, 3, 2, 4]
numbers.remove(2)

# What will be the value of numbers after executing this code?

# Answer ) [1, 3, 2, 4]     .remove() only removes first occurence of 2, not subsequent occurences





#14 ) Consider the following Python code:

devices = ['router1', 'switch2', 'firewall3']
removed_device = devices.pop(1)
print(devices)
print(removed_device)


# What will be the value of devices and removed_device after executing this code?
# The pop() method removes and returns the item by position. Here it's index 1, which is ‘switch2’. 
# By default, .pop() will remove the *last* item, or you can specify the index as in the example.
# devices will be ['router1', 'firewall3']

#Important note on .pop() is that you are removing the value from the list, but also "holding" onto it which can then be used elsewhere



#15) 

#Consider the Python code:

devices = ['router1', 'switch2', 'firewall3', 'server4']
del devices[1:3]
# What will be the value of devices after executing this code?

# Answer: devices will = ['router1', 'server4'] because del will delete based off index positions


#16) Consider the following Python code used in network automation:

devices = ['router1', 'switch2', 'firewall3', 'server4']
devices.clear()

# What will be the value of devices after executing this code?
# Answer )    [] <--- because .clear() removes all items from the list. 


#17 Consider the following Python code:

ip_addresses = ["10.0.0.2", "10.0.0.1", "10.0.0.3"]
ip_addresses.sort(key=lambda ip: tuple(map(int, ip.split('.'))))

# What will be the value of ip_addresses after executing this code?

# Answer ) ["10.0.0.1", "10.0.0.2", "10.0.0.3"]   The sort() method sorts the IP addresses in ascending order,
#  and the key parameter ensures that the IP addresses are sorted numerically rather than lexicographically

#18 ) In a network automation script written in Python, a list of IP addresses is sorted in descending order using the sort() method.

#  Which of the line of code correctly achieves this?

# Answer : ip_addresses.sort(reverse=True)     The reverse=True argument causes sort() to arrange the list in descending order.



#19 ) In Python, what is the purpose of the key parameter in the sort() method and the sorted() function?
 
#Answer : ) It defines the sorting criteria by applying a function to each element in the list

# The key parameter expects a function that defines the sorting criteria. 
# This function is applied to each element in the list, and the elements are sorted based on the values returned by this function. 
# This is what's happening with question # 17 with the lambda function i.e .sort(key=lambda ip: tuple(map(int, ip.split('.'))))



# 20 ) How can a case-insensitive sort be performed in Python using the sort() method or the sorted() function?
# Answer : By setting the key parameter to a function that converts each item to lowercase before comparison

# 21 ) What is the effect of the reverse() method on a list in Python?

# Answer : It modifies the original list to reverse the order of items and does not return any value

# 22 ) What is the result of using the copy() method or the list() constructor on a list in Python?

#Answer :  A new list is created from the original list. It is a separate list and does not modify the original.
b = ["cisco", "router"]
new_list = b.copy()
print(new_list)


# 24) What is the difference between using the + operator and the extend() method to concatenate lists in Python?

# Answer : The + operator creates a new list, while the extend() method adds elements to the end of the original list


#25 ) What happens to the original lists when they are concatenated using the + operator in Python? 

# Answer :  A new list is created, and changes to this list will not affect the original lists

# 26) What is a significant advantage of using tuples in Python for storing information about network devices?

# Answer :  Tuples can be used as keys in dictionaries due to their immutability. 
# Since tuples are immutable, they can be used as keys in dictionaries, which require immutability for hash mapping.


# 27) How can you determine the number of items in a tuple?
# Answer : By using the built in len() function. example below

tuple1 = ("cisco", "9200", "switch", "10.200.2.1")
print(len(tuple1))


# 28) How is a tuple with a single item created in Python?

# Answer : By placing a single value inside parentheses () and following it with a comma i.e mytuple = (router,)
single_tuple = ("virtual firewall",)
print(single_tuple)


#29) What is the purpose of the tuple() constructor?

# Answer : It converts an iterable into a tuple. The tuple() constructor can take an iterable (like a list or a string) as an argument and convert it into a tuple

#30) How are items in a tuple accessed?

 # By placing the index of the item inside square brackets [] after the tuple name




#31) How is a range of indexes specified in a tuple using slicing?
# Answer : By specifying a start index and an end index separated by a colon : inside square brackets []

# Slicing in Python is done by specifying a start index and an end index separated by a colon : inside square brackets []
# This applies for lists as well, not just tuples.





# 32) How does negative indexing work for tuples? 
# Negative indexing starts from the end of the sequence, with the last item at index -1




# 33) Which keyword is used to check if a specific item exists in a tuple?
# Answer : the keyword 'in' is used to check if items exist in a sequence like a tuple or list. It will return a true or false value.



#34) What is the correct sequence of steps to modify a tuple?

# Answer : Since tuples are immutable, the workaround to change the values in a tuple involves:
#  converting the tuple into a list, changing the list, and then converting the list back into a tuple



# 35) Which of the following Python code snippets correctly demonstrates the workaround to add an item to a tuple?

# Answer :
v = (1, 2, 3)
v = v + (4,5)
print(v)

# This is the correct way to add an item to a tuple. It involves concatenating the original tuple with another tuple containing the new item



# 36) Which of the following Python code snippets correctly demonstrates the workaround to remove an item from a tuple? 

# Answer : 
t = (1, 2, 3); t = list(t); t.remove(2); t = tuple(t)
print(t)

#This is the correct way to remove an item from a tuple. 
# It involves converting the tuple to a list, removing the item, and then converting the list back to a tuple.

