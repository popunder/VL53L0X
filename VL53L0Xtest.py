import smbus
import struct
import time

'''Function with parameter.'''

def bswap(val):
    return struct.unpack('<H', struct.pack('>H', val))[0]
def mread_word_data(adr, reg):
    return bswap(bus.read_word_data(adr, reg))
def mwrite_word_data(adr, reg, data):
    return bus.write_word_data(adr, reg, bswap(data))
def makeuint16(lsb, msb):
    return ((msb & 0xFF) << 8)  | (lsb & 0xFF)

VL53L0X_REG_IDENTIFICATION_MODEL_ID           = 0x00c0
VL53L0X_REG_IDENTIFICATION_REVISION_ID        = 0x00c2
VL53L0X_REG_PRE_RANGE_CONFIG_VCSEL_PERIOD     = 0x0050
VL53L0X_REG_SYSRANGE_START = 0x000
bus = smbus.SMBus(1)
address = 0x29
val1 = bus.read_byte_data(address, VL53L0X_REG_IDENTIFICATION_REVISION_ID)
print "Revision ID: " + hex(val1)
val1 = bus.read_byte_data(address, VL53L0X_REG_IDENTIFICATION_MODEL_ID)
print "Device ID: " + hex(val1)
#	case VL53L0X_VCSEL_PERIOD_PRE_RANGE:
#		Status = VL53L0X_RdByte(Dev,
#			VL53L0X_REG_PRE_RANGE_CONFIG_VCSEL_PERIOD,
#			&vcsel_period_reg);


#	case VL53L0X_VCSEL_PERIOD_FINAL_RANGE:
#		Status = VL53L0X_RdByte(Dev,
#			VL53L0X_REG_FINAL_RANGE_CONFIG_VCSEL_PERIOD,
#			&vcsel_period_reg);


#		Status = VL53L0X_WrByte(Dev, VL53L0X_REG_SYSRANGE_START, 0x01);
val1 = bus.write_byte_data(address, VL53L0X_REG_SYSRANGE_START, 0x01)
#	Status = VL53L0X_ReadMulti(Dev, 0x14, localBuffer, 12);
time.sleep(0.200)
data = bus.read_i2c_block_data(address, 0x14, 12)
print data
print "ambient count " + str(makeuint16(data[7], data[6]))
print "signal count " + str(makeuint16(data[9], data[8]))
#		tmpuint16 = VL53L0X_MAKEUINT16(localBuffer[11], localBuffer[10]);
print "distance " + str(makeuint16(data[11], data[10]))

DeviceRangeStatusInternal = ((data[0] & 0x78) >> 3)
print DeviceRangeStatusInternal