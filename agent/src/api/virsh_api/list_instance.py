import libvirt
from . import checkStatus



def list_instance(domainStatus):
    conn = libvirt.open("qemu:///system")
    listDomain = conn.listAllDomains(0)
    print("{:40}{:32}{:15}".format("UUID", "NAME", "STATUS"))
    object_instance_list = []
    for domain in listDomain:
        domainName = domain.name()
        domainUUID = domain.UUIDString()
        object_instance_list.append({
            "domainUUID":domainUUID,
            "domainName":domainName,
            "domainStatus":domainStatus
        })
    return object_instance_list