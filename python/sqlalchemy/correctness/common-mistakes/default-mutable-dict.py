import copy


def assign_func1(default={}):
    # ruleid: default-mutable-dict
    default["potato"] = 5


def assign_func2(default={}):
    for x in range(10):
        # ruleid: default-mutable-dict
        default[x] = 1


def assign_func3(default={}):
    x = default
    # ruleid: default-mutable-dict
    x[3] = 2


def assign_func4(x=1, default={}):
    # ruleid: default-mutable-dict
    default["1"] = 1


def assign_func5(default={}):
    if not default:
        # ruleid: default-mutable-dict
        default["1"] = "test"


def assign_func6(default={}, x="string"):
    # ruleid: default-mutable-dict
    default[1] = 0


def assign_func7(default={}):
    if True:
        default = dict(default)
    else:
        # ruleid: default-mutable-dict
        default[1] = 21


def assign_func8(default={}):
    while True:
        # ruleid: default-mutable-dict
        default[1] = 4
        break


def update_func1(default={}):
    # ruleid: default-mutable-dict
    default.update({1: 2})


def update_func2(default={}):
    for x in range(10):
        # ruleid: default-mutable-dict
        default.update({1: 2})


def update_func3(default={}):
    x = default
    # ruleid: default-mutable-dict
    x.update({1: 2})


def update_func4(x=1, default={}):
    # ruleid: default-mutable-dict
    default.update({1: 2})


def update_func5(default={}):
    if not default:
        # ruleid: default-mutable-dict
        default.update({1: 2})


def update_func6(default={}, x="string"):
    # ruleid: default-mutable-dict
    default.update({1: 2})


def update_func7(default={}):
    if True:
        default = dict(default)
    else:
        # ruleid: default-mutable-dict
        default.update({1: 2})


def update_func8(default={}):
    while True:
        # ruleid: default-mutable-dict
        default.update({1: 2})
        break


def setdefault_func1(default={}):
    # ruleid: default-mutable-dict
    default.setdefault(1, 2)


def setdefault_func2(default={}):
    for x in range(10):
        # ruleid: default-mutable-dict
        default.setdefault(1, 2)


def setdefault_func3(default={}):
    x = default
    # ruleid: default-mutable-dict
    x.setdefault(1, 2)


def setdefault_func4(x=1, default={}):
    # ruleid: default-mutable-dict
    default.setdefault(1, 2)


def setdefault_func5(default={}):
    if not default:
        # ruleid: default-mutable-dict
        default.setdefault(1, 2)


def setdefault_func6(default={}, x="string"):
    # ruleid: default-mutable-dict
    default.setdefault(1, 2)


def setdefault_func7(default={}):
    if True:
        default = dict(default)
    else:
        # ruleid: default-mutable-dict
        default.setdefault(1, 2)


def setdefault_func8(default={}):
    while True:
        # ruleid: default-mutable-dict
        default.setdefault(1, 2)
        break


##### Should not fire on anything below this

# OK
def not_assign_func0(x=1):
    x = {}
    x[123] = 456


# OK
def not_assign_func1(default={}):
    # Immediately overwrites default dict
    default = {}
    default[123] = 456


# OK
def not_assign_func2(default={}):
    # dict() returns a copy
    default = dict(default)
    default[123] = 456


# OK
def not_assign_func2_1(default={}):
    default = dict(m=1, n=2)
    default[123] = 456


# OK
def not_assign_func3(default={}):
    # copy.deepcopy returns a copy
    default = copy.deepcopy(default)
    default[123] = 456


# OK
def not_assign_func3_1(default={}):
    # copy.deepcopy returns a copy
    default = copy.copy(default)
    default[123] = 456


# OK
def not_assign_func4(default={}):
    # dict.copy returns a copy
    default = dict.copy(default)
    default[123] = 456


# OK
def not_assign_func5(default={}):
    # copy returns a copy
    default = default.copy()
    default[123] = 456


# OK
def assign_wrapper():
    pass
    # OK
    def not_assign_func6(default={}):
        default[123] = 456

    not_assign_func6()


# OK
def not_assign_func7(default={}):
    if default is {}:
        return 5 + 1


# OK
def not_assign_func8(default={}):
    default = default or {}
    default[123] = 456


# OK
def not_assign_func9(default={}):
    default = {str(x) for x in default}
    default[123] = 456


# OK
def not_update_func0(x=1):
    x = {}
    x.update({1: 2})


# OK
def not_update_func1(default={}):
    # Immediately overwrites default dict
    default = {}
    default.update({1: 2})


# OK
def not_update_func2(default={}):
    # dict() returns a copy
    default = dict(default)
    default.update({1: 2})


# OK
def not_update_func2_1(default={}):
    default = dict(m=1, n=2)
    default.update({1: 2})


# OK
def not_update_func3(default={}):
    # copy.deepcopy returns a copy
    default = copy.deepcopy(default)
    default.update({1: 2})


# OK
def not_update_func3_1(default={}):
    # copy.deepcopy returns a copy
    default = copy.copy(default)
    default.update({1: 2})


# OK
def not_update_func4(default={}):
    # dict.copy returns a copy
    default = dict.copy(default)
    default.update({1: 2})


# OK
def not_update_func5(default={}):
    # copy returns a copy
    default = default.copy()
    default.update({1: 2})


# OK
def update_wrapper():
    pass
    # OK
    def not_update_func6(default={}):
        default.update({1: 2})

    not_update_func6()


# OK
def not_update_func7(default={}):
    if default is {}:
        return 5 + 1


# OK
def not_update_func8(default={}):
    default = default or {}
    default.update({1: 2})


# OK
def not_update_func9(default={}):
    default = {str(x) for x in default}
    default.update({1: 2})


# OK
def not_setdefault_func0(x=1):
    x = {}
    x.setdefault(1, 2)


# OK
def not_setdefault_func1(default={}):
    # Immediately overwrites default dict
    default = {}
    default.setdefault(1, 2)


# OK
def not_setdefault_func2(default={}):
    # dict() returns a copy
    default = dict(default)
    default.setdefault(1, 2)


# OK
def not_setdefault_func2_1(default={}):
    # dict() returns a copy
    default = dict(m=1, n=2)
    default.setdefault(1, 2)


# OK
def not_setdefault_func3(default={}):
    # copy.deepcopy returns a copy
    default = copy.deepcopy(default)
    default.setdefault(1, 2)


# OK
def not_setdefault_func3_1(default={}):
    # copy.deepcopy returns a copy
    default = copy.copy(default)
    default.setdefault(1, 2)


# OK
def not_setdefault_func4(default={}):
    # dict.copy returns a copy
    default = dict.copy(default)
    default.setdefault(1, 2)


# OK
def not_setdefault_func5(default={}):
    # copy returns a copy
    default = default.copy()
    default.setdefault(1, 2)


# OK
def setdefault_wrapper():
    pass
    # OK
    def not_setdefault_func6(default={}):
        default.setdefault(1, 2)

    not_setdefault_func6()


# OK
def not_setdefault_func7(default={}):
    if default is {}:
        return 5 + 1


# OK
def not_setdefault_func8(default={}):
    default = default or {}
    default.setdefault(1, 2)


# OK
def not_setdefault_func9(default={}):
    default = {str(x) for x in default}
    default.setdefault(1, 2)
