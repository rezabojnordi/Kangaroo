
import libvirt
from . import checkStatus



def reset_instance(domainName):
    conn = libvirt.open("qemu:///system")
    domain = conn.lookupByName(domainName)
    domain.reboot()
    state, reason = domain.state()
    domainStatus = checkStatus(state, reason)
    if domainStatus == "reboot":
        return True
    else:
        return False
