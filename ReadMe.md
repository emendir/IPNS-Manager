# IPNS-Manager
IPFS-Manager is a GUI program for managing [IPFS (InterPlanetary File System)](https://ipfs.io) name keys. Its purpose is to make it easier to manage websites (and other content) hosted on IPFS with IPNS keys (IPFS Name System).

Built with the [PyQt5](https://pypi.org/project/PyQt5/) wrapper for the Qt graphics framework and the [IPFS-Toolkit](https://github.com/emendir/IPFS-Toolkit-Python) API for IPFS. 

## Prerequisite Knowledge and Understanding
This program is built for people who work with IPFS and understand the basic concepts of how it works, including [IPNS (InterPlanetary Name System)](http://docs.ipfs.io.ipns.localhost:8080/concepts/ipns/).

## Installation
You can download and run the binary in the dist folder if you're using a Linux x86_64 computer (tested on Ubuntu 20). If you are using a different operating system, you can run the program from source.

### Run from Source
- This program is written in the Python programming language. Install it and its package manager pip. Use at a version of at least 3.7.

  On Debian-based Linux systems, install with:  
  `sudo apt install python3`  
  `sudo apt install python3-pip`

  On windows, it is recommended not to install python from its app store as that has in some tests led to difficult-to-find-problems. Download it from the official website instead: https://python.org.

- Install the Python packages (libraries) which this project depends on:  
  `pip install PyQt5>=5.12`  
  `pip install IPFS-Toolkit>=0.1.4`
  (you may need to use `pip3` instead of `pip` in these two commands)
  

  On Linux, you may need to first run:
  `sudo apt install pyqt5-dev`

- Download the source code:  
  from IPFS: `ipfs get $(ipfs name resolve k2k4r8ksqdoku10pkm3ftt4d5c8svd9brfm22255uk3ho0sym169l8xi) -o IPNS-Manager`  
  from Github: `git clone https://github.com/emendir/IPNS-Manager`
- Make sure IPFS is running (`ifps daemon`), and run the project:  
`python3 IPNS-Manager`  
or (on some systems)  
`python IPNS-Manager`

Tested on Ubuntu-20 with Python3.8 and ipfs v0.9.1.

## Usage
### Adding Sites
Make sure IPFS is running on your computer before you run this program.

- Click on the "New Site" button at the bottom of the Sites page, enter a name for the Site (this name is only used on your computer for you to call your Site, and you will always be able to change it laterr). A new IPNS key will be automatically generated and displayed in the new box that appears in the page's Sites list.
- Add a source path for your Site by pressing the "source path" button to choose a file or folder or by pasting the path to the source of your website/other content in the field next to the button.
- Click the "Update from Source" button to upload the Site source to IPFS and assgn it to the IPNS key.
- You can view the Site on IPFS in your browser by clicking one of the "Open in Browser" buttons. The upper button opens the Site using its CID, wheras the lower button opens the Site using its IPNS key (which may take a longer time to load).

![](Screenshots/NewSite.png)![](Screenshots/AddedSource.png)

### Adding Custom Code
You can add your own Python code to be executed whenever you press a Site's "Update from Source". At the bottom of the IPNS-Manager window, press the "Code" tab. This will open a new view with a field in which you can paste a small python script. In this code, you can access the newly updated Site's data using the following variables:

    source_path  
    old_ipfs_cid  
    new_ipfs_cid  
    ipns_key_id  
    ipns_key_name 

You also have access to the [IPFS-Toolkit](https://ipfs.io/ipns/k2k4r8m2dzqi5s8jm3shm77sr1728ex7bsds0fk6e9gkf2ld2f3mnhcy) library (which contains the `IPFS_API`, `IPFS_DataTransmission` and `IPFS_LNS` modules), as well as all global variables in the LoadUI.py script from IPNS-Manager's source code.

![](Screenshots/Code.png)

Examples:

    # Write to log file:
    from datetime import datetime
    if new_ipfs_cid != old_ipfs_cid:
        with open(os.path.join(appdata_dir, "log"), "a+") as log_file:  # appdata_dir is a global varibale from LoadUI.py
            log_file.write(f"{datetime.now()}: {ipns_key_name}: {new_ipfs_cid}\n")

    # ssh into an always-online-computer with ipfs installed and pin the updated Site's CID  
    os.system(f"ssh -t -q admin@IP_ADDRESS 'ipfs pin rm {old_ipfs_cid}; ipfs pin add {new_ipfs_cid}; ipfs name resolve {ipns_key_id}'")
  
  The "Save" button saves your code to appdata. The "Update from Source" button however always executes the latest code you've written, regardless of whether it has been saved or not.
  To debug your code, run IPNS-Manager from a terminal window. All `print` statements in your code will be printed on the terminal.

# Links:
Naturally, this project is also hosted on IPFS.

Website: https://ipfs.io/ipns/k2k4r8m303h5pjaz7m3fckizzr6lne00ha6kcs97n20ivg9bpm1eu072  
Source Code: https://ipfs.io/ipns/k2k4r8ksqdoku10pkm3ftt4d5c8svd9brfm22255uk3ho0sym169l8xi