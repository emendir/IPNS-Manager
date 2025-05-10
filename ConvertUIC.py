"""Convert all this project's *.ui and *.qrc files to python."""
import os


def run():
    for dirname, dirnames, filenames in os.walk("."):
        for filename in filenames:
            path = os.path.join(dirname, filename)
            if (filename.split(".")[-1] == "ui"):
                print(filename)
                os.system(f"pyuic5 {path} -o {path[:-2]}py")
            elif (filename.split(".")[-1] == "qrc"):
                print(filename)
                os.system(f"pyrcc5 {path} -o {path[:-4]}_rc.py")


if __name__ == "__main__":
    run()
