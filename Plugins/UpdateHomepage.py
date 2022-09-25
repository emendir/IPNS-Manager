"""
This file contains a plugin for IPNS-Manager that will automatically pin IPNS
Sites to another computer via an SSH connection whenever the user updates the
Site's content.

This plugin requires the SSHRemotePinningUI.ui file (which defubes the
graphical UI elements and their layout) to be in the same folder.
The SSHRemotePinningUI.ui was created with and can be edited with Qt Designer,
a GUI program for creating Qt GUIs. On linux, this can be installed by running:
sudo apt -y install qttools5-dev-tools
sudo apt -y install qttools5-dev
For other operating systes, check out Qt's website:
https://www.qt.io/download-open-source

You can use this plugin as a starting point for building your own plugins.
To do so, simply make copies of this file and SSHRemotePinningUI.ui in the same
directory, renaming the copies appropriately, and modify them accordingly.
This file is clearly documented, so if you are familiar with programming in
Python and using the Qt framework with Python via the PyQt5 library, you
should learn to understand how this plugin system works fairly quickly.
More explicit documetation is coming soon.
"""


import os           # various utilities for interacting with operating system
import IPFS_API


class Plugin:
    """
    This class must be called 'Plugin'. It inherits the user interface class
    'SSHRemotePinningWidget' created with QtDesigner in the
    'SSHRemotePinningUI.ui' file.
    This class 'Plugin' contains all the functionality for controlling the
    user-interface. Most significantly, however, this class contains the
    functions 'PrePublish()' and 'PostPublish()', which get executed before and
    after a site is updated in IPNS-Manager's main page respectively.
    """
    # human readable name for this plugin, any characters allowed:
    plugin_friendly_name = "Update Homepage"
    # machine-preferred name for this plugin, preferably without spaces
    plugin_code_name = os.path.basename(__file__)[:-3]

    # SSH connection details for the computer
    # which this plugin shout to pin content to:
    pinner_username = ""
    pinner_ip = ""
    password = None

    def __init__(self):
        """This is the constructor for this Pulgin class, meaning that it 
        gets executed once when the plugin is loaded."""

    # Functions to be run when the user updates an IPNS Site ------------------

    def PrePublish(self, source_path, old_ipfs_cid, ipns_key_id, ipns_key_name):
        """
        This function gets executed every time the user clicks a Site's
        'Update from Source' button, before the source is actually uploaded
        to IPFS. This allows you to manipulate the folder/file before it is
        actually published.
        """
        if ipns_key_id != "k2k4r8nismm5mmgrox2fci816xvj4l4cudnuc55gkfoealjuiaexbsup":
            return

        sites = [
            ['/mnt/Uverlin/Programming/IPFS-Toolkit', 'IPFS-Toolkit'],
            ['/mnt/Uverlin/Programming/Brenthy', 'Brenthy'],
            ['/mnt/Uverlin/Programming/IPNS-Manager', 'IPNS-Manager'],
            ['/mnt/Uverlin/Programming/QR-ScanGen', 'QR-ScanGen'],
            ['/mnt/Uverlin/Programming/PupilCore/CursorControl', 'PupilCore-CursorControl'],
            ['/mnt/Uverlin/Programming/PupilCore/WinkDetection', 'PupilCore-WinkDetection'],
            ['/mnt/Uverlin/Programming/Atom/export-project-html', 'Atom--export-project-html']
        ]

        os.system("ipfs files rm -r /Homepage")
        # os.system("ipfs files mkdir /Homepage")

        website_cid = IPFS_API.Publish("/mnt/Uverlin/Website")
        os.system(f"ipfs files cp /ipfs/{website_cid}/ /Homepage")
        os.system(f"ipfs files mkdir /Homepage/Sites")

        website_cid
        for path, name in sites:
            cid = IPFS_API.Publish(os.path.join(path, "WebSite"))
            os.system(f"ipfs files cp /ipfs/{cid}/ /Homepage/Sites/{name}")

        from subprocess import Popen, PIPE

        proc = Popen(['ipfs', 'files', 'stat', '/Homepage'], stdout=PIPE)
        proc.wait()
        lines = []
        for line in proc.stdout:
            lines.append(line.decode('utf-8'))
        return {"ipfs_cid": lines[0].strip("\n")}

    def PostPublish(self, source_path, old_ipfs_cid, new_ipfs_cid,
                    ipns_key_id, ipns_key_name):
        """
        This function gets executed every time the user clicks a Site's
        'Update from Source' button, after the source is uploaded to IPFS.
        This allows you to execute post-publishing tasks, such as in this case,
        pinning the newly published content on another computer.
        """
        pass
