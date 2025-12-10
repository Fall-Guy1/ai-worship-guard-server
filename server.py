import asyncio
import websockets
import json
import random

# Simple demo analyzer (returns a fake AI score)
# We can upgrade this later to full audio fingerprinting.

async def handle(ws):
    print("Client connected")

    async for message in ws:
        try:
            data = json.loads(message)
        except:
            continue

        if data.get("action") == "scan":
            # Fake score for demo — 0.0 to 1.0
            score = round(random.uniform(0.0, 1.0), 2)
            print("Sending score:", score)

            await ws.send(json.dumps({"score": score}))

async def main():
    print("Server running on ws://0.0.0.0:10000")
    async with websockets.serve(handle, "0.0.0.0", 10000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
