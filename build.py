import os
for dirname, dirnames, filenames in os.walk("."):
    for filename in filenames:
        path = os.path.join(dirname, filename)
        if(filename[-2:] == "ui"):
            print(filename)
            os.system(f"pyuic5 {path} -o {path[:-2]}py")
os.system("pyinstaller --name='IPNS-Manager' --windowed --onefile --add-data='Icon.svg:.' --hidden-import=multiaddr.codecs.idna --hidden-import=multiaddr.codecs.uint16be LoadUI.py")
