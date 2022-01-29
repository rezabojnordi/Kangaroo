from flask import Flask

from openstack.authonticate import Authonticate
from openstack.info_host import InfoHost
from agent_request import request_to_agent


def change(instance_id):
    auth = Authonticate()
    info_host = InfoHost(instance_id)
    print(info_host.detailHost())
    #print(auth.getToken())
    instance_name = str(info_host.detailHost()["instance_name"])
    agent = str(info_host.detailHost()["compute"] + "{}").format(".iranserver.com")
    print(instance_name)
    #request_to_agent(agent,instance_id)


change('2ad4e572-afe5-40fe-8afe-4c63e9d17d7a')
