# 12.4 Text versus Binary Files:

# Text versus Binary Files
# Text files and binary files are two types of files that can be handled in Python.
# 
#  Here are the key differences between them:

# Text Files: These are human-readable files containing text (characters). They are structured as a sequence of lines, each containing a sequence of characters.
# This includes programming source code, HTML files, and more. When you open a text file in a text editor, it displays the contents as text.

# Binary Files: These are not designed to be human-readable.
# They may contain any type of data encoded in binary form for computer processing, such as images, audio files, executable files, etc.
#  When you open a binary file in a text editor, it often appears as a jumble of special characters.


# In Python, you can open both text and binary files using the open() function. 
# The mode parameter determines how the file is opened: ‘t’ for text (default) and ‘b’ for binary.
# For example, ‘rb’ opens a file for reading in binary mode, while ‘wt’ opens a file for writing text.

# When working with text files in Python, it handles the encoding and decoding of the text into the specific character set (like UTF-8).
# But for binary files, no such encoding/decoding is performed. The data is read from or written to the file directly. 
# This makes binary mode suitable for non-text files like images or executable files. 
# It’s also useful when you need to preserve the exact bytes of the file, such as a checksum operation.

#  In network automation, text files are often used for storing configuration commands, logs, etc.,
#  while binary files could be used for firmware images, packet captures, etc.
#  It’s important to choose the right type of file and mode based on the data you are working with.