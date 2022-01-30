# Todo

from api.virsh_api.shutdown_instance import shutdown
from api.virsh_api.dump_xml import dupxml
import os 
from api.config import config
class Backup():
    def __init__(self,instance_id,instance_name,xml_file=""):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.xml_file = xml_file
        


    

    def dump_xml(self):
        xml = dupxml(self.instance_name)
        make_xml_dump(self.instance_name,xml)
        url = split_path(xml)
        print(url)
        return xml
    


    def shut_instance(self):
        status = shutdown(self.instance_name)
        if status == True:
            return True
        else:
            return False
    


    def cp_instance(self):
        try:
            os.system("cp -ar /home/sae  /tmp/")
            return True
        except print(0):
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
    url = xml.split('/var/lib/nova/instances')
    return url




