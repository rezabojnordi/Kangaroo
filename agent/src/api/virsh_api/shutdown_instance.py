
import libvirt
from api.virsh_api.checkStatus import checkStatus
def shutdown(domainName):
    try:
        conn = libvirt.open("qemu+ssh://compute5/system")
        #domainName = sys.argv[1]
        domain = conn.lookupByName(domainName)
        state, reason = domain.state()
        domainStatus = checkStatus(state, reason)
        print("***********",domainStatus)
        if domainStatus == "Started":
            domain.shutdown()
            return True
        else:
            return False
    except:
        return False



