def func1():
    # ruleid:open-never-closed
    open("foo")


def func2():
    # ok:open-never-closed
    fd = open("bar")
    fd.close()


def func3():
    # ok:open-never-closed
    fd = open("baz")
    try:
        pass
    finally:
        fd.close()
