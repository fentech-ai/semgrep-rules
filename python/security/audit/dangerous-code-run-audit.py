x = object()

# ruleid:identical-is-comparison
if x is x:

# ok:identical-is-comparison
if x is None:
    pass

# ok:identical-is-comparison
if type(X) is str:
    pass

# ok:identical-is-comparison
if x is True:
    pass

# ok:identical-is-comparison
if x is False:
    pass

# ruleid: string-is-comparison
if x is "hello there":
    pass

# ruleid: string-is-comparison
if "hello there" is x:
    pass

# ok: string-is-comparison
if x is "":
    pass
r()
    # ruleid: dangerous-interactive-code-run-audit
    pl = code.compile_command(payload)
    inperpreter.runcode(pl)


def run_payload4(payload: str) -> None:
    inperpreter = code.InteractiveInterpreter()
    # ruleid: dangerous-interactive-code-run-audit
    inperpreter.runsource(payload)


def ok1() -> None:
    console = code.InteractiveConsole()


def ok2() -> None:
    inperpreter = code.InteractiveInterpreter()


def ok3() -> None:
    inperpreter = code.InteractiveInterpreter()
    inperpreter.runcode(pl)


def ok4() -> None:
    inperpreter = code.InteractiveInterpreter()
 {} .".format(sys.argv[1]), shell=True)


def bad4():
    # ruleid:dangerous-subprocess-use-tainted-env-args
    subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True, cwd="/home/user")


def bad5():
    # ruleid:dangerous-subprocess-use-tainted-env-args
    subprocess.run("grep -R {} .".format(sys.argv[1]), shell=True)


def bad6():
    # ruleid:dangerous-subprocess-use-tainted-env-args
    subprocess.run(["bash", "-c", sys.argv[1]], shell=True)


def bad7():
    cmd = sys.argv[1]
    # ruleid:dangerous-subprocess-use-tainted-env-args
    subprocess.call([cmd[0], cmd[1], "some", "args"])


def fn1(user_input):
    cmd = user_input.split()
    # fn:dangerous-subprocess-use-tainted-env-args
    subprocess.call([cmd[0], cmd[1], "some", "args"])


def fn2(payload: str) -> None:
    with tempfile.TemporaryDirectory() as directory:
        python_file = Path(directory) / "hello_world.py"
        python_file.write_text(
            textwrap.dedent(
                """
        name = input()
    """
            )
        )
        # fn:dangerous-subprocess-use-tainted-env-args
        program = subprocess.Popen(
            ["python2", str(python_file)], stdin=subprocess.PIPE, text=True
        )
        program.communicate(input=payload, timeout=1)
