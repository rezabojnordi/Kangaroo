from flask_restx import fields


class pist():
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c


data_structure = {
    "_id": "ObjectId",
    "user_name": "String",
    "project_name": "String",
    "domain": {
        "domain_name": "Domain",
        "https_enabled": "Boolean",
    },
    "services": [
        "filemanager": {"status": "String"},
        "filemanager": {"status": "String"},
        "filemanager": {"status": "String"},
    ]
}



{
    "_id" : ObjectId("61d08333d15397dfe239d538"),
    "project_id" : "morteza-lazarus",
    "database" : {
        "status" : "successful",
        "password" : "$3kur3",
        "project_sql_import" : false,
        "message" : {}
    },
    "domain_https" : true,
    "domain_name" : "lazarus.com",
    "filemanager" : {
        "status" : "successful",
        "password" : "baloot",
        "message" : {}
    },
    "nginx" : {
        "status" : "successful",
        "cache" : {
            "cache_valid" : 24
        },
        "certificate" : {
            "pub" : "string",
            "priv" : "string"
        },
        "message" : {}
    },
    "status" : "created",
    "storage" : {
        "status" : "successful",
        "quota_size" : 10,
        "message" : {}
    },
    "tag" : "verified",
    "wordpress" : {
        "status" : "successful",
        "password" : "$3kur3",
        "project_wordpress_import" : false,
        "message" : {}
    }
}