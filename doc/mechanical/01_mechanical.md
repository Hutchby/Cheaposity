# Mechanical specifications

## Different parts

- Frame
- Case
- Wheels
- Motor
- Battery

## Frame

The actual frame is actualy the third version. The design for move modelisation
is based on differential-drive wheeled robot, controlled by pwm (pulse-width
modulation). There are 2 freewheels and 2 motorized wheel, arranged diagonaly.

Outline of wheel's disposition:
(F) : freewheel
(M) : motorized wheel

```
(M)------(F)
  |       |
  |       |
  |       |
(F)------(M)
```

## Case

  The objectif of the frame is to host the drone, by secure and recharge it.
  For the recharge, the case top need two copper pad on wich the specific
  drone's padcan make electric contact.

  The drone position can be secure by some electro magnet, place under the surface

## Wheels

  Wheels need to be high enough to pass over little obstacle.
  The distance floor <-> frame bottom chosen is about 5cm.

## Motor

  The motor used are 12V DC motor. The control is handle 2 Roxxy Navy 700,
  wich use a pwm signal to control the power and polarisation apply to the motors.

  To select the motor correctly, the most important criterion is the engine couple.
  Because the global weight of the "frame + case + battery + motor" might be
  substantial.

## Battery

  The voltage choosen is 12V.
  To select the battery correctly, be careful to the comsuption of the motor at full
  acceleration, it can be regulated by software to slow down the acceleration.
  Li-Po are recommended for their capacity to deliver enough amperage. Be carefull to  protect them against over/under charge.
