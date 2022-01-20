import requests
import json
import time
from . import config
'''
this class for authonticate in keyston
'''
class Authonticate():
    def __init__(self):
        self.user_name=config.user_name
        self.password=config.password
        self.project_scope_name=config.project_scope_name
        self.expire_time=None
        self.domain_id=config.domain_id
        self.token=None

    def getRequestBody(self):
        body={
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name": self.user_name,
                            "domain": { "id": "default" },
                            "password": self.password
                        }   
                    }
                },
                "scope": {
                    "project": {
                    "name": self.project_scope_name,
                    "domain": { "id": self.domain_id }
                    }
                }
            }
        }
        return json.dumps(body)

    def getURL(self):
        return "http://{}:5000/v3/auth/tokens".format(config.url)
    
    '''
   this function for get token
    '''
    def getToken(self):
        if self.expire_time==None or self.expire_time < time.time():
            body=self.getRequestBody()
            header= {"Content-Type":"application/json"}
            r = requests.post(self.getURL(),headers=header,data = body,verify=False)
            self.authResponse=r.json()
            if r.status_code ==201:
                self.token=r.headers["X-Subject-Token"]
            else:
                self.status="failed"
                self.token=None
            self.expire_time=time.time()+1200
        return self.token

