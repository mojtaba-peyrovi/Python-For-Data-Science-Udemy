Seaborn:
part1----------------------------
how to import?   import seaborn as sns
                             %matplotlib inline
seaborn has some bulit-in datasets that we can use as examples. one of them is tips. 
tips = sns.load_dataset('tips')
- sns.distplot(tips['total_bill']) ==> will show the distribution of total bill for tips dataset. the curve is called kde. 
we can pass: kde=False to remove that.
third argument for it:  bins=30 or any integer. the bigger the number is, the smaller the bars are.
- sns.jointplot() will joint 2 distplots.   arguments:  sns.jointplot(x='column1',y=column2,data=dataset_name)

another parameter: kind='hex'==> it shows the scatters(which is the default) to hexagonal points. or kind='reg' will show the regression line.
or kind='kde' which is so cool.
- sns.pairplot(tips) ==> will quickly compare date for columns 2 by 2 and give us a nice insight about how data are corelated.
- pairplot has a cool parameter called hue. we can use it for categorized data like sex. hue='sex' then it seperates the colors and visually shows how data
differ for male/female. 
- sns.rugplot(tips['column_name'])  ==> simply makes a dashmark for each data and it again shows the distribution but simpler.
(KDE stands for: Kernel Density Estimation)

part2-----------------------------
plotting categorical data:
- sns.barplot(x='sex',y='total_bill',data=tips)  ==> we can use the x axis for a catgorical column and y for a numerical column.
- estimator: default is mean but we can use other functions such as std.
- sns.countplot(x='column_name',data=table_name) ==> will count valeues in each category.
- sns.boxplot(x='column_name', y='column_name',data=table_name)
boxplot shows a quarter of the data in boxes and show outlier data as dots inside the full range. 
- sns.violinplot(x='column_name', y='column_name',data=table_name) it is so similar to boxplot. for both of them, 
x should be qualitative and y should be quantitative data.
variable for both: hue='column_name' => should be categorized data. also for violin we can have split=True, to show both distributions
for 2 categories around one category.
- sns.stripplot(x='column_name', y='column_name',data=table_name, jitter=True, hue='sex', split=True) ==> will show
data as stacks of points on the top of each other. 
- sns.swarmplot(x='column_name', y='column_name',data=table_name) ==> a combination of violinplot and stripplot.

part3-----------------------------
plotting matrix data:
in order to have some of the matrix plots like heatmap, we need to have our dataset as matrix. for doing this we just
need to say: dataset_name.corr()
- sns.heatmap(matrix_name) ==> will make a heat map chart. a variable we can pass is annot=True, it shows the values directly 
on the cells.  cmap='coolwarm' is another parameter. coolwarm is a well known one but there are other options too.
	linecolor='white',linewidth=1  ===> will make separation between cells.
- sns.clsutermap() will cluster similar data in the matrix.  ==> standard_scale=1 will normalize data and show which categories
are having more values or less like groups.
part4-----------------------------
regression plots:
- sns.lmplot(x='total_bill',y='tip',data=tips) => will make the linear regression for the dataset values.
 parameters: hue='sex',markers=['o','v']   also => we can separate them by col and row so that it shows 4 charts
if we have 2 values for each categorical data for row and column.  aspect=0.6,size=8 ==> will make the cahrt look better.
part5-----------------------------
grids:
sns.pairplot() ==> from older lessions would make a full comparison of all data 2 by 2. now there is something more advanced:
- sns.GripPlot() ==> it makes the empty grid for comparison. 
then we can define for diagonal, upper or lower charts how to map data: like this:
g.map_diag(sns.distplot)
g.map_upper(plt.scatter) ==> plt is not from seaborn its from matplotlib so we need to import it as well.
g.map_lower(sns.kdeplot) 
-	 g = sns.FacetGrid(data=tips,col='time',row='smoker')
	g.map(sns.distplot,'total_bill')  ==> will compare time vs smoker and total_bill
part6------------------------------
styling and color:
-sns.set_style('ticks') ==> it has very nice pre-defined styles. one of the best ones is whitgrid, or darkgrid.
- to change canvas size we can still use matplotlib plt.figure(figsize=(12,8)) => first we need to import it.
- sns.set_context('notebook') ==> has pre defined sets of fonts and sizes for different context, like notebook(default),poster,talk and paper.
-palette='seismic' we have a lot diffrernt options for palettes. here: https://matplotlib.org/examples/color/colormaps_reference.html




