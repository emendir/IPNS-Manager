import os
for dirname, dirnames, filenames in os.walk("."):
    for filename in filenames:
        path = os.path.join(dirname, filename)
        if(filename[-2:] == "ui"):
            print(filename)
            os.system(f"pyuic5 {path} -o {path[:-2]}py")
