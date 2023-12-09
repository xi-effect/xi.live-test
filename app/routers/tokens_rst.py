from fastapi import APIRouter
from pydantic import BaseModel

from app.common.authorization import UserID, proxy_auth_dependency
from app.common.config import livekit
from app.common.livekitter import Grants

router = APIRouter(tags=["tokens"])


class TokenInput(BaseModel):
    token_name: str = "name"
    room_name: str


@router.post("/", dependencies=[proxy_auth_dependency])
def create_token(user_id: UserID, token_input: TokenInput) -> str:
    return livekit.create_access_token(  # type: ignore[no-any-return]
        identity=user_id,
        name=token_input.token_name,
        grants=Grants(
            room_join=True,
            room=token_input.room_name,
        ),
    ).to_jwt()
