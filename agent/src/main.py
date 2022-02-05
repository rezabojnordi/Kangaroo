from flask import Flask,jsonify,json,request
from celery import Celery,chain,signature
from api.action_queue.main import run_shutdown,run_backup,run_start
import json


app = Flask(__name__)
simple_app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')



@app.route("/backups",methods=["POST"])
def backups():
    res = request.get_json()["server"]
    instance_name = res["instance_name"]
    instance_id = res["instance_id"]
    res = chain(run_shutdown.s(instance_name).set(queue="shutdown"),run_backup.s(instance_id).set(queue="backup")).apply_async()
    return res.id



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
