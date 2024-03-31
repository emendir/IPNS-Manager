import ipfs_api
from threading import Thread
import os

from datetime import datetime

IPNS_RENEWAL_LEAD_HR = 24


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
                    self.ipfs_cid = ipfs_api.resolve_ipns_key(self.ipns_key_id)[
                        6:]
                except:
                    pass
            # resolve key on separate thread because if undefined it can take a minute
            Thread(target=ResolveKey, args=()).start()
            self.path = path

    def UpdateIPNS_Record(self, new_cid=None):
        """Publish self.path to IPFS (unless new_cid is specified)
        and update this IPNS Record to point to the new CID"""
        if new_cid:
            print("NEW CID", new_cid)
            self.ipfs_cid = new_cid
        elif not self.ipfs_cid:
            if os.path.exists(self.path):
                self.ipfs_cid = ipfs_api.publish(self.path)
        if not self.ipfs_cid:
            print(
                f"Warning: {self.ipns_key_name} we have no IPFS CID to update!")
            return
        print(self.ipns_key_name, "Updating IPNS Record")

        Thread(
            target=ipfs_api.update_ipns_record_from_cid,
            args=(self.ipns_key_name, self.ipfs_cid, "24h", "100h"),
            kwargs={'timeout': 300}
        ).start()

    def CheckIpnsStatus(self):
        try:
            expiry_date = ipfs_api.get_ipns_record_validity(self.ipns_key_id)
            validity_remaining_hrs = (
                expiry_date - datetime.utcnow()
            ).total_seconds() / 3600
        except ipfs_api.ipfshttpclient.exceptions.TimeoutError:
            print("Caught error")
            validity_remaining_hrs = 0
        print(self.ipns_key_name, validity_remaining_hrs)
        if validity_remaining_hrs < IPNS_RENEWAL_LEAD_HR:
            self.UpdateIPNS_Record()

    def DeleteIPNS_Record(self):
        ipfs_api.http_client.key.rm(self.ipns_key_name)

    def ChangeIPNS_Name(self, name):
        ipfs_api.http_client.key.rename(self.ipns_key_name, name)
        self.ipns_key_name = name
