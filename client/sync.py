import aiohttp

async def sync(url, outgoing_data: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=outgoing_data)
        async with session.get(url) as resp:
           incoming_data = await resp.text()
           print(resp.text)

    return incoming_data