from apis import api
from .user_project import resource as res1
from .service import resource as res2
from .tag import resource as res3
from .cache import resource as res4
from .ssl import resource as res5
from .backup import resource as res6
from .monitoring import resource as res7
# # ...
# from .resourceX import resource as resX


# Add resource namespaces
api.add_namespace(res1)
api.add_namespace(res2)
api.add_namespace(res3)
api.add_namespace(res4)
api.add_namespace(res5)
api.add_namespace(res6)
api.add_namespace(res7)
# # ...
# api.add_namespace(resX)
