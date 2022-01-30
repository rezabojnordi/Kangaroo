import libvirt
import sys


def dupxml(domainName):
    try:
        #conn = libvirt.openReadOnly(None)
        conn = libvirt.open("qemu+ssh://compute5/system")
    except libvirt.libvirtError:
        print('Failed to open connection to the hypervisor')
        sys.exit(1)
    try:
        dom0 = conn.lookupByName(domainName)
        return dom0.XMLDesc()
    except libvirt.libvirtError:
        print('Failed to find the main domain')
        sys.exit(1)


