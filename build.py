import shutil
import os
import platform
# converting *.ui files to *.py files
for dirname, dirnames, filenames in os.walk("."):
    for filename in filenames:
        path = os.path.join(dirname, filename)
        if(filename[-2:] == "ui"):
            print(filename)
            os.system(f"pyuic5 {path} -o {path[:-2]}py")
# shutil.rmtree("dist")

if (platform.system().lower() == "windows"):
    os.system("pyinstaller --name=IPNS-Manager --windowed --onefile --add-data=Icon.svg;. --hidden-import=multiaddr.codecs.ip4 --hidden-import=multiaddr.codecs.idna --hidden-import=multiaddr.codecs.uint16be LoadUI.py")
    shutil.move(os.path.join("dist", "IPNS-Manager.exe"),
                os.path.join("dist", f"IPNS-Manager_{platform.system().lower()}_{platform.machine().lower()}.exe"))
else:
    os.system("pyinstaller --name='IPNS-Manager' --windowed --onefile --add-data='Icon.svg:.' --hidden-import=multiaddr.codecs.ip4 --hidden-import=multiaddr.codecs.idna --hidden-import=multiaddr.codecs.uint16be LoadUI.py")
    shutil.move(os.path.join("dist", "IPNS-Manager"),
                os.path.join("dist", f"IPNS-Manager_{platform.system().lower()}_{platform.machine().lower()}"))
