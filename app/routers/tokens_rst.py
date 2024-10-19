from fastapi import APIRouter
from pydantic import BaseModel

from app.common.authorization import ProxyUserID, ProxyUsername
from app.common.config import LIVEKIT_URL, livekit
from app.common.livekitter import Grants

router = APIRouter(tags=["tokens"])


class TokenResponse(BaseModel):
    token: str
    demo_url: str


DEMO_BASE_URL = "https://meet.livekit.io/custom"


@router.post("/")
def create_token(
    user_id: ProxyUserID,
    username: ProxyUsername,
    room_name: str = "room",
) -> TokenResponse:
    token_jwt = livekit.create_access_token(
        identity=user_id,
        name=username,
        grants=Grants(
            room_join=True,
            room=room_name,
        ),
    ).to_jwt()
    return TokenResponse(
        token=token_jwt,
        demo_url=f"{DEMO_BASE_URL}?liveKitUrl={LIVEKIT_URL}&token={token_jwt}",
    )
