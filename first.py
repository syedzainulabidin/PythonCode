# Python
#todo Chapter 1 (Variables and Data Type)
#!=====================================================================
# val1 = 10; #? Declearation and Assignment in same line of val1
# val2 = 40; #? Storing INT 40 in a variable with the identifier val2
# print(val1+val2)
#!=====================================================================
#! In Python , we can also assign multiple variables in single line
# name1 , name2 = "Syed", "Ali";
# print(name1)
# print(name2)
#!=====================================================================
# ! type() fuction used to print the type of the variable
# name = "zain"; #? string
# age = 19; #? integar
# salary = 1000000.00; #? float

# print("The type of",name,"is",type(name));
# print("The type of",age,"is",type(age));
# print("The type of",salary,"is",type(salary));
#!=====================================================================
#! There are 5 data types in Python as listed
# string = "I'm a string";
# integar = 69;
# float = 19.5;
# boolean = True;
# none = None;
# print(type(string))
# print(type(integar))
# print(type(float))
# print(type(boolean))
# print(type(none))
#!=====================================================================
#! Sum of 2 numbers
# val1 = 10; #? Assigning 10 value to val1
# val2 = 50; #? Assinging 50 value to val2
# sum = val1+val2; #? Assigning the sum of val1 and val2 in sum
# print(sum)
#!=====================================================================
#! In Python adding * b/w STR & INT is a feature (repeatation)
# name = "zain" #? String
# repeat = 4 #? Integar , how much repeatation you want
# print(name*repeat)
#!=====================================================================
#! Concatenation work same as JS
# name1 , name2= "Syed", "Ali";
# print(name1+" "+name2)
#!=====================================================================
#! Difference b/w Division (/) and Integar Division (//)
#? FROM NORMAL DIVISION
#todo Always returns float data type even if the value is a complete integar (i.e. 2.0, 9.0, 0.0) 
# val1 = 5;
# val2 = 10;
# output = val2/val1;
# print(output)
# print(type(output))
#? FROM INTEGAR DIVISION
#todo Always returns int data type, if there is an float it'll turn that float value to 0 (i.e. 3.7 => 3) 
# val1 = 3;
# val2 = 10;
# output = val2//val1;
# print(output)
# print(type(output))
#!=====================================================================
#! 2 Types of Comments in Python
#Comment type 1
"""Comment type 2 (multi
 line comment)"""
#!=====================================================================
#! Input Function
# ? String
# name = input("Enter your name: ");
# print("Welcome",name)
# ? Integar
# age = int(input("Enter your age: "));
# print("According to my calculations, you was born in", 2024-age)
# ? Float
# salary = float(input("Enter your salary: "))
# print(salary,"Sounds like a Good Salary")
#!=====================================================================
#! Conditional Statement
#? Without Logical Operators
# color = input("Enter a color: ");
# if(color == 'red'):
#     output = 'stop'
# elif(color == 'yellow'):
#     output = 'wait'
# elif(color == 'green'):
#     output = 'go'
# else:
#     output = 'Broken Light'
# print(output)
#? With Logical Operators
#todo (or) Logical Operator
# age = int(input("Enter your Age: "))
# if(age < 18 or age > 60):
#     print("Sorry , you are not allowed to vote")
# else:
#     print("Yes , you are allowed to vote")
#todo (and) Logical Operator
# mark = int(input("Enter your marks: "))
# if(mark >= 90 and mark <= 100):
#     print("Grade A+")
# elif(mark >= 80 and mark < 90):
#     print("Grade A")
# elif(mark >= 70 and mark < 80):
#     print("Grade B")
# elif(mark >= 60 and mark < 70):
#     print("Grade C")
# elif(mark >= 50 and mark < 60):
#     print("Grade D")
# else:
#     print("Grade F")
#todo (not) Logical Operator
# blocked = 'zain';
# username = input("Enter your name: ")
# if(not(username == blocked)):
#     print('Acess Granted, (your username is not in our blacklist database)')
# else:
#     print("Acess Denied, (your username is found in our blacklist database)")
#!=====================================================================
#! Nesting Conditions
# age = int(input("Enter your Age: "));
# if(age>=18):
#     if(age>=80):
#         print("Sorry , you're above the age limit")
#     else:
#         print("Yes , you're good to go")
# else:
#     print("Sorry , you're below age limit")
#!=====================================================================
#! Even or Odd check
# num = int(input("Enter a number: "))
# if(num%2 == 0):
#     print(num,"is Even")
# else:
#     print(num,"is Odd")
#!=====================================================================
#! Find the Greatest number b/w 3 entered by User
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# greatest = 0;
# if(num1 > num2 and num1 > num3):
#     greatest = num1
# elif(num2 > num3):
#     greatest = num2
# else:
#     greatest = num3
# print(greatest)
#!=====================================================================
#! Find the Greatest number b/w 4 entered by User
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))
# greatest = 0;
# if(num1 > num2 and num1 > num3 and num1 > num4):
#     greatest = num1
# elif(num2 > num3 and num2 > num4):
#     greatest = num2
# elif(num3 > num4):
#     greatest = num3;
# else:
#     greatest = num4
# print(greatest)
#!=====================================================================
#! Find if the number taken from user is multiple of 7
# num = int(input("Enter a number: "))
# result = "YES" if num%7 == 0 else "NO"
# print(result)
#!=====================================================================
#! Ternary Operator
#? With Variable
# food = 'cake'
# output = "Yes" if food == 'cake' else 'No';
# print(output)
#? With Direct Statement
# food = 'biryani';
# print('Yes') if food == 'cake' else print("No")
#? Clever if / Ternary Operator
# age = 66;
# output = ("You are not allowed","You are allowed") [age>18 and age<60]
# print(output)
#!=====================================================================
#! Type Casting
#? Converting Float to Integar
# todo It always returns the floor value
# a = 2.5;
# a = int(a);
# print(a);
#? Converting String to Integar
# a = '3';
# a = int(a);
# print(a+1);
#? Converting Integar in Float
# a = 3;
# a = float(a);
# print(a)
#!=====================================================================
#! Program to Print sum of 2 numbers taken from user
# val1 = int(input("Enter Firsy Val: "))
# val2 = int(input("Enter Second Val: "))
# sum = val1+val2;
# print('The sum of',val1,'and',val2,'is =',sum)
#!=====================================================================
#! Program to Print area of Square taken from user
# side = float(input("Enter 1 side of square"))
# area = side*side;
# print(area)
#!=====================================================================
#! Program to Print the Average of 2 numbers taken from user
# a = float(input("Enter val1: "));
# b = float(input("Enter val2: "));
# average = (a+b)/2
# print(average)
#!=====================================================================
#! Program to Print TRUE OR FALSE according to the condition
# a = int(input("Enter val1: "))
# b = int(input("Enter val2: "))
# print(a>=b)
#!=====================================================================
#! Escape Sequence
# str = "My name is\nSyed Ali";
# print(str)
#!=====================================================================
#! Concatenation
# str1 = "Syed ";
# str2 = "Ali";
# print(str1+str2)
#!=====================================================================
#! Length
# str = "Syed Ali";
# print(len(str))
#!=====================================================================
#! Indexing
#todo you can only access the character but you can't modify 'em
# str = "Syed Ali";
# print(str[0], str[5])
#!=====================================================================
#! Slicing
#? Positive Indexing
# todo It starts from the 1st val but stops before second. 2nd isn't include
# str = "Syed Ali";
# first = str[0:4];
#* OR
# first = str[:4]
# second = str[5:9]
#* OR
# second = str[5:len(str)];
#* OR
# second = str[5:]
# print(first,second)
#? Negative Indexing
# str = "Syed Ali"
# print(str[-8:-4])
#!=====================================================================
#! String Functions
#todo Ends With
# str = "Syed Ali";
# print(str.endswith("Ali")) #? True
# print(str.endswith("Khan")) #? False
#todo Capitalize
# str = "syed ali";
# print(str.capitalize()) #todo it does effect the orrignal string
#* Output => Syed ali
#todo Replace
# str = "syed ali syed";
# print(str.replace("syed","Muhammad")) #todo it replace all the target not only the first one
#* Output => Muhammad ali Muhammad
#todo Find
# str = "Syed Ali";
# print(str.find("Ali")) #todo Prints the starting index of the target word, -1 if there is no
# #* Output => 5
#todo Count
# str = "My name is Syed Ali , and I'm studying Python";
# print(str.count('a')) #todo prints the occurance (repeatation) of the word in str
#* Output => 2
#!=====================================================================
#! Print Length of name taken from user
# name = input("Enter your Name: ")
# print(len(name))
#!=====================================================================
#! Print Occurance of a letter in a string taken from user
# str = input("Enter something here: ");
# target = input("Enter the Target word: ");
# print("The word",str,"contains '"+target+"'",str.count(target),"times.")
#!=====================================================================
#! Lists
#? Very similar to JS Arrays
#todo lists are mutable , we can change list value in original list
#todo Multiple Data types are allowed 
# student = ["Syed Ali",99,"Turab",75,"Akram",60];
# student[1] = 100;
# print(student) #* Output => Syed Ali",100,"Turab",75,"Akram",60
#!=====================================================================
#! Slicing in Lists
# student = ["Syed Ali",99,"Turab",75,"Akram",60];
# print(student[0:2]) #* Output => 'Syed Ali' , 99
#!=====================================================================
#! List Methods
#? Functions like sort and reverse also work in strings a=>z
#todo Append
# list = [2,1,3];
# list.append(4)
# print(list) #* Output => 2,1,3,4
#todo Sort (Ascending Order)
# list = [2,1,3];
# list.sort();
# print(list) #* Output => 1,2,3
#todo Sort Reverse (Descending Order)
# list = [2,1,3];
# list.sort(reverse=True);
# print(list) #* Output => 3,2,1
#todo reverse
# list = [2,1,3];
# list.reverse();
# print(list) #* Output => 3,1,2
#todo insert
# list = [2,1,3];
# list.insert(0,15);
# print(list) #* Output => 15,2,1,3
#todo Remove
# list = [2,1,3];
# list.remove(1);
# print(list) #* Output => 2,3
#todo Pop
# list = [2,1,3];
# list.pop(2);
# print(list) #* Output => 2,1
#!=====================================================================
#! Tuples (Imutable) changes don't effect in original tuple
#todo if you want to add a single element in a tuple , you should write like this (1,):-
#todo you can create an empty Tuple with just ()
# tup = (1,2,3,4,5);
# print(type(tup))
#? Empty Tuple
# tup = ();
# print(tup);
# print(type(tup)); #* Output => <class='tuple'>
#todo Slicing
# tup = (3, 1, 2);
# new = tup[1:2]
# print(new) #* Output => 1
#todo Index
# tup = (4,7,2,7,3,1,6,3);
# print(tup.index(3)) #todo (index) take one parameter and return the index where it finds that
#* Output => 4
#todo Count
# tup = (4,7,2,7,3,1,6,3);
# print(tup.count(9)) #todo (count) return how many times a number is detected
#* Output => 0
#!=====================================================================
#! Practice Question
#? Store user's 3 most fav movie names in a list
# movies = [];
# movies.append(input("Enter Movie 1: "))
# movies.append(input("Enter Movie 2: "))
# movies.append(input("Enter Movie 3: "))
# print(movies)
#? Check if the List is a Palindrome
# list = ['r','a','c','e','c','a','r'];
# list2 = list.copy();
# list2.reverse()
# if(list == list2):
#     print("It's a Palindrome")
# else:
#     print("It's not a Palindrome")
#? Count A grade count
# grade = ["C","D","A","A","B","B","A"];
# gA = grade.count("A");
# grade.sort();
# print(grade)
# print(gA,"Number of Students Got Grade A");
#!=====================================================================
#! Dictionary
#todo Like the JS Objects
#todo in (key:value) Pairs
#todo We can set the value's data type to anything but we are not allowed to set the data type of Key to Dictionary itself or a List
# student = {
#     'name' : "Syed Ali",
#     'roll' : 6969,
#     'marks' : 530,
# }
# student['gender'] = 'M'; #? Assigning new Key:value pair
# student['marks'] = 550; #? Modifying existing value;
# print(student['name'], student['roll'], student['marks'])
# print(student)
#!=====================================================================
#! Empty Dictionary
# null_dic = {} 
#!=====================================================================
#! Nested Dictionary
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
#todo This is how you can access a particular value from a dictionary stored in another dictionary
# print(student['subjects']['eng']) #* Output => 89
#!=====================================================================
#! Dictionary Methods
#todo keys()
#? Returns all the key
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
# print(student.keys())
# print(student['subjects'].keys())
#todo values()
#? Return all the Values
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
# print(student.values())
# print(student['subjects'].values())
#todo items()
#? Returns the pairs as Tuple
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
# print(student.items())
# print(student['subjects'].items())
#todo get()
#? Works same as simple but if I entered smth which isn't stored in dict, then it'll return NONE rather than an Error
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
# print(student["sasdfgf"]) #* Error
# print(student.get("sasdfgf")) #* No Error => NONE
#todo update()
#? Works same as simple but if I entered a key which isn't located in dict, then it'll return NONE rather than an Error
# student = {
#     "name" : "Syed Ali",
#     "roll" : 6969,
#     "subjects" : {
#         "eng" : 89,
#         "phy" : 75,
#         "com" : 99
#     },
#     "gender" : "M"
# }
# student.update({'roll':100})
# print(student)
#!=====================================================================
#! Sets
#* Sets => MUTABLE | Sets => Elements => IMMUTABLE
#* Elements can be Immutable like String , Tuples etc
#* Elements can't be Mutable like List and Dictionary
#todo Duplicate Items are ignored by set and they're unordered
# collection = {1,2.3,3,4,'Hello',3,1,'Hello'};
# print(collection)
# print(len(collection)) #* Output => 5
# print(type(collection)) #* Output => <class=set>
#todo Empty Set
# collection = set();
# print(type(collection)) #* Output => <class=set>
#!=====================================================================
#! Sets Methods
#todo add Method
#? adds a specific element
# collection = set();
# collection.add("Hello")
# collection.add("World")
# collection.add("Hello")
# print(collection) #* Output => {"Hello","World"}
#todo remove Method
#? removes a specific element
# collection = {"Hello","x","World"}
# collection.remove("x");
# print(collection) #* Output => {"Hello","World"}
#todo clear Method
#? clears the entire set
# collection = {"zain","hamza","moix"};
# collection.clear();
# print(collection) #* Output => {}
#todo pop Method
#? removes a random value
# collection = {"zain","hamza","moiz","ahmed","shahzaib","fawad","bilal"};
# collection.pop();
# print(collection) #* Output => {"zain","hamza","moiz","ahmed","shahzaib","bilal"}
#todo Union
#? returns the union between 2 sets
# set1 = {1,2,3,4};
# set2 = {3,4,5,6};
# union = set1.union(set2)
# print(union) #* Output => {1,2,3,4,5,6}
#todo Intersect
#? returns the common between 2 sets
# set1 = {1,2,3,4};
# set2 = {3,4,5,6};
# intersect = set1.intersection(set2)
# print(intersect) #* Output => {3,4}
#!=====================================================================
#! Practice Question
#? Store Values accordingly
# dictionary = {
#     'table' : ['a piece of furniture','a list of facts and figures'],
#     'cat' : 'a small animal'
# }
# print(dictionary.get('table'))
# print(dictionary.get('cat'))
#? Classroom
# subjects = {'python','java','C++','python','javascript','java','python','java','C++','C'}
# classroom = len(subjects);
# print(classroom)
#? Add marks from user in an empty dictionary
# marks = {};
# marks.update({'maths':int(input("Enter Maths Marks: "))})
# marks.update({'english':int(input("Enter English Marks: "))})
# marks.update({'computer':int(input("Enter Computer Marks: "))})
# print(marks)
#? Store 9 and 9.0 in set
# number = {9,'9.0'};
#* OR === === ===
# number = {
#     ('int',9),
#     ('float',9.0)
# }
# print(number)
#!=====================================================================
#! Loops
#? While Loop
#* Normal Loops
# i = 1;
# while i<=5:
#     print("Hello");
#     i+=1
#* Reverse Loop
# i = 10;
# while i >= 0:
#     print(i);
#     i-=1;
#? For Loop
#* With List
# list = ['cake','chocolate','candy','snickers'];
# for idx in list:
#     print(idx)
#* With Tuple
# tup = ('cake','chocolate','candy','snickers');
# for idx in tup:
#     print(idx)
#* With Sets
# set = {'cake','chocolate','candy','snickers'};
# for idx in set:
#     print(idx)
#* With Dictionary
# dict = {
#     'name' : 'Syed Ali',
#     'age' : 99,
#     'gender' : 'M'
#     };
# for idx in dict:
#     print(idx , dict[idx])
#todo For Loop with OPTIONAL else
# list = ['cake','chocolate','candy','snickers']
# for i in list:
#     print(i);
# else:
#     print("Ended !")
#!=====================================================================
#! Range
#* Returns a Sequence of Numbers | Stoping value in Compulsory
#todo SYNTAX range(start,stop,step)
# for i in range(0,20,2):
#     print(i)
#? Pass allows us to make empty loops (can be used as a placeholder for future code)
# for i in range(0,20,2):
#     pass;
# print("Hello")
#!=====================================================================
#! Practice Questions
#? Print Number form 1 - 100 using while loop
# i = 1;
# while i<=100:
#     print(i);
#     i+=1
#? Print Number form 1 - 100 using for loop and range
# for i in range(1,101):
#     print(i);
#? Print Number form 100 - 1
# i = 100;
# while i >= 1:
#     print(i);
#     i-=1;
#? Print Number form 100 - 1 using for loop and range
# for i in range(100,0,-1):
#     print(i)
#? Table Generator using While Loop
# val = int(input("Enter a Number Value: "));
# i = 1;
# while i<=10:
#     print(val,"x",i,"=",(i*val));
#     i+=1;
#? Table Generator using For Loop and range
# val = int(input("Enter a Value: "));
# for i in range(1,11):
#     print(val,"x",i,"=",(val*i))
#? Square Generator from 1 - 10 in a List
# square = [];
# i = 1;
# while i <= 10:
#     square.append(i*i)
#     i+=1;
# print(square)
#? Search in Tuple using While loop
# val = int(input("Enter a Value: "))
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0;
# found = False;
# while idx < len(tup):
#     if(val == tup[idx]):
#         print("yes Found",val,"at Index",idx);
#         found = True;
#         break;
#     else:
#         idx+=1;
#         continue;
# if(found == False):
#     print("Sorry, Can't find",val,'in',tup)
#? Search in Tuple using For loop
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100);
# val = int(input("Enter a Value: "));
# found = False;
# for i in tup:
#     if(i == val):
#         print("Yes, found",val,"in",tup);
#         found == True;
#         break;
# else:
#     if(found == False):
#         print("Sorry, Can't find",val,'in',tup)
#? Printing Only Even Numbers 1 - 20
# i = 0;
# while i <= 20:
#     if(i%2==0):
#         print(i);
#     i+=1;
#? Printing sum of all numbers from While Loop
# val = int(input("Enter a value: "));
# final = 0;
# i = 0;
# while i <= val:
#     final+= i;
#     i+=1;
# print(final)
#? Printing sum of all numbers from For Loop
# val = int(input("Enter a value: "));
# final = 0;
# for i in range(0,val+1):
#     final += i;
# print(final)
#? Printing Factorial of number taken from user
# val = int(input("Enter a value: "));
# final = 1;
# for i in range(1,val+1):
#     final *= i;
#     i+=1;
# print(final);
#!=====================================================================
#! Funcitons
#? Pararmeterized Functions
# def mul(a,b):
#     return a*b;
# print(mul(10,7))
#!=====================================================================
#? Non Pararmeterized Functions
# def p():
#     print("hello")
# p()
#todo if Funciton isn't returning smth the output variable stores NONE
# def p():
#     print("hello")
# output = p();
# print(output)
#!=====================================================================
#! Calculate Average of 3 Numbers
# def cal_avg(a,b,c):
#     return (a+b+c)/3;

# print('The Average is:',
#     cal_avg(
#         int(input('Enter 1st Value: ')),
#         int(input('Enter 2nd Value: ')),
#         int(input('Enter 3rd Value: '))
#         )
#     )
#? Built-in Functions
# print() , len(), type(), range();
#? User Defined Functions
# def cal_sum(a,b):
#     return a+b;
# print(cal_sum(10,5))
#? Default Parameters mul(a,b=X)
#todo Undefined should be Listed as Parameters First than Defined Parameters
# def mul(a,b=4):
#     print(a*b)
# mul(5);
#!=====================================================================
#! Practice Question
#? Print The length of a List (list is the parameter)
# fruits = ["apple","mango","banana","lichie"];
# heroes = ["ironman","thor","captain america","hulk","black widow","hawkeye"];
# def cal_len(a):
#     print('The Length is',len(a));
# cal_len(fruits);
# cal_len(heroes);
#? Print Elements of List in single line
# fruits = ["apple","mango","banana","lichie"];
# heroes = ["ironman","thor","captain america","hulk","black widow","hawkeye"];
# def list_el(list):
#     for i in list:
#         print(i, end=" ")
# list_el(heroes)
# list_el(fruits)
#? Print The Factorial of Number n (n is the parameter)
# def factorial(val):
#     result = 1;
#     for i in range(1,val+1):
#         result *= i;
#     print(result)
# factorial(int(input("Enter a Val: ")));
#? Print Conversion b/w Dollar to PKR
# def convert(val):
#     print(val,"$ is Equal to",val*(277.50),"PKR || UPDATED ON 02-11-2024")
# convert(int(input("Enter a Value: ")))
#? Even Odd Check Function
# def odd_even(a):
#     if(a%2 == 0):
#         return "EVEN";
#     else:
#         return "ODD";
# output = odd_even(int(input("Enter a Value: ")));
# print(output)
#!=====================================================================
#! Recursion
# def check(n):
#     if(n == 0): #! Base Case
#         return; #! Empty return , returns control
#     print(n)
#     check(n-1) #! Re-running the function with modified value
    
# check(6)
#? Recursion Factorial
# def check(n):
#     if(n == 0):
#         return 1;
#     else:
#         return n * check(n-1)
# print(check(6))
#!=====================================================================
#! Practice Question
#? Recusrsive Function to calculate the sum of first to n numbers
# def cal(a):
#     if(a == 1):
#         return 1;
#     else:
#         return a + cal(a-1)

# output = cal(int(input("Enter a Value: ")));
# print(output)

#? Recusrsive Function to Print all the elements in a list
# def check(n):
#     if(len(n) == 0):
#         return;
#     else:
#         print(n.pop())
#         check(n)
# heroes = ["ironman","thor","captain america","hulk","black widow","hawkeye"];
# output = check(heroes);
# print(output)
#!=====================================================================
#! File I/O input output
#todo if there no file found , it'll create that
#todo read(5) <== this will return the first 5 char of file
#? Open
# file = open('demo.txt','r'); #? open funtion takes 2 parameters. First is compulsory which is the path of file | but second is optional as it's the mode , default set to r : read
#? Read
# data = file.read(); #? .read() function converts that into stream (readable format)
# print(data) #? Printing the output from sibling file
#? Close
# file.close() #? Always remember to close the file after completing all the operations
#!=====================================================================
#? Write
# file = open("demo.txt","w");
# data = file.write("Hey, I'm learning Python")
# file.close()
#!=====================================================================
#? Append
# file = open("demo.txt","a");
# data = file.write("\nHello , I'm here after append");
# file.close()
#!=====================================================================
#! WITH syntax
# #todo READ
# with open("demo.txt","r") as f:
#     print(f.read());
# #todo WRITE
# with open("demo.txt","w") as f:
#     print(f.write("HELLO WORLD"));
# #todo APPEND
# with open("demo.txt","a") as f:
#     print(f.write("\nI'm appended from Python Code"));
#!=====================================================================
#! Remove , OS , remove
# import os;
# os.remove('demo.txt')
#!=====================================================================
#! Practice Question
#? Creating and Adding text to a file using Python
# with open("practice.txt","w") as f:
#     f.write("Hi Everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
#? Changing file's specific content
# with open("practice.txt",'r') as f: #* opening the file in read mode
#     data = f.read() #* storing whole content in DATA variable
# with open("practice.txt",'w') as f: #* opening same file again in write mode
#     f.write(data.replace("Java","Python")) #*writing content again but with replace function
#? Search if the word LEANING exist in file
# with open("practice.txt",'r') as f:
#     data = f.read();
#     print(("No","Yes") [data.count('learning') > 0])
#? Print the line where the word LEARNING occured first, -1 if not
# def checkLine(): #* Function
#     data = True; #* Initial value set to TRUE to start the loop
#     line = 1; #* Intitial value set to 1 for the line 1
#     with open("practice.txt","r") as f: #* opening the file in read mode
#         while data: #* Running loop till the data become invalid (usually when it return empty value)
#             data = f.readline(); #* storing single line in data
#             if("learning" in data): #* Base case
#                 return line; #* if found then return the line number
#             line+=1; #* Updating line number on each loop
#     return -1; #* When the loop will end without finding anything , return -1
# print(checkLine()) #* Running the function and printing the returning values
#? Print even numbers in another file sperated by commas
# def sumNum():
#     with open("numbers.txt","r") as f:
#         data = f.read();
#         num = "";
#         for i in range(len(data)):
#             if(data[i] == ','):
#                 print(int(num)) if int(num)%2==0 else ""
#                 num = "";
#             else:
#                 num+= data[i];
# sumNum()
#*===========================OR=================================
# def sumNum():
#     with open("numbers.txt","r") as f:
#         data = f.read();
#         num = data.split(',');
#         for i in num:
#             print(int(i)) if int(i)%2==0 else ""
# sumNum()
#!=====================================================================
