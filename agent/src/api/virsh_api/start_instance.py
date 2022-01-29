import libvirt
from . import checkStatus




def start_instance(domainName):
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