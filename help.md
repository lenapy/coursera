The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python.

operator.itemgetter(*items)

Return a callable object that fetches item from its operand using the operand’s __getitem__() method.
If multiple items are specified, returns a tuple of lookup values.
In short operator.itemgetter(n) constructs a callable that assumes an iterable object (e.g. list, tuple, set) as input,
and fetches the n-th element out of it.

Example of using itemgetter() to retrieve specific fields from a tuple record:


>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]

>>> getcount = itemgetter(1)

>>> list(map(getcount, inventory))

[3, 2, 5, 1]

>>> sorted(inventory, key=getcount)

[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]