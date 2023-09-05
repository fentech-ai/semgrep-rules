def A():

    # ruleid:useless-inner-function
    def B():

    # ruleid:useless-inner-function
    def C():

    return None


def A():

    # ok:useless-inner-function
    def B():

    # ok:useless-inner-function
    def C():

    # ok:useless-inner-function
    @something
    def D():

    return B(), C()


def foo():
    # ok:useless-inner-function
    def bar():

    return bar


def create_decorating_metaclass(decorators, prefix="test_"):
    class DecoratingMethodsMetaclass(type):
        # ok:useless-inner-function
        def __new__(cls, name, bases, namespace):
            namespace_items = tuple(namespace.items())
            for key, val in namespace_items:
                if key.startswith(prefix) and callable(val):
                    for dec in decorators:
                        val = dec(val)
                    namespace[key] = val
            return type.__new__(cls, name, bases, dict(namespace))

    return DecoratingMethodsMetaclass


def dec(f):
    # ok:useless-inner-function
    def inner(*args, **kwargs):
        return f(*args, **kwargs)

    result = other_dec(inner)
    return result


def decorator_factory(foo):
    def decorator(function):
        # https://github.com/returntocorp/semgrep-rules/issues/660
        # ok:useless-inner-function
        def function_wrapper(*args, **kwargs):
            # Do something with 'foo'.
            return function(*args, **kwargs)

        return function_wrapper

    return decorator


@decorator_factory("bar")
def test():
    """Simple reproducer."""
