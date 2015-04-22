

## Conditional expressions and Boolean operators

Let's take a closer look at the _conditional expression_  of the `if`-statement, e.g. 

        x > 100 

Without the `if` clause, this expression reads as:

> `x` is greater than `100`

When `x` is set to `88`, the result of this expression is the value `False`. Keep in mind that `False` is one of Python's special keywords, and it is _not_ the same as `"False"`.

All the other comparison operators you learned in elementary arithmetic are available:

- `>` - greater than
- '<' - less than
- '>=' - greater than or equal to
- '<=' - less than or equal to
- '==' - equal to
- '!=' - not equal to

### Equality operators




A very, very common error is to mix up:

~~~py
x = 10
~~~

and:

~~~py
x == 10
~~~

This is where having an attention to detail is very important. Always remember, as taught in that early lesson on variables, that `x = y` is _always_ an expression that _assigns_ the value on the right to the variable on the left. As soon as you see a _double_-equals sign, then you have a completely different expression.

### The `in` keyword

The comparison operators can be used to compare strings:

~~~py
"a" < "b"
# True
"a" < "A"
# False
"a" != "A"
# True
~~~

