from client import main
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(main.main())