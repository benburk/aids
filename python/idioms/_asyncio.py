import asyncio


async def foo() -> None:
    await asyncio.sleep(1)


loop = asyncio.get_event_loop()
loop.run(foo())
