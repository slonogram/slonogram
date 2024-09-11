# Sena

Library for composable handlers.

# Design choices

First of all, this library mostly does not depend on whether your functions
async or sync, it is abstract as hell and tries to deal with constraints of python
type hints.

From now on, I'll use arrow notation to describe, functions: `(arg1, arg2, ...) -> return_type`, for example:
1. `() -> bool` - `Callable[[], bool]`
2. `(int) -> bool` - `Callable[[int], bool]`

Sometimes I'll introduce generic parameters in that type, like the following: `[T](T) -> T`, this means
```python
def identity[T](value: T) -> T:
  return value
```
For bounds I'll use the following syntax: `[T: Bound](T) -> T` (which means `TypeVar("T", bound=Bound)`), and `[T: Bound1 & Bound2](T) -> T`,
which means that `T` satisfies both `Bound1` and `Bound2`, currently, in python, this can be achieved more verbose the following way (assuming that `Bound1` and `Bound2` are protocols):

```python
class Bound(Bound1, Bound2):
  ...

T = TypeVar("T", bound=Bound)
def f(x: T) -> T:
  return x
```

Related - <https://peps.python.org/pep-0695/>.

Actually, python team discussing it rn, consider
contributing [here](https://discuss.python.org/t/reviving-the-hybrid-keyword-arrow-syntax-for-callables/52499) if you can.

Also, this text can contain a lot about python limitations about typing (as of 3.12), this is crucial to understand why some decision
was made.

### `SeqHandler` and `Handler` distinguishing

It's accurate to think of them as two functions:

1. `SeqHandler` is `[I, O, N](I, N) -> O`
2. `Handler` is `[I, O](I) -> O`

So, `SeqHandler` is `Handler`'s version with one extra argument (the most abstract interpretation), but logically `SeqHandler` is a "sequential"
handler, or, one may call it "handler with continuation", and `N` is the "next" function.

##### Why there's `O` in generics?

Since python don't have Rank2Types (or `associated types` like in Rust), we must reside to plain generics.

If python had one, we could omit output type and "calculate" it based on arguments.

Related - <https://github.com/python/mypy/issues/7790>.


### Why "next" function is generic and not just callable?

Consider the following example:

```python
# `then` runs `rhs` after running `lhs`. Basically this:
# 
#   <lhs>
#   <rhs>
#
# where <lhs> and <rhs> are code of the lhs and rhs.
def then(lhs, rhs):
  def impl(arg, next):
    return lhs(arg, lambda x: rhs(x, next))
  return impl

def stringify(x: int, next):
  return next(str(x))

def action(x: str, next) -> str:
  return next(x + ", lol")

def identity(x):
  return x

seq = lambda arg: then(stringify, action)(arg, identity)
```

Guess type of the `seq`? It is `(int) -> str`, let's try type hint this example:

```python
import typing as t

I = t.TypeVar("I")
O = t.TypeVar("O")

In = t.TypeVar("In")
On = t.TypeVar("On")

Inn = t.TypeVar("Inn")
Onn = t.TypeVar("Onn")

def then(lhs: (I, (In) -> On) -> O, rhs: (In, (Inn) -> Onn) -> On) -> ((I, (In) -> On) -> O):
  ...

# ...
```

Gross! And impractical. And I'm not even sure if it's properly typed (and too lazy to check with mypy, especially
when arrow syntax is not supported, this thing would look horrible with `Callable`s all over the place), complex!
Our problem is that sequential handler can pass whatever type it likes to the continuation.

So, basically, solution here is to not write unnecessary types, consider checking the [Apply](_internal/apply.py) implementation.


### What's `Reducible` and `Reducer`?

Way to inspect handlers in depth. Reducer is the `[Acc](Acc, t.Any) -> t.Acc`. Here, we use `t.Any`, since
1. Python allows that, and `reduce` expressiveness is great with that
2. Type hints are not powerful enough to more statically-driven (made-up term) approach

For example, you can count number of handlers in chain like that:

```python
def reducer(acc: int, handler: Any) -> int:
  if isinstance(handler, Then):
    return handler.reduce(reducer, acc + 1)
  return acc
```

### ...Chain?

Sure, this library implements [chain-of-responsibility](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern) pattern. It's pretty flexible
and modular, you can even write your own if-else without using any if-else in implementation with it (pretty lame note, by the way).

### What's an `Ext`?

Wrapper around anything that adds sugar-methods to handlers. Simple as that.

