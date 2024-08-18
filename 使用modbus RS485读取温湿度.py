# 请先安装 pymodbus 和 pyserial
# pip install pymodbus
# pip install pyserial


#from pymodbus.client.sync import ModbusSerialClient as ModbusClient   # 报错，说找不到 sync
from pymodbus.client import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException, ConnectionException
import logging

# 配置日志记录
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# 初始化Modbus串行客户端
# client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=3)    # [Errno 2] could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
# client = ModbusClient(method='rtu', port='/dev/ttyTHS1', baudrate=9600, timeout=3)
# ttyTHS4 ttyS0 ttyS1 ttyS2 ttyS4
# client = ModbusClient(method='rtu', port='/dev/ttyTHS1', baudrate=9600, timeout=3)
# client = ModbusClient(method='rtu', port='/dev/ttyTHS0', baudrate=9600, timeout=3, stopbits=1, bytesize=8, parity='N')
client = ModbusClient(port='COM4', baudrate=9600, timeout=3,
                      stopbits=1, bytesize=8, parity='N')    # 看文档，method='rtu'貌似没用


def read_temperature_and_humidity(client):
    try:
        # 读取寄存器地址0和1上的4个字节（两个寄存器）
        # result = client.read_input_registers(address=0, count=3, unit=1)  # 这个错了，这是读取输入寄存器的）0x04
        # result = client.read_holding_registers(address=0, count=3, unit=1)  # 这个才是读取输入寄存器的0x03  # unit参数错了，当前pymodbus版本没有这个参数，搞乌龙了，要不是用filelocator搜索函数用法，还真不知道- -
        result = client.read_holding_registers(
            address=0, count=2, slave=1)  # 读取输入寄存器的0x03 # 读两个寄存器就ok，卖家说第三个寄存器是预留的，不用读

        if result.isError():
            # 处理错误
            print("读取错误:", result)
            return None, None

        # 将读取到的结果转换为温度和湿度
        registers = result.registers
        temperature_reg = registers[0]
        humidity_reg = registers[1]

        # 检查是否有探头错误
        if temperature_reg == 0x8000 or humidity_reg == 0x8000:
            print("探头错误")
            return None, None

        # 计算实际的温度和湿度值
        temperature = temperature_reg * 0.1
        humidity = humidity_reg * 0.1

        # 格式化温度和湿度值，保留一位小数
        temperature = round(temperature, 1)
        humidity = round(humidity, 1)

        return temperature, humidity

    except ModbusException as e:
        print("Modbus异常:", e)
        return None, None
    except Exception as e:
        # 捕获除ModbusException之外的所有异常
        print(f"An error occurred: {e}")
        return None, None


def main():
    try:
        if client.connect():  # 尝试连接到Modbus服务器/设备
            temperature, humidity = read_temperature_and_humidity(client)
            if temperature is not None and humidity is not None:
                print(f"温度: {temperature}°C, 湿度: {humidity}%RH")
            client.close()  # 关闭连接
        else:
            print("无法连接到Modbus设备")

    except ConnectionException as e:
        print("连接异常:", e)


if __name__ == "__main__":
    main()

