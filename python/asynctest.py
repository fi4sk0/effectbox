import asyncio
import time

# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.


async def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        time.sleep(1)
        await asyncio.sleep(1)
        n -= 1

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]

print("running until complete")

loop.run_until_complete(asyncio.wait(tasks))

print("not closed yet")

loop.close()