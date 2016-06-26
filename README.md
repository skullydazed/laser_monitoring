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

This project was created by [Zach White](https://github.com/skullydazed) with
significant contributions from Ben Hencke ([github](https://github.com/simap),
[website](http://www.bhencke.com)), Austin Neff, and Chris Maddox.
Many other members at Idea Fab Labs contributed ideas and suggestions in
the process of building this.

Special thanks to Kelsey Rice, the Laser Zone Manager, for being open to this
crazy idea and lending his support.

Repository Contents
===================

Arduino Shield
--------------

* [doc/Arduino Shield Gerbers](doc/Arduino Shield Gerbers) - This directory
  contains gerbers for the Arduino Shield.
* [doc/Arduino Shield Schematic.png](doc/Arduino Shield Schematic.png) - The
  schematic for hooking up the sensors to the Arduino.
* [CAD/Laser Monitor.brd](Laser Monitor.brd) and
  [CAD/Laser Monitor.sch](Laser Monitor.sch) - EAGLE files for the Arduino
  Shield

Raspberry Pi
------------

* [CAD/Laser Cut Case.dxf](CAD/Laser Cut Case.dxf) - Plans for a case that
  can contain the Raspberry Pi

Software
--------

* [Laser_Monitoring.ino](Laser_Monitoring.ino) - Arduino sketch for reading
  and reporting data over serial
* [laserd](laserd) - Python 3.4 script to fetch readings and shove
  them into an RRD
* [laser_lcd](laser_lcd) - Python 3.4 script to fetch readings from RRD and
  display them on a PiFace Control and Display board

Required Parts
==============

* 1 &times; Computer with USB able to run python 3.4
* 1 &times; [Arduino](http://store-usa.arduino.cc/products/a000066) (we used
  an Uno, but any arduino with analog pins will work.)
* 3 &times; [50A Current sensors](http://www.robotshop.com/en/dfrobot-50a-current-sensor-ac-dc.html)
* 2 &times; [LM34DZ Fahrenheit Temperature Sensor](http://www.allelectronics.com/make-a-store/item/lm34dz/fahrenheit-temperature-sensor/1.html)

Optional Parts
--------------

These parts aren't required for the monitoring portion, but we found each one
to be a valuable addition to our implementation.

* 1 &times; [Raspberry Pi](https://www.raspberrypi.org)
* 1 &times; [PiFace Control and Display Board](https://www.element14.com/community/docs/DOC-55622/l/piface-control-and-display-board-for-use-with-raspberry-pi)
* 1 &times; USB Wifi Adaptor
* 1 &times; [Custom Arduino Shield](Laser Monitor.brd) - etch it yourself or
  have it made
* 6 &times; 10k resistors
* 1 &times; [Varistor](http://www.mouser.com/search/ProductDetail.aspx?R=0virtualkey0virtualkeyV8ZA2P) for overload protection
* 1 &times; Laser cut case. See [Laser Cut Case.dxf](Laser Cut Case.dxf) for
  plans. Use any 3mm (1/8") material.
* 24 &times; M3 x 10 Screw + Nut

Assembly
========

Program The Arduino
-------------------

(You can do this part on any computer, it doesn't have to be the monitoring
computer.)

1. Open the [Laser_Monitoring.ino](Laser_Monitoring.ino) file in the Arduino
   IDE
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
will need to reference [the schematic](doc/Arduino Shield Schematic.png) to get
everything wired up properly.

You will need to make your own pigtails for the temperature sensors. For
consistency with the current sensors we recommend using Red for VCC, Blue for
Signal, and Black for GND.

FIXME: Have Ben describe connecting the DC current sensing.

Once you've wired up the Arduino, you can plug it into the monitoring computer
(in our setup that's the Raspberry Pi)

Setup and First Run
===================

* Clone this repository to /home/pi/Laser_Monitor
* Create the RRD file:
  * `rrdtool create readings.rrd --step 1 \`  
    `DS:current1:GAUGE:30:U:U \`  
    `DS:current2:GAUGE:30:U:U \`  
    `DS:current3:GAUGE:30:U:U \`  
    `DS:dc_current:GAUGE:30:U:U \`  
    `DS:temp1:GAUGE:30:U:U \`  
    `DS:temp2:GAUGE:30:U:U \`  
    `RRA:AVERAGE:0.5:1:24 RRA:AVERAGE:0.5:6:10`
* Run `laserd` to read data from the Arduino and write it to an RRD file.
* Run `laser_lcd` to read data from the RRD and write it to the LCD.

Systemd
=======

If you're using a systemd based distribution you can use
[setup_systemd.sh](setup_systemd.sh) to setup the RRD file and the services
that will write to and read from that RRD.

TODO
====

* Create a web interface to display data from the RRD
