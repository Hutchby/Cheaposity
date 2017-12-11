# Sonar

The sonar is used to detect object which could block the rover. It's a HC-SR04 
model. It's based on the GPIO, 18 for trigger and 24 for echo, ports of the 
raspberry

**Class declaration**
```python
Sonar()
```

**The prototype of the main function is:**
```python
measure()
```
* return: is the distance in meter between the sonar and the object 
(max distance is 1,5m)
