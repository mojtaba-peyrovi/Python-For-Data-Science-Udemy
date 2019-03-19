### Numpy Review:
---

Numpy arrays are build-blocks of Numpy library. They will come in two different forms. 

1) Vectors which are 1d Numpy arrays
2) Matrices which are 2d Numpy arrays

This is how we pass a Python list into a Numpy array to create a vector. 
```
lst = [1,2,3,4]
array = np.array(lst)  // returns  array([1,2,3,4])
```

And here is how we make a list of lists, into Numpy array to create a matrix:
```
lst = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(lst)  
```
output:
```
array([[1,2,3]
       [4,5,6]
       [7,8,9]])
```
Also, there are np built-in functions to create arrays easier. for example:
```
arr = np.arange(0,10)  // returns 'array([0,1,2,3,4,5,6,7,8,9])'
```
(this is a-range, not arrange, so it has only one r)

we can third parameter to it to make step size. like this:
```
arr = np.arange(0,10,2)  // returns 'array([0,2,4,6,8])
```
Another useful one:
```
np.zeros(3)  // returns a vector of 3 zeros
np.ones(4)   // returns a vecotr of 4 ones
```
also for matrices:
```
np.zeros((3,4))  // returns a 3x4 matrix of zeros
np.ones((34,23))  // returns a 34x23 matrix of ones
```
__Linspace():__ It returns any number of values between two numbers, evenly distanced.
```
arr = np.linspace(0,20,3)  // returns 'array([0,10,20])'
```
It can returns floats as well. 

Creating an identity matrix:
```
np.eye(4)   // creates a matrix all zero except ones on the diagonal line
```
generating random values from Uniform distribution:
```
np.random.rand(5)  // creates 5 random values between 0 and 1
np.random.rand(3,3)  //generates 3x3 matrix of random values between 0 and 1
```
generating random values from Normal distribution:
```
np.random.randn(5)  // creates 5 random normal values with mean of 0
np.random.randn(3,3)  //generates 3x3 matrix of random normal values with mean of 0 
```
generating random integer values from Normal distribution:
```
np.ramdom.randint(1,100,10)  // generated 10 random integers from 0-100 
```
Reshaping an array:
```
arr = np.arange(25)  // creates a vector from 0-24
reshaped_arr = np.reshape(arr)  // converts arr to a 5x5 matrix with the same values
```
Finding max, and min:
```
arr.max()  // returns the maximum value in array
arr.min()  // returns the minimum values in array
```
Finding the index, where the min or max are located:
```
arr.argmax()  // retunrs the index of the max value
arr.argmin()  // returns the index of the min value
```
To find out the data type of the array:
```
arr.dtype()  // retunrs the type i.e. 'int32'
```
Adding two arrays together:
```
arr1 = [1,2,3]
arr2 = [4,5,6]
arr1 + arr2  // returns 'array([5,7,9])'
arr1 - arr2  // retutns 'array([3,3,3])'
arr1 * arr2  // returns 'array([4,10,18])'
# Scalers:
arr1 + 100  // returns 'array([101,102,103])'
arr1 * 100  // returns 'array([100,200,300])'

# Exponentionals:
arr1 ** 2  // retunrns 'array([1,4,9])'
np.sqrt(arr1) // returns the square root for each item
np.exp(arr1)  // retunts exponentional
```



