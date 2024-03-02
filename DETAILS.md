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

```

