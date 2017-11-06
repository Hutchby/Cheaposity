from i2c import i2c_device
import time

ADDRESS         = 0x68
ADDRESS_AK8963  = 0x0c

DEVICE_ID       = 0x71

# REGISTER 

SMPLRT_DIV      = 0x19
CONFIG          = 0x1A
GYRO_CONFIG     = 0x1B
ACCEL_CONFIG    = 0x1C
ACCEL_CONFIG_2  = 0x1D
LP_ACCEL_ODR    = 0x1E
WOM_THR         = 0x1F
FIFO_EN         = 0x23
I2C_MST_CTRL    = 0x24
I2C_MST_STATUS  = 0x36
INT_PIN_CFG     = 0x37
INT_ENABLE      = 0x38
INT_STATUS      = 0x3A
ACCEL_OUT       = 0x3B
TEMP_OUT        = 0x41
GYRO_OUT        = 0x43

I2C_MST_DELAY_CTRL  = 0x67
SIGNAL_PATH_RESET   = 0x68
MOT_DETECT_CTRL     = 0x69
USER_CTRL           = 0x6A
PWR_MGMT_1          = 0x6B
PWR_MGMT_2          = 0x6C
FIFO_R_W            = 0x74
WHO_AM_I            = 0x75

GFS_250     = 0x00
GFS_500     = 0x01
GFS_1000    = 0x02
GFS_2000    = 0x03
AFS_2G      = 0x00
AFS_4G      = 0x01
AFS_8G      = 0x02
AFS_16G     = 0x03

AK8963_ST1          = 0x02
AK8963_MAGNET_OUT   = 0x03
AK8963_CNTL1        = 0x0A
AK8963_CNTL2        = 0x0B
AK8963_ASAX         = 0x10

AK8963_MODE_DOWN    = 0x00
AK8963_MODE_ONE     = 0x01
AK8963_MODE_C8HZ    = 0x02
AK8963_MODE_C100HZ  = 0x06

AK8963_BIT_14       = 0x00
AK8963_BIT_16       = 0x01

def dataConv(data1, data2):
    value = data1 | (data2 << 8)
    if (value & (1 << 16 -1)):
        value -= (1 << 16)
    return value

class AK8963(i2c_device.i2c_device):
    
    def __init__(self):
        super().__init__(addr=ADDRESS_AK8963)
        self.configAK8963(AK8963_MODE_C8HZ, AK8963_BIT_16)

    def configAK8963(self, mode, mfs):
        if mfs == AK8963_BIT_14:
            self.mres = 4912.0/8190.0
        else:
            self.mres = 4912.0/32760.0
        self.write_cmd_arg(AK8963_CNTL1, 0x00)
        self.write_cmd_arg(AK8963_CNTL1, 0x0f)
        data = self.read_i2c_block_data(AK8963_ASAX, 3)

        self.magXcoef = (data[0] - 128) / 256 + 1.0
        self.magYcoef = (data[1] - 128) / 256 + 1.0
        self.magZcoef = (data[2] - 128) / 256 + 1.0
    
        self.write_cmd_arg(AK8963_CNTL1, 0x00)
        self.write_cmd_arg(AK8963_CNTL1, (mfs << 4 | mode))
    
    def readMagnet(self):
        x = 0
        y = 0
        z = 0
        drdy = self.read_data(AK8963_ST1)
        if drdy & 0x01:
            data = self.read_i2c_block_data(AK8963_MAGNET_OUT, 7)
            if (data[6] & 0x08) != 0x08:
                x = dataConv(data[1], data[0])
                y = dataConv(data[3], data[2])
                z = dataConv(data[5], data[4])
                
                x = round(x * self.mres * self.magXcoef, 3)
                y = round(y * self.mres * self.magYcoef, 3)
                z = round(z * self.mres * self.magZcoef, 3)

        return {'x': x, 'y': y, 'z': z}

class MPU9250(i2c_device.i2c_device):
    
    def __init__(self):
        super().__init__(ADDRESS)
        self.configMPU9250(GFS_250, AFS_2G)

    def searchDevice(self):
        who_am_i = self.mpu_device.read_data(WHO_AM_I)
        return who_am_i == DEVICE_ID

    def configMPU9250(self, gfs, afs):
        if gfs == GFS_250:
            self.gres = 250.0 / 32768.0
        elif gfs == GFS_500:
            self.gres = 500.0 / 32768.0
        elif gfs == GFS_1000:
            self.gres = 1000.0 / 32768.0
        else:
            self.gres = 2000.0 / 32768.0

        if afs == AFS_2G:
            self.ares = 2.0 / 32768.0
        elif afs == AFS_4G:
            self.ares = 4.0 / 32768.0
        elif afs == AFS_8G:
            self.ares = 8.0 / 32768.0
        else:
            self.ares = 16.0 / 32768.0

        self.write_cmd_arg(PWR_MGMT_1, 0x00)
        time.sleep(0.1)
        self.write_cmd_arg(PWR_MGMT_1, 0x01)
        time.sleep(0.1)
        self.write_cmd_arg(CONFIG, 0x03)
        self.write_cmd_arg(SMPLRT_DIV, 0x04)
        self.write_cmd_arg(GYRO_CONFIG, gfs << 3)
        self.write_cmd_arg(ACCEL_CONFIG, afs << 3)
        self.write_cmd_arg(ACCEL_CONFIG_2, 0x03)
        self.write_cmd_arg(INT_PIN_CFG, 0x02)
        time.sleep(0.1)

    def checkDataReady(self):
        drdy = self.read_data(INT_STATUS)
        return drdy & 0x01

    def readAccel(self):
        data = self.read_i2c_block_data(ACCEL_OUT, 6)
        x = dataConv(data[1], data[0])
        y = dataConv(data[3], data[2])
        z = dataConv(data[5], data[4])

        x = round(x * self.ares, 3)
        y = round(y * self.ares, 3)
        z = round(z * self.ares, 3)

        return {"x":x, "y":y, "z":z}

    def readGyro(self):
        data = self.read_i2c_block_data(GYRO_OUT, 6)
        
        x = dataConv(data[1], data[0])
        y = dataConv(data[3], data[2])
        z = dataConv(data[5], data[4])
        x = round(x * self.gres, 3)
        y = round(y * self.gres, 3)
        x = round(z * self.gres, 3)
    
        return {"x":x, "y":y, "z":z}





