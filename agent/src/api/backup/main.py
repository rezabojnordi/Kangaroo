# Todo


from api.virsh_api.dump_xml import dupxml
import os 
from api.config import config
import re
class Backup():
    def __init__(self,instance_id,instance_name,xml_file=""):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.xml_file = xml_file
        

    
    def dump_xml(self):
        xml = dupxml(self.instance_name)
        make_xml = make_xml_dump(self.instance_name,xml)
        if make_xml == True:
            split_path(xml)
            return True
        return False



def make_xml_dump(instance_name,xml):
    directory = "BACKUP"
    parent_dir = "/"
    path = os.path.join(parent_dir, directory)
    if not os.path.isdir(config.path):
        os.mkdir(path)
    with open(('{}/{}.{}').format(config.path,instance_name,"xml"), "w") as xml_file:
        xml_file.write(xml)
    return True
    



def split_path(xml):
    url = re.findall("((nova).instances).(.*)",xml)
    disk = "/tmp/var/lib/nova/instances/{}".format(url[0][2])
    base_image = "/tmp/var/lib/nova/instances/{}".format(url[1][2])
    obj = {
        "disk":disk.split("/disk'")[0],
        "base_image":base_image.replace("'/>"," ")
    }
    cp_instance(obj)
    return True



def cp_instance(url):
    try:
        print("cpppp")
        cp1 = os.system("cp -ar {} {}".format(url["disk"],"/BACKUP/"))
        cp2 = os.system("cp -ar {} {}".format(url["base_image"],"/BACKUP/"))
        if cp1 > 0 and cp2 > 0:
            #file not found
            return False
        return True
    except print(0):
        return False




