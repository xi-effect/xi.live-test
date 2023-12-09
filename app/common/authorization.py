from typing import Annotated

from fastapi import Depends
from fastapi.security import APIKeyHeader

# TODO these return 403
proxy_auth_user_id_scheme = APIKeyHeader(name="X-User-ID", scheme_name="User ID")
proxy_auth_user_id_dependency = Depends(proxy_auth_user_id_scheme)
ProxyUserID = Annotated[str, proxy_auth_user_id_dependency]

proxy_auth_username_scheme = APIKeyHeader(name="X-Username", scheme_name="Username")
proxy_auth_username_dependency = Depends(proxy_auth_username_scheme)
ProxyUsername = Annotated[str, proxy_auth_username_dependency]
