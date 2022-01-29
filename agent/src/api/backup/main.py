# Todo


class Backup():
    def __init__(self,instance_id,instance_name):
        self.instance_id = instance_id
        self.instance_name = instance_name



    def shutdown_instance(self):
        shutdown_instance(self.instance_name)
    


    def cp_instance(self):
        pass
    

    def change_status_on_db(self):
        pass
    


    



