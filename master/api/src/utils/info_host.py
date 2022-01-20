import requests
from authonticate import Authonticate
from config import config

class InfoHost():
    def __init__(self,instance_id):
        self.instance_id = instance_id

    def getURL(self):
        return "http://{}:8774/v2.1/servers/".format(config.url)

    def detailHost(self):
        self.auth=Authonticate()
        header= {"X-Auth-Token":self.auth.getToken(),"Content-Type":"application/json"}
        r = requests.get(self.getURL()+"/%s"%self.instance_id , headers=header,verify=False)
        response=r.json()
        return {
                "compute":response["server"]["OS-EXT-SRV-ATTR:host"],
                "instance_name": response["server"]["OS-EXT-SRV-ATTR:instance_name"],
                "status": response["server"]["status"],
                "project_id": response["server"]["tenant_id"]
            }
    
