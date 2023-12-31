def test1():
    # ruleid:hardcoded-tmp-path
    f = open("/tmp/blah.txt", "w")
    f.write("hello world")
    f.close()


def test2():
    # ruleid:hardcoded-tmp-path
    f = open("/tmp/blah/blahblah/blah.txt")
    f.read()
    f.close()


def test3():
    # ok:hardcoded-tmp-path
    f = open("./tmp/blah.txt", "w")
    f.write("hello world")
    f.close()


def test3a():
    # ok:hardcoded-tmp-path
    f = open("/var/log/something/else/tmp/blah.txt", "w")
    f.write("hello world")
    f.close()


def test4():
    # ruleid:hardcoded-tmp-path
    with open("/tmp/blah.txt") as fin:
        fin.read()


def test5():
    # ok:hardcoded-tmp-path
    with open("./tmp/blah.txt", "w") as fout:
        fout.write("hello world")
