### PANDAS:

---
#### Series:

Pnadas series are built on the top of Numpy arrays, except that we can address the elements using the index number.

We can make series using pd.Series().

we can change the index values by passing index attribute into Series method:
```
pd.Series(data=[10,20,30], inedx=['a','b','c'])
OR
pd.Series([10,20,30],['a','b','c'])  as long as they are in the correct order.
```
Also we can pass a numpy array as data field, and it works the same way as passing lists:
```
pd.Series(np.array([10,20,30]))
```
A cool way to make series, is to pass a dictionary into the series method and it automatically assigns indexes.
```
pd.Series({'a':10,'b':20,'c':30})
```
- An important characteristic of pandas series, is that they can hold almost any datatype even built-in functions.

In order to call an object of a series we can call the index:

```
seri1 = pd.Series([1,2,3],['USA','Germany','Japan'])
seri1['USA']   // returns '1'
```
if the index is an integer, we simply call the index number:
````
seri2 = pd.Series([1,2,3,4])
seris2[3] // retutns '4'
````
When we try to sum up two series, it will find the ones with the same index, adds them up and if there is no common index in some cases, pandas will put 'NaN' instead.

__IMPORTANT:__ When doing math operations on series, the results will be automatically converted into float.


#### DataFrames:

pd.DataFrame() will create a table just like excel. 

Each column of a dataframe is actually a pandas series. A dataframe is made of a bunch of series that share the same indexes.

#### USEFUL PANDAS OPERATIONS:

1- Grabbing a column:
```
df['column_header']  i.e.  df['W']   // returns the column W

ALSO:  df.W   // returns the column W
```

2- to check the datatype of a dataframe or a column:
```
type(df)  OR  type(df['W'])
```  

In order for pandas to return multiple columns, we can pass a list of column names:
```
df[['W','Y']]  // returns both W,Y columns
```
3- to add a column we just act as if it already exists:
```
df['new'] = df['W'] + df['Z']  // adds a column called new 
and the value for each row equals W+Z
```

4- To delete a column:
```
df.drop('new',axis=1)  // deletes the column called new
```
This however is not inplace. in order to make it permanent we need to specify:
```
df.drop('new', axis=1, inplace=True)
```
5- To delete a row:
```
df.drop('E')  // deletes the row with the index of E
```
6- Select a specific row by index name:
```
df.loc['E']  // returns row E as a series
```
7- Select a specific row by index location:
```
df.iloc[2]  // returns the third row
```
8- To select a single cell:
```
df.loc['A','W']   // returns the value in row A and columns W
```
9- To select a subset of the dataframe:
```
df.loc[['A','B'],['W','Z']]
```
10- We can compare all cells in the dataframe, with a single number and it returns a dataframe of booleans.
```
df > 0  // returns the dataframe, and for each cell, if it is greater than zero, it returns True and False otherwise.
```
Now if we pass df > 0 inside df, we get the dataframe back and wherever the condition is true it returns the value, and if it is false it returns `NaN`
```
df[df > 0]
```
__SO USEFUL:__ It happens in real world conditions, that we want to have only the rows, where a specific column has a condition and if the condition is not true, we want to row to be cut off. We do it like this:
```
df[df['W'] > 0] // returns the rows where column W has positive value.
```
Since, the result of the expression above, is a dataframe itself, we can do all dataframe operations on that as well, like:
```
df[df['W'] > 0]['X'] // returns only column x of the new dataframe
```
or:
```
df[df['W'] > 0]][['X','Y']] //returns columns x,y of the new dataframe
```
11- When we want to return the values, where multiple conditions are true: for example:
```
df [ (df['W'] > 0) & (df['X'] < 0) ] // returns only the rows where both conditions are true.
```
Also, for __OR__ condition, we use pipe (|).

12- In order to reset index into numerical values, we can say:
```
df.reset_index(inpace=True)
```
Also we can create a list of indexes we want, and assign them to the dataframe. 
```
new_index = 'CA NY WY OR CO'.split()  // returns ['CA','NY','WY','OR','CO'] 
df['State'] = new_index   // adds the values as a new column
df.set_index('State')  // sets the new columns as the index
```

13- groupby: we can see in group-by-table.jpg, we can group the data by company name:
```
byComp = df.groupby('company')  // returns a grouby object
```
Now we can call an aggregate function on the groupby function:
```
byComp.mean() // will retrun the average of sales per company
byComp.sum() // will return the sum of sales per company
byComp.std()  // returns standard deviation
byComp.count()  // returns the count of people working for each company, and number of sales.
```
The result of these aggregates will be a dataframe too, so we can say:
```
byComp.sum().loc['fb']  // returns the sum of facebook sale
``` 
Also we can call describe on gorupby and get information about each group:
```
byComp.describe()
```





