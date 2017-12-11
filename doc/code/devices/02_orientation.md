# Direction Module

The direction module is a simple module to get the spatial orientation of the 
rover.
It's based on pitch, roll and azimuth (yell).

the pitch and roll of both drone and rover needs to be known before landing the 
drone on the rover

Each are calculated from the accelerometer, magnetometer, and gyroscope device.

Accelerometer and  gyroscope are read from the MPU9250 and the magnetometer 
comes from the AK8963

Azimuth is used to find the way to the drone and keep the rover in its direction

Here are the functions prototypes:

```python
azimuth(vect)
altitude(vect)
pitch(vect)
roll(vect)
```

* vect: vector (acceleration, gyroscope, magnetometer)
