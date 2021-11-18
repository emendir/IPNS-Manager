import IPFS_API
import _thread


class Site:
    """Site objects represent IPNS content (Sites) which you're hosting on IPFS using an IPNS key.
    It has a local folder/file (this classes 'path' attribute) on your computer associated with it,
    so that this program can upload changes to it to IPFS and update the IPNS record for you.
    """
    path = ""
    ipfs_cid = ""
    ipns_key_id = ""
    ipns_key_name = ""

    def __init__(self, name: str, id="", path=""):
        self.ipns_key_name = name
        # Create new record if id parameterr is left empty
        if id == "":
            self.ipns_key_id = IPFS_API.CreateIPNS_Record(name)
        else:
            self.ipns_key_id = id

            def ResolveKey():
                self.ipfs_cid = IPFS_API.ResolveIPNS_Key(self.ipns_key_id)[6:]
            # resolve key on separate thread because if undefined it can take a minute
            _thread.start_new_thread(ResolveKey, ())
            self.path = path

    def UpdateIPNS_Record(self):
        """Publish the new IPFS CID associated with this IPNS Record"""
        self.ipfs_cid = IPFS_API.Upload(self.path)
        _thread.start_new_thread(IPFS_API.UpdateIPNS_RecordFromHash,
                                 (self.ipns_key_name, self.ipfs_cid, "1000h", "1000h"))

    def DeleteIPNS_Record(self):
        IPFS_API.ipfs.key.rm(self.ipns_key_name)

    def ChangeIPNS_Name(self, name):
        IPFS_API.ipfs.key.rename(self.ipns_key_name, name)
        self.ipns_key_name = name
