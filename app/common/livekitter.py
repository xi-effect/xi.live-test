from datetime import timedelta
from typing import Final

from aiohttp import ClientTimeout
from livekit.api import AccessToken, LiveKitAPI, VideoGrants  # type: ignore
from livekit.api.access_token import DEFAULT_TTL  # type: ignore

DEFAULT_TIMEOUT: Final[ClientTimeout] = ClientTimeout(total=60)


class LiveKit(LiveKitAPI):  # type: ignore
    def __init__(
        self,
        url: str,
        api_key: str,
        api_secret: str,
        *,
        timeout: ClientTimeout = DEFAULT_TIMEOUT,
    ) -> None:
        self.url = url
        self.api_key = api_key
        self.api_secret = api_secret
        super().__init__(
            url=url,
            api_key=api_key,
            api_secret=api_secret,
            timeout=timeout,
        )

    def create_access_token(
        self,
        grants: VideoGrants | None = None,
        name: str = "",
        metadata: str = "",
        sha256: str = "",
        ttl: timedelta = DEFAULT_TTL,
        identity: str = "",
    ) -> AccessToken:
        token = AccessToken(self.api_key, self.api_secret)

        token.claims.name = name
        token.claims.metadata = metadata
        token.claims.sha256 = sha256
        if grants is not None:
            token.claims.video = grants

        token.identity = identity
        token.ttl = ttl
        return token
