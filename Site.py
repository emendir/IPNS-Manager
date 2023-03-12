import ipfs_api
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
            self.ipns_key_id = ipfs_api.create_ipns_record(name)
        else:
            self.ipns_key_id = id

            def ResolveKey():
                try:
                    self.ipfs_cid = ipfs_api.resolve_ipns_key(self.ipns_key_id)[6:]
                except:
                    pass
            # resolve key on separate thread because if undefined it can take a minute
            _thread.start_new_thread(ResolveKey, ())
            self.path = path

    def UpdateIPNS_Record(self, new_cid=""):
        """Publish self.path to IPFS (unless new_cid is specified)
        and update this IPNS Record to point to the new CID"""
        print("NEW CID", new_cid)
        if new_cid:
            self.ipfs_cid = new_cid
        else:
            self.ipfs_cid = ipfs_api.publish(self.path)
        _thread.start_new_thread(ipfs_api.update_ipns_record_from_hash,
                                 (self.ipns_key_name, self.ipfs_cid, "1000h", "1000h"))

    def DeleteIPNS_Record(self):
        ipfs_api.http_client.key.rm(self.ipns_key_name)

    def ChangeIPNS_Name(self, name):
        ipfs_api.http_client.key.rename(self.ipns_key_name, name)
        self.ipns_key_name = name
