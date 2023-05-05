from __project__ import version, project_name
import shutil
import os
import platform
hidden_imports = [
    "multiaddr.codecs.ip4",
    "multiaddr.codecs.idna",
    "multiaddr.codecs.uint16be",
]

# converting *.ui files to *.py files
for dirname, dirnames, filenames in os.walk("."):
    if dirname == "./Plugins" or "./.git" in dirname:
        continue
    for filename in filenames:
        path = os.path.join(dirname, filename)
        if(filename[-2:] == "ui"):
            print(filename)
            os.system(f"pyuic5 {path} -o {path[:-2]}py")
# shutil.rmtree("dist")

# if (platform.system().lower() == "windows"):
#     os.system("pyinstaller --name=IPNS-Manager --windowed --onefile --add-data=IPNS-Manager-Icon.svg;. --hidden-import=multiaddr.codecs.ip4 --hidden-import=multiaddr.codecs.idna --hidden-import=multiaddr.codecs.uint16be LoadUI.py")
#     shutil.move(os.path.join("dist", "IPNS-Manager.exe"),
#                 os.path.join("dist", f"IPNS-Manager_{platform.system().lower()}_{platform.machine().lower()}.exe"))
# else:
#     os.system("pyinstaller --name='IPNS-Manager' --windowed --onefile --add-data='IPNS-Manager-Icon.svg:.' --hidden-import=multiaddr.codecs.ip4 --hidden-import=multiaddr.codecs.idna --hidden-import=multiaddr.codecs.uint16be LoadUI.py")
#     shutil.move(os.path.join("dist", "IPNS-Manager"),
#                 os.path.join("dist", f"IPNS-Manager_{platform.system().lower()}_{platform.machine().lower()}"))

if (platform.system().lower() == "windows"):
    cmd = f"pyinstaller --name={project_name} --windowed --onefile --add-data=IPNS-Manager-Icon.svg;. __main__.py"
    for lib in hidden_imports:
        cmd += f" --hidden-import={lib}"
    os.system(cmd)
    shutil.move(os.path.join("dist", f"{project_name}.exe"),
                os.path.join("dist", f"{project_name}_v{version}_{platform.system().lower()}_{platform.machine().lower().replace('x86_64', 'amd64')}.exe"))
else:
    cmd = f"pyinstaller --name='{project_name}' --windowed --onefile --add-data='IPNS-Manager-Icon.svg:.' __main__.py"
    for lib in hidden_imports:
        cmd += f" --hidden-import={lib}"
    os.system(cmd)
    shutil.move(os.path.join("dist", project_name),
                os.path.join("dist", f"{project_name}_v{version}_{platform.system().lower()}_{platform.machine().lower().replace('x86_64', 'amd64')}.AppImage"))
