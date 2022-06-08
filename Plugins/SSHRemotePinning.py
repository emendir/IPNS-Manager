import os           # various utilities for interacting with operating system
import appdirs      # library for getting appdata dir
import json         # library for serialising python objects for appdata
import traceback    # library for accessing error logs
import socket       # library for opening network communications
import paramiko     # library for making SSH connections

# GUI framework libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QInputDialog

# importing the user interface created with Qt Designer saved as the
# 'SSHRemotePinningUI.ui' file as a class called SSHRemotePinningWidget
SSHRemotePinningWidget, QWidget = loadUiType(os.path.join(
    os.path.dirname(__file__), 'SSHRemotePinningUI.ui'))


class Plugin(QWidget, SSHRemotePinningWidget):
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
    plugin_friendly_name = "SSH Remote Pinning"
    # machine-preferred name for this plugin, preferably without spaces
    plugin_code_name = os.path.basename(__file__)[:-3]

    # SSH connection details for the computer
    # which this plugin shout to pin content to:
    pinner_username = ""
    pinner_ip = ""
    password = None

    def __init__(self, mainwindow):
        """This is the constructor for this Pulgin class, meaning that it 
        gets executed once when the plugin is loaded."""
        super(Plugin, self).__init__()
        self.setupUi(self)
        self.mainwindow = mainwindow  # reference to IPNS-Manager's QMainWindow

        # setting appdata paths
        self.appdata_dir = os.path.join(appdirs.user_data_dir(
        ), "IPNS-Manager", "Plugins", self.plugin_code_name)
        self.settings_path = os.path.join(self.appdata_dir, "settings.json")
        self.host_keys_path = os.path.join(self.appdata_dir, "known_hosts")
        if not os.path.exists(self.appdata_dir):
            os.makedirs(self.appdata_dir)

        self.LoadConfig()   # loading plugin settings from appdata

        # setting eventhandlers for UI elements
        self.pinner_ip_txbx.textEdited.connect(self.OnPinnerIPChanged)
        self.pinner_username_txbx.textEdited.connect(
            self.OnPinnerUserNameChanged)
        self.test_btn.clicked.connect(self.OnTestBtnClicked)

        # initialising SSH machinery
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        if os.path.exists(self.host_keys_path):
            self.ssh.load_host_keys(self.host_keys_path)
        self.TryToConnectSSH()  # test SSH connection using loaded settings

    # Functions to be run when the user updates an IPNS Site ------------------

    def PrePublish(self, source_path, old_ipfs_cid, ipns_key_id, ipns_key_name):
        """
        This function gets executed every time the user clicks a Site's
        'Update from Source' button, before the source is actually uploaded
        to IPFS. This allows you to manipulate the folder/file before it is
        actually published.
        """
        pass

    def PostPublish(self, source_path, old_ipfs_cid, new_ipfs_cid,
                    ipns_key_id, ipns_key_name):
        """
        This function gets executed every time the user clicks a Site's
        'Update from Source' button, after the source is uploaded to IPFS.
        This allows you to execute post-publishing tasks, such as in this case,
        pinning the newly published content on another computer.
        """
        if not self.TryToConnectSSH(True):  # connect via SSH to pinning computer
            return
            # run the 'ipfs pin add cid' command on the other computer
            stdin, stdout, stderr = self.ssh.exec_command(
                f"ipfs pin add {new_ipfs_cid}")
            print(stdout.read())
            # unpin the old now outdated content (if the content changed at all)
            if old_ipfs_cid != new_ipfs_cid:
                stdin, stdout, stderr = self.ssh.exec_command(
                    f"ipfs pin rm {old_ipfs_cid}")
                print(stdout.read())

    # AppData loading and saving ----------------------------------------------

    def LoadConfig(self):
        """Load the user's settings for this plugin from appdata."""
        if os.path.exists(self.settings_path):
            with open(os.path.join(self.appdata_dir, "settings.json"), "r") as settings_file:
                data = json.loads(settings_file.read())
                self.pinner_ip = data["pinner_ip"]
                self.pinner_username = data["pinner_username"]
            self.pinner_ip_txbx.setText(self.pinner_ip)
            self.pinner_username_txbx.setText(self.pinner_username)

    def SaveConfig(self):
        """Save the user's settings for this plugin to appdata."""
        with open(self.settings_path, "w+") as settings_file:
            settings_file.write(json.dumps({"pinner_ip": self.pinner_ip,
                                "pinner_username": self.pinner_username}))

    # UI elements' eventhandler -----------------------------------------------

    def OnPinnerUserNameChanged(self, event_args):
        self.pinner_username = self.pinner_username_txbx.text()
        self.SaveConfig()

    def OnPinnerIPChanged(self, event_args):
        self.pinner_ip = self.pinner_ip_txbx.text()
        self.SaveConfig()

    def OnTestBtnClicked(self, event_args):
        self.TryToConnectSSH()

    # SSH connection machinery ------------------------------------------------

    def TryToConnectSSH(self, keep_connection_open=False):
        self.test_btn.setStyleSheet("")
        if self.pinner_ip == "":
            return
        success = self.ConnectSSH(keep_connection_open)
        if success:
            self.test_btn.setStyleSheet("background: rgb(20,150,20)")
        else:
            self.test_btn.setStyleSheet("background: rgb(150,20,20)")
        return success

    def ConnectSSH(self, keep_connection_open=False):
        """Tries to make an SSH connection to the specified computer,
        taking care of SSH key management (for checking against
        man-in-the-middle attacks)"""
        # Get computer's SSH public key
        sock = socket.socket()
        sock.connect((self.pinner_ip, 22))
        trans = paramiko.transport.Transport(sock)
        trans.start_client()
        current_key = trans.get_remote_server_key()

        if not current_key:
            print(
                f"cannot create an SSH connection to the computer  \
{self.pinner_ip}")
            return False
        known_keys = self.ssh.get_host_keys()
        # if we've connected to this computer before
        if self.pinner_ip in known_keys.keys():
            # if we've never seen this key for this computer before, warn  user
            if not current_key in known_keys[self.pinner_ip].values():
                button_reply = QMessageBox.question(
                    self,
                    'Warning',
                    f"We have connected to this computer before, and now it  \
has a new SSH key. This should be normal only if you reinstalled \
that computer's OS, changed its SSH key manually or something \
similar. Otherwise, you might be under a man-in-the-middle attach.{os.linesep} \
Known keys:{os.linesep} \
{os.linesep.join([key.get_base64() for key in known_keys[self.pinner_ip].values()])}{os.linesep} \
New key:{os.linesep} {current_key.get_base64()}{os.linesep} \
Do you wish to proceed?",
                    QMessageBox.Yes | QMessageBox.No)
                if button_reply == QMessageBox.Yes:
                    known_keys.add(
                        self.pinner_ip, current_key.get_name(), current_key)
                    known_keys.save(self.host_keys_path)
                else:
                    return False
        else:  # if we've never connected to this computer before
            button_reply = QMessageBox.question(
                self,
                'Info',
                f"We don't remember connecting to this computer before. \
If you would like to check that computer's SSH key before connecting, \
here it is:{os.linesep} \
{current_key.get_base64()}{os.linesep} \
Shall we proceed?",
                QMessageBox.Yes | QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                known_keys.add(
                    self.pinner_ip, current_key.get_name(), current_key)
                known_keys.save(self.host_keys_path)
            else:
                return False
        try:
            # password request and connection attempt loop
            while True:
                try:
                    self.ssh.connect(
                        self.pinner_ip,
                        username=self.pinner_username,
                        password=self.password
                    )
                    break
                except paramiko.AuthenticationException:
                    self.password, ok = QInputDialog.getText(
                        self.mainwindow,
                        'Enter Password',
                        f'Enter your password for  \
{self.pinner_username}@{self.pinner_ip}'
                    )
                    if not ok:
                        return False
            # if we were just testing, close SSH connection
            if not keep_connection_open:
                self.ssh.close()
            return True
        except:
            print(f"Error while attempting to open SSH connection  \
to {self.pinner_ip}")
            print(traceback.format_exc())
            return False
