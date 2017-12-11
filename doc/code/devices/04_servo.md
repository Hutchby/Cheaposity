# Servo

The servomotor is used to change the orientation of the sonar, to get a better
"view" of the rover environment.

**Class declaration**
```python
servoMG996R(channel, pulse)
```

**prototype if the main function is:**
```python
rotate(value)
```
* value: a value between 0 and 1, where 0 is the min position of the servomotor 
	and 1 the max, example: 0.5 while set the servo at mid-distance between 
	min and max
