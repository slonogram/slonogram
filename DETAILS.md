# Just a function

every handler could be just a function

```python
# Explicit `Activation` would be somehow sidestepped later
async def handle(context: Context[int]) -> Activation:
    return Activation.ACTIVATED

def ctx(value: int) -> Context[int]:
    # for demonstration purposes
    raise NotImplemented

observer = Wrap(handler).never_activate()
# Now this function when calling will always return `Activated.STALLED`

await observer(any_context) == Activation.STALLED

# What if we want, say, activate only if filter satisfied?
# filter also is just a predicate function with signature
# (Context[M]) -> bool
def is_even(v: int) -> bool:
    return v % 2 == 0

def last_digit_is_zero(v: int) -> bool:
    return v % 10 == 0

f = Wrap(handle).filtered(lift(is_even))
# we can lift is_even, so that lift(is_even) type will be
# (Context[int]) -> bool instead of (int) -> bool

assert (await f(ctx(10)) == Activation.ACTIVATED)

# Also if you like using operators instead of chained methods
f = Wrap(handle) & lift(is_even)

# By the way, `lift` optionally performs extending `is_even` to the `ExtendedFilter` type
# Which supports combining filters with binary operators
f = Wrap(handle) & (lift(is_even) & lift(last_digit_is_zero))

assert (await f(ctx(10)) == Activation.ACTIVATED)

# Or like that
f = Wrap(handle) & (lift(is_even) & ~lift(last_digit_is_zero))

# Number must be even and not divisible by 10
assert (await f(ctx(12)) == Activation.ACTIVATED)
assert (await f(ctx(10)) == Activation.STALLED)

# Also we can use middlewares like that

def throw(e: Exception) -> NextMiddleware[int]:
    async def _mw(context: Context[int]) -> Activation:
        raise e
    return _mw

async def catch_and_print(ctx: Context[int], next: Handler[M]) -> Activation:
    try:
        return await next(ctx)
    except Exception as exc:
        print(f"Caught exception {exc} at {next}")
        return Activation.STALLED

f = Wrap(handle) << throw(ValueError("I am the error")) << catch_and_print

assert (await f(ctx(10)) == Activation.STALLED)
# Also "Caught exception <...> at <...>" would be printed in the terminal
# middlewares are executed from right to left, so exact order is:
# 1. catch_and_print
# 2. throw(ValueError("I am the error"))
# 3. Wrap(handle)
```

# Benefits

1. Relatively easy conception: handler is just a function, all other abstractions and functionalities are just wrapped around (functionality is just a layer around function) the single handler
2. We can show user a meaningful error, for example, if some filter matched, but at this state we can definitely say that user **wanted** to use that handler, just screwed up something, exception can be thrown from failed filter and catched, like:
```python
(
    Wrap(handle)
    @ (prefix & word('test') & report & word('123'))
    << catch
)
```
In this example, `catch` will catch exception like `ScrewedUp` and send useful error message
