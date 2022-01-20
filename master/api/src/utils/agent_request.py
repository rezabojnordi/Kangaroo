import requests
import json
import time




def request_to_agent(url_agent,body):
    print("=========",url_agent,body)
    header= {"Content-Type":"application/json"}
    r = requests.post(create_url(url_agent),headers=header,data = make_body(body),verify=False)
    return r

def create_url(url):
    return "http://{}:8774/v1.0/agent".format(url)


def make_body(body):
    scope ={
            "project": {
                "instance_id": body }}
    return "scope"

