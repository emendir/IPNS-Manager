import IPFS_API
from tqdm import tqdm
response = dict(IPFS_API.http_client.pin.ls())
cids = [e for e in response.get("Keys") if isinstance(e, str)]

selected_cids = []
for i in tqdm(range(len(cids))):
    i = 100
    cid = cids[i]
    try:
        if "lang" in IPFS_API.CatFile(cid).decode():
            # if "pinner_username_txbx" in IPFS_API.CatFile(cid).decode():
            selected_cids.append(cid)
    except:
        pass

selected_cids
