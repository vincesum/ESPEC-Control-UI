import serial
import serial.rs485

'''
UART Master class for serial communication
Baudrate: 9600
Data bits: 8
Parity: None
Stop bits: 1
'''
class UARTMaster:
    def __init__(self, port='COM3', baudrate=9600, timeout=1, use_rs485=False, device_address=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.use_rs485 = use_rs485
        self.address = device_address  # Store the target device address

    def CreateDeviceInfoList(self):
        pass

    def GetDeviceInfoList(self):
        pass

    #Opens the serial port
    def Open(self):
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=self.timeout
        )
        if self.use_rs485:
            # This tells the driver to toggle RTS high while sending
            # Note: Not all drivers support this. If yours fails, you need a hardware
            # adapter with "Automatic Send Data Control".
            rs485_conf = serial.rs485.RS485Settings(
                rts_level_for_tx=True, 
                rts_level_for_rx=False,
                loopback=False,
                delay_before_tx=None,
                delay_before_rx=None
            )
            self.ser.rs485_mode = rs485_conf

    def Close(self):
        if self.ser:
            self.ser.close()

    def Purge(self):
        if self.ser:
            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()

    def Write(self, cmd):
        if self.ser and self.ser.is_open:
            # FIX #2: Add Address for RS-485
            # RS-485 commands MUST start with "Address," (e.g., "1,TEMP?")
            if self.use_rs485:
                full_command = f"{self.address},{cmd}\r\n"
            else:
                full_command = f"{cmd}\r\n"

            self.ser.write(full_command.encode('ascii'))
        else:
            print("Error: Port not open")

    def Read(self):
        if self.ser and self.ser.is_open:
            # Read until newline
            return self.ser.readline().decode('ascii').strip()
        return None
    
