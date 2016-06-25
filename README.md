Device For Monitoring Some Critical Parameters of a CO2 Laser Cutter.
=====================================================================

This is a project undertaken by members of Idea Fab Labs in Santa Cruz to 
help monitor some critical parameters of our laser cutter. We're using
this to monitor 6 different parameters on our Redsail 100w Laser Cutter:

* Overall AC current usage (as measured at the electrical panel's "In")
* Chiller AC current usage
* AC in to power supply
* DC out of power supply
* Temperature at the tube's water inlet
* Temperature at the tube's water outlet

Who Built This?
---------------

This project was created by Zach White with significant contributions from 
Ben Hencke, Austin Neff, and Chris Maddox. Many other members at Idea Fab Labs
contributed ideas and suggestions in the process of building this.

Special thanks to Kelsey Rice, the Laser Zone Manager, for being open to this
crazy idea and lending his support.

Repository Contents
===================

Arduino Shield
--------------

* [Arduino Shield Gerbers](Arduino Shield Gerbers) - This directory contains gerbers for the Arduino Shield.
* [Arduino Shield Schematic.png](Arduino Shield Schematic.png) - The schematic for hooking up the sensors to the Arduino.
* [Laser Monitor.brd](Laser Monitor.brd) and [Laser Monitor.sch](Laser Monitor.sch) - EAGLE files for the Arduino Shield

Raspberry Pi
------------

* [Laser Cut Case.dxf](Laser Cut Case.dxf) - Plans for a case that can contain the Raspberry Pi

Software
--------

* [Laser_Monitoring.ino](Laser_Monitoring.ino) - Arduino sketch for reading and reporting data over serial
* [read_data.py](read_data.py) - Python 3.4 script to fetch readings and shove them into an RRD

Required Parts
==============

* 1 &times; Computer with USB able to run python 3.4
* 1 &times; [Arduino](http://store-usa.arduino.cc/products/a000066) (we used an Uno, but any arduino with analog pins will work.)
* 3 &times; [50A Current sensors](http://www.robotshop.com/en/dfrobot-50a-current-sensor-ac-dc.html)
* 2 &times; [LM34DZ Fahrenheit Temperature Sensor](http://www.allelectronics.com/make-a-store/item/lm34dz/fahrenheit-temperature-sensor/1.html)

Optional Parts
--------------

These parts aren't required for the monitoring portion, but we found each one
to be a valuable addition to our implementation.

* 1 &times; [Raspberry Pi](https://www.raspberrypi.org)
* 1 &times; [PiFace Control and Display Board](https://www.element14.com/community/docs/DOC-55622/l/piface-control-and-display-board-for-use-with-raspberry-pi)
* 1 &times; USB Wifi Adaptor
* 1 &times; [Custom Arduino Shield](Laser Monitor.brd) - etch it yourself or have it made
* 6 &times; 10k resistors
* 1 &times; [Varistor](http://www.mouser.com/search/ProductDetail.aspx?R=0virtualkey0virtualkeyV8ZA2P) for overload protection
* 1 &times; Laser cut case. See [Laser Cut Case.dxf](Laser Cut Case.dxf) for plans. Use any 3mm (1/8") material.
* 24 &times; M3 x 10 Screw + Nut

Assembly
========

Program The Arduino
-------------------

(You can do this part on any computer, it doesn't have to be the monitoring
computer.)

1. Open the [Laser_Monitoring.ino](Laser_Monitoring.ino) file in the Arduino IDE
2. Upload the sketch to the Arduino
3. Open up the Serial Monitor (Tools -> Serial Monitor)
4. You should see a line written once a second consisting of 6 tab separated 
   numbers
5. Close the Arduino IDE

Wiring
------

Start by wiring up your Arduino. If you have made the PCB, you only need to
plug the current sensors in, wire up the temp sensors, and interface with the
laser's power supply for DC current. If you decide to forego the PCB you
will need to reference [the schematic](Arduino Shield Schematic.png) to get
everything wired up properly.

You will need to make your own pigtails for the temperature sensors. For
consistency with the current sensors we recommend using Red for VCC, Blue for 
Signal, and Black for GND.

FIXME: Have Ben describe connecting the DC current sensing.

Once you've wired up the Arduino, you can plug it into the monitoring computer
(in our setup that's the Raspberry Pi) 

Operation
=========

Run `python3.4 read_data.py` to read data from the Arduino and write it to
an RRD file.

TODO
====

* Create an interface to display data from the RRD
