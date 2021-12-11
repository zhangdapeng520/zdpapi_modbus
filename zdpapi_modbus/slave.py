"""
slave相关的便捷操作
"""
from .zstruct import trans_float_to_int
from .libs.modbus_tk import modbus_tcp
from typing import List
import time
from .random import rand_float


class Slave:
    def __init__(self,
                 ip: str = "0.0.0.0",
                 port: int = 502) -> None:

        # modbus服务对象
        self.server = modbus_tcp.TcpServer(port=port, address=ip)

        # slave字典
        self.slaves = {}

    def add_slave(self, slave_id):
        """
        添加slave
        """
        if self.slaves.get(slave_id) is None:
            slave = self.server.add_slave(slave_id)
            self.slaves[slave_id] = slave

    def add_block(self, slave_id: int, block_name: str, func_code: int, address: int = 0, length: int = 3000):
        """
        添加block
        """
        slave = self.slaves.get(slave_id)
        slave.add_block(block_name, func_code, address, length)

    def write_many_float(self, slave_id, block_name, data: List[float]):
        """
        批量写入float数据。
        注意：地址位是连续的地址位，如果不连续，不要调用此功能。
        """
        slave = self.slaves.get(slave_id)  # slave
        values = trans_float_to_int(data)
        value_length = len(values)

        # 一次写入100个数据，分批写入
        index = 0
        while True:
            slave.set_values(block_name, index, values[index:index + 100])

            # 最后一次传输
            value_length -= 100
            if value_length <= 100:
                slave.set_values(block_name, index, values[index:])
                break

            # 每次传100个数
            index += 100

    def run(self, slave_id, block_name, data: List[float], freq_seconds: int = 1, random_data: bool = False):
        """
        运行Slave，使用slave向modbus写入数据
        slave_id：slave的唯一编号
        block_name：slave上对应的block的名称
        data：要写入的数据，是浮点数列表
        freq_seconds：写入频率，单位是秒
        """
        self.server.start()
        while True:
            if random_data:
                data = [rand_float(0, 100) for _ in data]
            self.write_many_float(slave_id, block_name, data)
            time.sleep(freq_seconds)
