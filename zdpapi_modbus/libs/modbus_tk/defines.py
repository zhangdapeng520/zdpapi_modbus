# modbus异常码
ILLEGAL_FUNCTION = 1
ILLEGAL_DATA_ADDRESS = 2
ILLEGAL_DATA_VALUE = 3
SLAVE_DEVICE_FAILURE = 4
COMMAND_ACKNOWLEDGE = 5
SLAVE_DEVICE_BUSY = 6
MEMORY_PARITY_ERROR = 8

# 支持的读写func码
# 常用读数据
READ_COILS = 1  # 读线圈
READ_DISCRETE_INPUTS = 2  # 读离散输入
READ_HOLDING_REGISTERS = 3  # 读寄存器
READ_INPUT_REGISTERS = 4  # 读输入寄存器

# 常用写数据
WRITE_SINGLE_COIL = 5  # 写单一线圈
WRITE_SINGLE_REGISTER = 6  # 写单一寄存器
WRITE_MULTIPLE_COILS = 15  # 写多个线圈
WRITE_MULTIPLE_REGISTERS = 16  # 写多寄存器

# 其他
READ_EXCEPTION_STATUS = 7
DIAGNOSTIC = 8
REPORT_SLAVE_ID = 17
READ_WRITE_MULTIPLE_REGISTERS = 23
DEVICE_INFO = 43

# 支持的block类型
COILS = 1
DISCRETE_INPUTS = 2
HOLDING_REGISTERS = 3
ANALOG_INPUTS = 4
