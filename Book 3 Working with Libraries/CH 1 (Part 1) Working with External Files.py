"""
2 Main File Types

Text File : Contains plain text characters

-Plain text: .txt, .csv
-Source Code: .py, .html, .css, .js
-Data: .json, .xml

Binary File : Stores information in bytes

-Executable: .exe, .dmg, .bin
Images: .jpg, .png, .gif, .tiff, .ico
Video: .mp3, .m4v, .mp4. mov
Audio: .aif, .mp3 .mpa, .wav
Compressed .zip, .deb, .tar.gz
Font: .woff, .otf, .ttf
Document: .pdf, .docx, .xlsx
"""

"""

open(filename.ext[,mode])


»»  r:(Read): Opens the file but does not allow Python to make any changes. This
is the default mode and is used if you don’t specify a mode. If the file doesn’t
exist, Python raises a FileNotFoundError exception.

»»  r+:(Read/Write): Opens the file and allows Python to read and write to the file.

»»  a:(Append): Opens the file and allows Python to add content to the end of
the file but not change existing content. If the file doesn’t exist, this mode
creates the file.

»»  w:(Write): Opens the file and overwrites its contents, or creates the file if it
doesn’t exist.

»»  x:(Create): Creates the file if it doesn’t already exist. If the file does exist, it
raises a FileExistsError exception.

You can also specify the type of file you're opening or creating.
»»t: (Text): Opens the file as a text file and allows Python to read and write text.
»»b: (Binary): Opens the file as a binary file and allows Python to read and
write bytes.
"""