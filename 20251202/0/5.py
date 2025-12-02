import asyncio
import random

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()

async def snd():
    evsnd.set()
    print("snd: generated evsnd")

async def mid(k):
    await evsnd.wait()
    if k == 0:
        evmid0.set()
        print("mid: generated evmid0")
    else:
        evmid1.set()
        print("mid: generated evmid1")

async def rcv():
    await evmid0.wait()
    print("rcv got evmid0")
    await evmid1.wait()
    print("rcv got evmid1")