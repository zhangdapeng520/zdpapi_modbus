"""
从服务端获取100台机组的数据，每台机组有25个变量
"""
from zdpapi_modbus import MasterAsync, trans_int_to_float
import time
import asyncio

master = MasterAsync("127.0.0.1", 502)
slave_id = 1


class Device:
    def __init__(self, address, length) -> None:
        self.master = MasterAsync("127.0.0.1", 502)
        self.address = address
        self.length = length

    async def execute(self):
        start = time.time()
        await asyncio.sleep(0.04)
        data = await self.master.execute(1, 3, self.address, self.length)
        data = trans_int_to_float(data)
        end = time.time()
        print("读取到的数据是：", data)
        print("单次读取耗时: ", end - start)


devices = [Device((i-1)*48, 48) for i in range(1, 51)]


async def run():
    while True:
        # 每次读取50个
        start = time.time()
        tasks = []
        for device in devices:
            tasks.append(device.execute())
        await asyncio.gather(*tasks)
        print("总共读取耗时：", time.time() - start)

# asyncio.run(run())

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
