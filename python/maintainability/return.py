def alwaysblue():
    if isblue():
        return "blue"
    # ruleid: code-after-unconditional-return
    return "red"
    return "green"


def alwaysblue():
    if isblue():
        return "blue"
    # ruleid: code-after-unconditional-return
    return "red"


def resolve(key: str):
    key = os.path.join(path, "keys", key)
    # ok: code-after-unconditional-return
    return key


def resolve(key: str) -> str:
    key = os.path.join(path, "keys", key)
    # ok: code-after-unconditional-return
    return key


def resolve(key: str) -> str:
    key = os.path.join(path, "keys", key)
    # ok: code-after-unconditional-return
    return key, key


# ruleid: return-not-in-function
return (a, b)
