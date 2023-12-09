from fastapi import APIRouter
from pydantic import BaseModel

from app.common.authorization import UserID, proxy_auth_dependency
from app.common.config import LIVEKIT_URL, livekit
from app.common.livekitter import Grants

router = APIRouter(tags=["tokens"])


class TokenInput(BaseModel):
    username: str = "name"
    room_name: str


class TokenResponse(BaseModel):
    token: str
    demo_url: str


DEMO_BASE_URL = "https://meet.livekit.io/custom"


@router.post("/", dependencies=[proxy_auth_dependency])
def create_token(user_id: UserID, token_input: TokenInput) -> TokenResponse:
    token_jwt = livekit.create_access_token(
        identity=user_id,
        name=token_input.username,
        grants=Grants(
            room_join=True,
            room=token_input.room_name,
        ),
    ).to_jwt()
    return TokenResponse(
        token=token_jwt,
        demo_url=f"{DEMO_BASE_URL}?liveKitUrl={LIVEKIT_URL}&token={token_jwt}",
    )
