
import libvirt
from . import checkStatus



def reset_instance(domainName):
    conn = libvirt.open("qemu:///system")
    domain = conn.lookupByName(domainName)
    domain.reset()
    state, reason = domain.state()
    domainStatus = checkStatus(state, reason)
    if domainStatus == "reset":
        return True
    else:
        return False
