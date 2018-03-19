pandas: 
part1--------------------------------------
I wasted a lot of time because I wrote Series as series and it didnt work. (silly)
pandas is called the excel of Python. 
- pandas.Series( ) will make a list into a series.
- we can pass a list as data, and another list as index.
if we dont mention data and index and just mention 2 list names they will be automatically be assigned as data and index in the order. first list or array will be data and second list will be index.
if we pass a dictionary it will autmatically translate it to data and indexes.
we can pass the index to the sereies name just like list and array and get the data. like: seri1['USA'] ==> returns 1 (usa is index and data is 1)
we can add 2 series like this: ser1 + ser2 and it will sum up the data for common items and for unique items it will return NaN
pandas and numpy convert all integers to float in order to retain as much information as possible.
part2-------------------------------------
dataframes 1
-main tool using pandas. dataframes are like tabes in ex
-pandas.Dataframe( ) will make a table of data. we can specify number of columns, rows and data. so cool
-df['new'] = df['X'] + df['Y'] ==> this will add up two columns and put the values in a new column called 'new'
-df.drop('new') will remove new column but we need to pass another array: Axis=1 axis means dimension. axis 0 means row and      axis 1 means column.
-there is another variable we should pass to delete it permanently==> inplace=True
-Axis=0 for rows is not necessary as row is always the default.
-in Pandas dataFrames both row and columns are series.
- for selecting a row we should say:  df.loc['row_name']   OR we say: df.iloc['2']  2 is the index number of the row. (3rd row)
- finding a specific value with row and column:  df.loc['A','X'] ==> returns the value of location row A and column X
- a subset of the dataset:  df.loc[['A','B'],['X','Z']]
part3-------------------------------------
dataframes 2
- we can say df>0 and is shows true/false in each cell
- we can pass the df>0 condition into the dataframe like this:  df[df>0] and it shows the true values and NaN for false values. 
- df[df['W']>0]: fiters the dataframe based on column W values greater than 0
- *****conditional selecting: we can say from the dataframe find greater than zero values and based on that which is another dataframe show me the values of another column.  e.g. df[df['X']>0]['Z']  *****
- for multiple conditions: we can pass all conditions in a parathesis and seperate them with & e.g. : df[(df['X]>0) & (df['Y']<1)]
- for OR operator we should use pipe |
- method reset_index() will add another column for index and uses the index values as an actual column. if we want it to be permanent we need to pass Inplace=True .
- for adding a new column we can say: 'a b c r y e f'.split() and then give the range a name and pass it to the df.
- method df.setIndex('column_name') will assign the column values as index. again we need have inplace=true.
part4---------------------------------------
dataframe 3
-Zip function in python will make tuples from 2 differnet dataframes or lists as pairs. e.g. => list(zip(list1,list2)) it returns thsi==>
[('A',1),('B',2),('C',3)}
- pandas.index.names ===> shows the names of indexes.
- df.xs(1,level='Num') will select all rows with Num=1 in both G1,G2 groups.
part5--------------------------------------
-missing data: if there is any NaN data in dataframe with np.dropna() we can drop all rows that have at least one missing value.
- for doing the same thing or columns we can pass Axis= 1
-parameter thresh= 2 or any number will keep the rows that have at least 2 non NaN value and will erase the rest of the rows.
- fillna can fill the missing values with new values, we can also add mean of other values in a row or column by simply giving the NaN cells the values of df['row_name'].mean()
part6--------------------------------------
-method groupby() will group data by a column name and then we can aggregate the data based on it.
-some useful objects of groupby:
.count()   .sum()  .max()   .min()   .describe()--> this one gives a lot of information including all the others mentioned.
-also we can say  .describe().transpose() then it give information nicely organised in a table.
- at the end of the groupby objects we can simply add ['column_name'] and it will show that data only for a specific column,.
part7--------------------------------------
- concatenation of dataframes:
pd.concat([df1,df2,df3]) ==> The dimensions of the dataframes should match.
-by adding axis=1 we can concatenate based on columns.
- merging:  pd.merge(df1,df2,on='specific_column')  or we can add a list of columns instead of one column
another parameter: how='inner' or 'outer' or 'left' or 'right'  ===> default is inner.
- join method will join multi dataframes with the same indexes and different columns as onr dataframe. similar to merge the difference is that the key is in a index instead of column.  syntax:  df1.join(df2)  we can also have how='inner', 'outer' , 'left' , 'right'
part8--------------------------------------
- finding unique values in a column:   df['column_name'].unique()  ==> we can say: len(df['column_name'].unique()) and it shows how many unique values are there.  also a built-in function does it: nunique()
- values_counts() will count how many times each value is repeated in a dataframe column.
-conditional selection:  df[df['col1']>1]
- apply() method will apply our custom functions to a dataframe. e.g.  df['col1'].apply(sample_function)
- df.drop('col_name',axis=1,inplace=True) ==> deletes a column
>>>>>
An attribute-->   df.columns ==> shows column names
-df.sort_values('col2') ==> will sort the dataframe based on col2  or df.sort_values(by='col2')
-df.isnull() -> shows if there is any null in the datarframe  (boolean)
- df.pivot_values(values='A',index=['B','C'],columns='D')----> an example of a pivot table.
part9 ----------------------------------------
- 4 libraries we need to install first:  1) sqlalchemy  2) lxml   3)html5lib         4)beautifulsoup4  5)xlrd     6) openpyxl 
- pd.read_csv('filename')  reads csv
- df.to_csv() will write df into a csv and save it.
- pandas can only read data and not any formula
- df.read_excel() will read excel. but we need to specify the sheet name like this:  df.read_excel('filename',sheetname='sheet_name')
- df.read_html() when we pass the link to the html will get the data from the html page. 
- sql:
                         from sqlalchemy import create_engine  
                         engine = create_engine('sqlite:///:memory:')   ==> will make a small sql engine in memory
                         df.to_sql('my_table',engine)
                         sqldf = pd.read_sql('my_table',con=engine)
