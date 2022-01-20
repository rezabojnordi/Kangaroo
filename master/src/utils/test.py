from flask import Flask
from openstack.authonticate import Authonticate
from openstack.info_host import InfoHost
from agent_request import request_to_agent


def change(instance_id):
    auth = Authonticate()
    info_host = InfoHost(instance_id)
    print(auth)
    print(info_host.detailHost())
    print(auth.getToken())
    request_to_agent("172.20.8.6", instance_id)


change('3989c2fc-2dad-43b2-ac96-68bb886d13ca')
