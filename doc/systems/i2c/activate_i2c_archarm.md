```sh

pacman -Suy i2c-tools

modprobe i2c-dev
modprobe i2c-bcm2708

echo "i2c-dev" > /etc/modules-load.d/i2c-dev.conf
echo "i2c-bcm2708" > /etc/modules-load.d/i2c-bcm2708.conf

int /boot/config.txt
device_tree=bcm2710-rpi-3-b.dtb
device_tree_param=i2c1=on
device_tree_param=spi=on

i2cdetect -y 0

```
