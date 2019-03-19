### Python Crash Course:

__using format to print:__

Here is a good example:

```
num = 12
name = moji
print('my name is {}, and my number is {}'.format(name, mum))
```
Outcome:
```
my nme is moji, and my number is 12
```
It automatically grabs the values based on the order we pass the variables into format().

If we need different orders, we can say:
```
name = Moji
num = 12
print('my name is {one}, and my number is {two}'.format(one=name, two=mum))
```

In strings we can address the characters of a string by bracket and the number starting from 0 to any number we want to grab the item from:
```
str = 'moji wins'
print(str[0])  // returns 'm'
print(str[3]   // returns 'i'
```

Also, we can grab characters before/after a specific character:
```
str[3:0]   // returns 'i wins'
str[:3]    // returns 'moj'  - IMPORTANT: it doesn't include index 3.
str[2:5]   // retuns 'ji '  - includes 2 but not 5
```
##### List:
list can take any value such as number, list, or other lists.

```
lst1 = [1,2,3,4]  // list of numbers
lst2 = ['1','2','3']   // list of strings
```
We can add a values to the list like this:
```
list = [1,2,3,4,5,6]
list.append(7)   /// retunrs [1,2,3,4,5,6,7]
```
for lists we can again use brackets to address an object in the list. 
```
list = [1,2,3,4,5,6]
list[2] // returns '3'
list[2:] // returns [3,4,5,6]
list[2:4] // returs [3,4]
```
we can re-assign the values in the list:

```
my_lst = ['a','b','c','d']
my_lst[2] = 'm'   // returns ['a','b','m','d']
```
Here is how we refer to nested elements:
```
lst = [1,2,[3,4]]
print(lst[2][1])  //returns '4'
```

#### Dictionaries:
Dics are series of key-value sets.

```
d = {'key1':'value1', 'key2':123}
```

In dictionaries, we can't pass index number as we did in list, or string. we need to pass the key:
```
d = {'key1':'value1', 'key2':123}
d['key2']  // returns '123'
```
another example:
```
d = {'moji':'awesome', 'num':100}

print('moji is {}, and his grade is {}'.format(d['moji'],d['num']))

```

output:
```
moji is awesome, and his grade is 100
```
the value in the dict can be anything like another list, or dictionary.

example:
```
d = {'key':{'moji':'awesome'}}

d['key']

d['key']['moji']  // returns 'awesome'
```
#### Tuples:

Tuples are exactly like lists, except that they are immutable, and we can't assign a new value to them. 

The syntax is all similar to list but instead of [] we use ()

```
my_lst = [1,2,3]
my_tpl = (1,2,3)
my_lst[0] // returns '1'
mu_tpl[0] // returns '1'
```
We use tuples when we want to make sure the user can't change the values in the output.

#### SETS:

Sets are a sequence of __DISTINCT__ values coming inside curly bracket. 

```
my_set = {1,2,2,3,4,5,3,2,1,1}
print(my_set}   // returns {1,2,3,4,5}
```
sets, are useful when we want to grab unique values of a list. we can use set() function and pass a list to it:
```
lst = [1,2,3,1,3,4,2,2]
set(lst)  // returns // {1,2,3,4
```

We can use add() to add items into the set, and if they already exist, it does'nt return an error but also wouldn't change the set.

```
my_set = {1,2,3}
my_set.add(5)  // returns {1,2,3,5}
``` 

#### Comparative Operators:

We can use < > or == to see what values is greater than the other, and python will return True, or False.

Also, != is for checking if the values are not equal. 

When we use AND operator for two comparison statements, they have to be both True, otherwise it returns False. When we use OR operation, only one of them can be true and it returns True.

#### Basic IF statement syntax:
```
if 1 < 2:
    print('yep!')
```

This is with else:
```
if 1==2:
    print('First')
else:
    print('Last')    
```

Here is with elif:
```
if 1==2:
    print('first')
elif 3==3:
    print('middle')
else:
    print('last')        
```
we can have as many elif statements as needed.

#### Basic FOR statement syntax:
```
seq = [1,2,3,4,5]
for item in seq:
    print(item)     
```
output:
```
1
2
3
4
5
```
But in fact we don't use the seq. we can just say:
```
for item in range(1,5):
    print(item)
```
It returtns the same thing.

or if we want 0 to 10 values, we can say : range(10) it works. 

Or also we can use range() and make a list of values from 0-10 in a list:
```
lst = list(range(10))
lst // returns [0,1,2,3,4,5,6,7,8,9,10]
```
#### Basic WHILE loop syntax:
```
i = 1
while i < 5:
    print('i is:  {}'.format(i))
    i += 1
```
output:
```
i is: 1
i is: 2
i is: 3
i is: 4
```
#### List Comprehension:
```
lst = [1,2,3,4]
out = []
for num in lst:
    out.append(num**2)
print(out)      
```
output:
```
[1,4,9,16]
```
list comprehension is a backward saying of the following for loop:
```
out = [num**2 for num in lst]
print(out)  // returns [1,4,9,16[
```

#### Functions:
```
def myFunc(name):
    print('hello'+ name)
myFunc('moji')   // returns : hello moji    
```
If we want to have a default variable (the variable will be moji unless another name passed when the function is called:
```
def nuFunc(name='moji'):
    print('hello' + name)
myFunc()       // returns : hello moji    
```
When we want to have the output of the variable to be assigned to another variable or used later in other code, we need to use return()
```
def square(num):
    return num**2
my_var = square(3)   // assigns 9 to my_var  
```
__Map Function:__ we can map a function to a list and return it as a list:
```
lst = [1,2,3,4]
def square(num):
    return num**2
list(map(square, lst))   // returns [1,4,9,16]    
```
__Lambda:__ We can make the list above, without separately defining the function. like this:
```
lst = [1,2,3,4]
list(map(lambda x:x**2, lst))  // returns [1,4,9,16]
```
__Filter:__ We can filter the list using a condition:
```
list(filter(lambda x: x%2 == 0, lst))  // returns even values in the list
```
__Methods:__  Methods are predefined functions we can call off of an object, using a dot, like this:

```
s = 'my name is John Doe'
s.upper()   // returns  'MY NAME IS JOHN DOE'
```
__Split() Method:__ It can put all words in a string into a list:
```
s = 'hi, my name is John Doe'
s.split()    // returns ['hi,', 'my', 'name', 'is', 'John', 'Doe']
```
We can also pass some parameters into the split() method, like this:
```
tweet = 'Go Sport! #sport'
tweet.split('#')[1]   //returns sport
```
__in:__ we can check if a value is in a list:
```
x in [1,2,3,4]  // returns 'False'
x in ['x','y','z']   // returns 'True'
```
__Tuple unpacking:__ It's very useful in py, because so many functions return the results in a list of tuples. When we have the list of tuples we can unpack them:
````
x = [(1,2),(3,4),(5,6)]
for a,b in x:
    print(a)   
````
output:
```
1
3
5
```
