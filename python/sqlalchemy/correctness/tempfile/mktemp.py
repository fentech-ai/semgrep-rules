# ruleid: tempfile-insecure
x = tempfile.mktemp()
# ruleid: tempfile-insecure
x = tempfile.mktemp(dir="/tmp")
