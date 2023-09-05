fout = open("example.txt", "w")
# ok:writing-to-file-in-read-mode
fout.write("I'm writable!")
fout.close()


fout = open("example.txt")
# ruleid:writing-to-file-in-read-mode
fout.write("whoops, I'm not writable!")
fout.close()


with open("example.txt", "rb") as fout:
    # ruleid:writing-to-file-in-read-mode
    fout.write("whoops, me neither!")
