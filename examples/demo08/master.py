"""
从服务端获取100台机组的数据，每台机组有25个变量
"""
from zdpapi_modbus import MasterAsync
import time, asyncio

master = MasterAsync("127.0.0.1", 502)
slave_id = 1
async def run():
    while True:
        # 每次读取50个
        total_time = 0
        for i in range(1, 101):
            start = time.time()
            address = (i - 1) * 50
            data = await master.execute(1, 3, address, 50)
            print(master.to_float(data))
            asyncio.sleep(0.04)
            end = time.time()
            spend = end - start
            if i == 1:
                print("单次读取耗时：", spend)
            total_time += spend

        print("总共读取耗时：", total_time)

asyncio.run(run())