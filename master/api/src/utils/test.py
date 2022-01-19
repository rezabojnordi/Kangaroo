from flask import Flask
from authonticate import Authonticate
from info_host import InfoHost

def change(instance_id):
    auth=Authonticate()
    info_host = InfoHost(instance_id)
    print(auth)
    print(info_host.detailHost())
    print(auth.getToken())

change('instance_id')
