
## About Pandas

From the [pandas homepage](http://pandas.pydata.org/):

> __What problem does pandas solve?__
>
> Python has long been great for data munging and preparation, but less so for data analysis and modeling. pandas helps fill this gap, enabling you to carry out your entire data analysis workflow in Python without having to switch to a more domain specific language like R.

_pandas_ is probably overkill for what we want to do, but it does make the process of handling and organizing data, and then turning into visualizations, less tedious. Its data structures are based off of structures fundamental and familiar to plain Python: __lists__ and __dictionaries__.

Pandas was created by [Wes McKinney](http://blog.wesmckinney.com/), who also authored [Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](http://www.amazon.com/gp/product/1449319793/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1449319793&linkCode=as2&tag=quantpytho-20&linkId=T7GQREAOX3EJE6WS), which I recommend and also quote from in this guide.

Here's a quick 10-minute tour of pandas from McKinney:

<iframe src="https://player.vimeo.com/video/59324550" width="500" height="309" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Greg Rada has an excellent tutorial that covers roughly the same scope of concepts I'm cover here. Check them out for another perspective: 

- [Intro to Pandas data structures](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/)
- [Working with DataFrames](http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/)

### Importing the `pandas` package

For the rest of this lesson, assume that __pandas__ has been imported into the environment like so:


    import pandas as pd

In virtually every tutorial, including this one, you'll see the convention of `pd` being used as _shorthand_ for `pandas`.

## The `pandas.Series` data structure

Pandas docs: [pandas.Series](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.Series.html)


The `pandas.Series` structure is pretty similar to a _list_, in that it holds an ordered list of values:

```py
import pandas as pd
myseries = pd.Series(['alpha', 1, 2, 3, 'zeta'])
print("The first value is:", myseries[0])
# The first value is: alpha
```


However, you can also think of a `Series` object as a _dictionary_, in that its elements can also be indexed by _keys_. Via Wes McKinney's [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do):

> Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. It can be substituted into many functions that expect a dict.


### Constructing a `Series` object

Since `Series` is so similar to a dictionary, we can construct a new `Series` object by passing in a dictionary to its constructor function:


    mydict = {'gamma': 42, 'beta': 30, 'delta' : 101}
    myseries = pd.Series(mydict)
    
    print("This is gamma:", myseries['gamma'])
    print("This is the 3rd element:", myseries[2])


    This is gamma: 42
    This is the 3rd element: 42


As indicated in the above example, when creating the `Series` from a dictionary, pandas will sort the keys by default. Unlike a typical dictionary, this ordering will be enforced, as it would be in a list.

#### Specifying the index

The concept of an ordered __index__ is central to Python lists and for pandas Series as well. In lieu of constructing a Series using a dictionary, you can create a new Series by passing in a list of values and then specifying the __index__ argument. 

Note in the example below how the Series will _not_ sort the index alphabetically and will keep it in the same order as we've specified in the __index__ argument:


    mylist = [42, 30, 10]
    myseries = pd.Series(mylist, index = ['gamma', 'beta', 'delta'])
    print("This is gamma:", myseries['gamma'])
    print("This is the 3rd element:", myseries[2])

    This is gamma: 42
    This is the 3rd element: 10


### Indexing and slices

As seen above, referring to the rows of a Series uses the same bracket `[]` notation as used for lists and dictionaries. However, there are a few more options in selecting _multiple_ values when working with Series.

While using an individual index/key will return the single corresponding value, e.g. `index[0]` gets you `42`, the following examples of multiple indexes/keys will create new Series objects:



    myseries = pd.Series([42, 30, 10, 99], index = ['gamma', 'beta', 'delta', 'alpha'])
    
    myseries[[0, 2]]




    gamma    42
    delta    10
    dtype: int64




    myseries[['alpha', 'beta']]




    alpha    99
    beta     30
    dtype: int64



__A note about the output above:__ The `pandas` data structures come with metadata; the `dtype: int64` refers to the fact that every value in the resulting Series objects from the above commands is an integer.

#### Making slices

*Pandas docs: [Slicing ranges](http://pandas.pydata.org/pandas-docs/stable/indexing.html#slicing-ranges)*

This is similar to slicing plain Python lists:


    myseries = pd.Series([42, 30, 10, 99], index = ['gamma', 'beta', 'delta', 'alpha'])
    
    myseries[2:]




    delta    10
    alpha    99
    dtype: int64



However, we can also slice a Series by its index values:



    myseries['gamma':'beta']




    gamma    42
    beta     30
    dtype: int64



A couple of things to note:

1. Unlike ranges that use integers, ranges with index values are _inclusive_, i.e. the row indexed as `beta` is also included in the resulting sub-Series.
2. You can see how confusing things get if you choose to index your series in non-traditional order, which, in the above scenario, would be alphabetical order.

### Series-wide operations and transformations

Assuming that everything in a given Series is of a single type, we can perform mass operations (better known as [scalar and array operations](http://en.wikipedia.org/wiki/Scalar_%28mathematics%29)) on that Series, creating a new Series object in the process.

Here's how to mass-assign the string `'fluffy'` to the same range of rows accessed in the previous example:


    myseries[2:] = 'fluffy'
    myseries




    gamma        42
    beta         30
    delta    fluffy
    alpha    fluffy
    dtype: object



Note how the `dtype` of `myseries` changed to `object`; the series no longer contains just integers. Although _Series_ are just like lists and dictionaries in that they can contain a sequence of any type of objects, we normally strive to keep them all of one type in most data-wrangling/analysis scenarios.

Here's an example of __scalar arithmetic__, e.g. multiplying all of the elements in the Series with a single value:


    myseries = pd.Series([42, 30, 10, 99], index = ['gamma', 'beta', 'delta', 'alpha'])
    myseries * 10




    gamma    420
    beta     300
    delta    100
    alpha    990
    dtype: int64



And here's an example of __array arithmetic__, e.g. adding elements of a Series with corresponding elements from another sequence (i.e. a list or Series) to produce a new Series: 


    myseries + [1000, 2000, 3000, -4000]




    gamma    1042
    beta     2030
    delta    3010
    alpha   -3901
    dtype: int64



Attempting to perform array operations against differently-sized sequences will result in an error:

```py
myseries + [1000, 2000]
```

#### Boolean operations

Boolean expressions are also possible. The following command creates a new Series object that contains the result of the boolean expression as it is applied to each row:


    myseries > 20




    gamma     True
    beta      True
    delta    False
    alpha     True
    dtype: bool



### Aggregating series

The _pandas_ Series objects come with a variety of useful and familiar aggregation methods and attributes:


    myseries = pd.Series({'a': 20, 'b': -5, 'c': 42})
    myseries.size




    3




    myseries.sum()




    57




    myseries.mean()




    19.0




    myseries.min()




    -5



### Filtering series

One of the biggest advantages for us in using _pandas_ data structures are their many methods for filtering data.

Consider how we filter a dictionary in plain Python:


    mydict = {'apples': 42, 'bagels': 9, 'carrots': 303, 'dates': 7}
    newdict = {}
    for k, v in mydict.items():
        if v > 10:
            newdict[k] = v

Or if you prefer using a [comprehension](http://stackoverflow.com/a/16589453/160863):


    {k: v for k, v in mydict.items() if v > 10}




    {'apples': 42, 'carrots': 303}



Filtering a Series can be done using the same bracket `[]` notation used in indexing a Series:


    myseries = pd.Series({'apples': 42, 'bagels': 9, 'carrots': 303, 'dates': 7})
    
    myseries[myseries > 10]




    apples      42
    carrots    303
    dtype: int64



### Changing the index

It can't be emphasized enough that while a _pandas_ Series is as accessible as a Python dictionary, it still maintains its specified order of keys, i.e. its __index__, and the values they map to.

When creating a Series from a Python list, its index is simply the numerical position of each element. And in creating a Series from a dictionary, its index are the keys of the dictionary: 


    series_a = pd.Series([4, 10, 3])
    series_a.index




    Int64Index([0, 1, 2], dtype='int64')




    series_b = pd.Series({'x': 500, 'y': 600, 'z': 700})
    series_b.index




    Index(['x', 'y', 'z'], dtype='object')



The `index=` method can be used to change the index, effectively __relabeling__ the data, by substituting a list of new index values (the Series and the list of new index values have to be the same size):


    myseries = pd.Series([4, 10, 3])
    myseries.index = ['a', 'b', 'c']
    myseries.index




    Index(['a', 'b', 'c'], dtype='object')



#### Reindexing

The `reindex()` method allows you to rearrange the values of a Series; note that it __does not change__ the Series object but creates a new one:


    myseries = pd.Series({'apples': 42, 'bagels': 9, 'carrots': 303})
    myseries.reindex(['bagels', 'apples', 'carrots'])




    bagels       9
    apples      42
    carrots    303
    dtype: int64



Reindexing the series using values not found in the original index will return a Series that contains the new index values pointing to null/`NaN` values:


    myseries.reindex(['oranges', 'bagels', 'apples', 'carrots'])




    oranges    NaN
    bagels       9
    apples      42
    carrots    303
    dtype: float64



## The `pandas.Dataframes` structures

The __DataFrame__ structure can be thought of as series of _Series_ objects, except that they share two indices: the index that represents the _row_ order, and the index that represents the _columns_ order. In other words, it's pretty much like a spreadsheet.

### Constructing a DataFrame

You can create a 


    
