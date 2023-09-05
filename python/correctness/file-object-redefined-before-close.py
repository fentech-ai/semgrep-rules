def test1():
    # ruleid:file-object-redefined-before-close
    fin = open("file1.txt")
    fin.read()
    fin = open("file2.txt")
    fin.read()
    fin.close()


def test2():
    # ok:file-object-redefined-before-close
    fin = open("file1.txt")
    fin.read()
    fin.close()

    fin = open("file2.txt")
    fin.read()
    fin.close()
