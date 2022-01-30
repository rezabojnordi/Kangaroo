
import libvirt
from . import checkStatus
def shutdown(domainName):
    try:
        conn = libvirt.open("qemu:///system")
        #domainName = sys.argv[1]
        domain = conn.lookupByName(domainName)
        domain.shutdown()
        state, reason = domain.state()
        domainStatus = checkStatus(state, reason)
        if domainStatus == "Shutdown":
            return True
        else:
            return False
    except:
        return False



