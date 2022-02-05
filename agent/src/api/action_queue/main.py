import time
import os
import sys
from celery import Celery
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger
from api.virsh_api.shutdown_instance import shutdown
from api.backup.main import Backup



logger = get_task_logger(__name__)



app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')
app.conf.task_routes = {'app.tasks.run_shutdown' : {'queue': 'shutdown'},
  'app.tasks.run_backup' : {'queue': 'backup'},
  'app.tasks.run_start' : {'queue': 'run_start'}
  
  }


@app.task(name='shutdown')
def run_shutdown(instance_name):
    print("44444",instance_name)
    #print("tttt666t",ansible_role)
    #cmd = 'ansible-playbook test.yml'
    #os.system(cmd)
    result = shutdown(instance_name)
    return instance_name


@app.task(name='backup')
def run_backup(instance_name,instance_id):
    #instance_id,instance_name
    bk = Backup(instance_id,instance_name)
    dump_xml = bk.dump_xml()
    #os.system(cmd)
    return True


@app.task()
def run_start(instance_name):
    pass
    # result = start(instance_name)
    # #os.system(cmd)
    # return result




