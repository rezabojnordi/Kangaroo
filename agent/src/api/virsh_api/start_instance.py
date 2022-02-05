import libvirt
from api.virsh_api.checkStatus import checkStatus


def start(domainName):
    conn = libvirt.open("qemu:///system")
    domain = conn.lookupByName(domainName)
    domain.create()
    print("%s Started" % domainName)
    state, reason = domain.state()
    domainStatus = checkStatus(state, reason)
    if domainStatus == "Started":
        return True
    else:
        return False