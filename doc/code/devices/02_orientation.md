# Direction Module

The direction module is a simple module to get the spatial orientation of the rover.
It's based on pitch, roll and azimuth (yell).

the pitch and roll of both drone and rover are known, it's the main data for 
engaging the 

Each are calculated from the accelerometer, magnetometer, and gyroscope device.

Accelerometer and  gyroscope are read from the MPU9250 and the magnetometer 
comes from the AK8963

Here are the functions prototypes:

```python
azimuth(vect)
altitude(vect)
pitch(vect)
roll(vect)
```

Where vect is a vector (x, y, z)
