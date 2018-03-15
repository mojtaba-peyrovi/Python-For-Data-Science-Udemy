Numpy intro:
part1--------------------------
numy arrays: 1)vector(linear)         2) metrices 2d
-np.array converts python lists to arrays.
-np.arange makes arrays => variables: start, stop, step.  e.g. even numbers between 0,10 ==> np.arrange(0,11,2)
-np.zeros makes an array of zeros. we can pass a tuple for rows and columns. e.g. np.zeros((5,5))
or np.ones is same thing.
-np.linspace is a function that divides an interval into equal intevals  e.g. np.linspace(0,5,10) ==> cuts 0-5 to 10 equal intervals. it returns only one array.
-np.eye(5) ==> generates an indentity matrix size 5x5 
-np.random.rand() generates a matrix of random numbers between 0-1 (uniform distribution) ==> if we want 2 dimensions we dont pass a tuple we just say: np.random.rand(2,4)
-np.random.randn() returns values from a normal distribution centered around 0
-np.random.randint() returns random integers e.g.  np.random.randint(0,100) ==> returns one random number between 0-100
if we say np.random.randint(0,100,10) ==> returns 10 random numbers between 0-100
-array_name.reshape() will reshape the array from vector to 2d or vice versa e.g.  arr.reshape(5,5) => reshapes a vector array to a 5x5 array if the vector array has enough objects to fill the new array otherwise it returns an error
- array_name.max() returns the max value in the array and min() does it for the minimum.
- array_name.argmax() will return the index of the maximum value and argmin() does the same thing for the minimum value.
- array_name.shape brings back the type of the array
- array_name.dtype returns the datatype
part2------------------------------
- numpy select from array similar to python lists: array_name[index] e.g.  arr[0]==> returns the first element of the array
- also slicing:  array_name[beginning_index : ending_index] e.g. arr[4:6] returns 4th and 5th items
- array_name[:6] ==> will bring eveything before 6th value
-array_name[6:] grabs eveything after 6th index.
- array_name[:5] = 100 ===> [100,100,100,100,100,4,5,8,5,3,6]
- in 2d array we can reference a value by referencing row first and column second. e.g.   arr[0][0] --> it grabs the top left value.
- also we can reference the entire row e.g.   arr[0] ===> returns the entire first row.
- another way or easier way is to say arr[0,0] it is the same as arr[0][0]
- we can do slicnig in 2d arrays like this:  arr[1:2,0:4]
- array comparison with a specific number e.g arr > 5 returns true for values more than 5 and false for less than 5
- arr[arr>5] returns only values greater than 5
part3-------------------------------
- we can use + to add up values by values for 2 arrays. 
- also - for substraction and * for multiplication and / for division
- we can say arr + 100 ==> it adds 100 to each value in the array.
- np.sqrt(arr) ==> takes the sqaure root for each item in the array
- np.exp(arr) ==> makes 2 ** i in the array
