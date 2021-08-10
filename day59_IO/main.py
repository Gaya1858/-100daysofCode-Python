'''
IO module
The io module provides the Python interfaces to stream handling.
The builtin open function is defined in this module.
 At the top of the I/O hierarchy is the abstract base class IOBase.
 It defines the basic interface to a stream.
'''
import io

new_text =" I am doing python data analysis"
file = io.StringIO(new_text)
bytes_stream = io.BytesIO(b'Hello from Journaldev\x0AHow are you?')
print(bytes_stream.getvalue())
bytes_stream.close()
print(file.read())
file.write("This is sometime boring!")
file.seek(0)
print(file.read())
# file = io.open("sample.txt", "rb", buffering = 5)
#
#
# file.seek(0)
# print(file.read())
# Close the file
file.close()