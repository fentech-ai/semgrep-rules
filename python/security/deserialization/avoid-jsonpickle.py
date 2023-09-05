import jsonpickle


def run_payload(payload: str) -> None:
    # ruleid: avoid-jsonpickle
    jsonpickle.decode(payload)


def ok():
    # ok: avoid-jsonpickle
    jsonpickle.decode("foobar")
