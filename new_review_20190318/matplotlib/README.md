### Matplotlib:

---

- __Plotting x, y basic__: x , y are Numpy series or Pandas 1d dataframe.
```
plt.plot(x, y)
```
If we are not in Jupyter notebook we need to say the following to see the graph:
```
plt.show()
```
- __Axis labels and graph title:__
```
plt.xlabel("x title")
plt.ylabel("y title")
plt.title("my title")
```
- __Subplot:__
```
plt.subplot(1,2,1) // 1=rows 2=columns 1=plot number
plt.plot(x, y)
```
example:
```
def sub_plot(x, y):
    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'r')  //r:red

    plt.subplot(1, 2, 2)
    plt.plot(y, x, 'b')   //b:blue
    plt.show()

sub_plot(x, y)
```

__OBJECT ORIENTED:__ 

We first define a figure, then add objects to the figure:
```
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  
//0.1=left 0.1=bottom 0.8=width 0.8=height
```
This makes an empty area with x, y axis.(figure object)

Then we can add plots to the empty figure.
```
axes.plt(x, y)
```
We can also add x label, y label, title:
```
axes.set_xlabel("X values")
axes.set_ylabel("Y values")
axes.set_title("Object Oriented")
```
__Nested plots:__
