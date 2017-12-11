# I2C Driver

Every i2c component is based on the I2C driver which is composed of I/O 
functions

It uses the smbus python module to communicate.


* Function prototypes:

```python
write_cmd(cmd)
write_cmd_arg(cmd, data)
write_cmd_data(cmd, data)

read_data(cmd)
read_block_data(cmd)
read_i2c_block_data(cmd, data)
```
