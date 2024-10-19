from app.common.livekitter import LiveKit
from app.utils import getenv_or_error

LIVEKIT_URL: str = getenv_or_error("LIVEKIT_URL")
LIVEKIT_API_KEY: str = getenv_or_error("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET: str = getenv_or_error("LIVEKIT_API_SECRET")

livekit = LiveKit(LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
