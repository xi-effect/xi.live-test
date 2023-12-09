from typing import Annotated

from fastapi import Depends
from fastapi.security import APIKeyHeader

proxy_auth_scheme = APIKeyHeader(name="X-User-ID")
proxy_auth_dependency = Depends(proxy_auth_scheme)
UserID = Annotated[str, proxy_auth_dependency]
