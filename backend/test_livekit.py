import asyncio
import os
from dotenv import load_dotenv
from livekit import api


async def main():
    load_dotenv()

    url = os.getenv("LIVEKIT_URL")
    key = os.getenv("LIVEKIT_API_KEY")
    secret = os.getenv("LIVEKIT_API_SECRET")

    print("URL:", url)
    print("API KEY:", "SET" if key else "MISSING")
    print("API SECRET:", "SET" if secret else "MISSING")

    lk = api.LiveKitAPI(url, key, secret)

    try:
        request = api.ListRoomsRequest()
        rooms = await lk.room.list_rooms(request)

        print("LiveKit authentication: SUCCESS")
        print("Rooms returned:", len(rooms.rooms))

    except Exception as e:
        print("LiveKit authentication: FAILED")
        print(type(e).__name__, str(e))

    finally:
        await lk.aclose()


if __name__ == "__main__":
    asyncio.run(main())