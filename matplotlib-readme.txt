Matplotlib:
part1---------------------------
how to import;  import matplotlib.pyplot as plt
first thing to do at Jupyter is:  %matplotlib inline ==> it lets us see plot inline.
- plt.plot(x,y)  ===> x , y are two numpy arrays.
- if we dont use jupyter we need to say " plt.show()
- plt.xlabel()   plt.ylabel()   plt.title()   ==> will specify labels and titles
- plt.subplot()==> can make us 2 sub plots on the same canvas. 
- object oriented:   fig = plt.figure() ==> will make an empty canvas.
                               axes = fig.add_axes([0.1,0.1,0.8,0.])  => specifies where the axes                                are and how long they are. (percentage of the canvas)
first number: distance from left(percentage)
second number: distance from bottom(percentag)
third number: length of x axis (percentage)
fourth number: length of y axis (percentage)
axes.plot(x,y)  ==> plots the same thing as before. 
- for object oriented we need to do:  axe1.set_title() or axe1.set_xlabel()
part2---------------------------------
- for making a new figure instead of figure() we can say fig,axes = plt.subplots()
   subplots(nrows=1,ncols=3) ==> will make 3 subplots in one row.
- for inputing data into the plots we can iterate with for loop, or we can call their array index like this: axes[0].plot(x,Y)
- plt.tight_layout() will take care of spacing between plots
- parameters for figure() ==> figsize=(2,3), dpi=100    (dpi=dots per inch)
- fig.savefig('file_name.png',dpi=200) ==> will save the file in the same folder
- ax.legend() will add legond. but before that we need to have a label as a parameter for plot()
- legend as a parameter called loc we can make it =0 so that it finds the best location.
part3 ---------------------------------
- method plot takes parameters like:
ax.plot(x,y,color='color_name or hex code", linewidth= 2 , alpha=0.5, linestyle='--' or '-.' or 'steps',marker='o',markersize=10)  alpha is related to opacity. 
instead of linewidth we can say lw and it works. instead of linestyle we can simply say ls.
marker will mark the array objects on the plot.
- ax.set_xlim([0,10]) ==> will make the limit of x axis to 10. and we have set_ylim as well for y axis limit.

nice link for matplot lib guidance. 
https://www.labri.fr/perso/nrougier/teaching/matplotlib/
