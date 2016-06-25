import serial
import time


def to_volt(reading):
    """Returns the voltage for a reading from an Ardunio's analog pin.
    """
    return int(reading) * .0049


def split_line(raw_line):
    """Returns a tuple containing the following fields:

           current1, current2, current3, dc_current, temp1, temp2

       Each field is a voltage between 0 and 5v
    """
    datapoints = raw_line.strip().split('\t')
    datapoints = map(to_volt, datapoints)

    return datapoints


def handle_data(current1, current2, current3, dc_current, temp1, temp2):
    """Write the datapoints out to a file or print them or something.
    """
    print time.time(), u'current1:%s current2:%s current3:%s dc_current:%s temp1:%s F temp2:%s F' % (current1, current2, current3, dc_current, temp1, temp2)


with serial.Serial('/dev/cu.usbmodemfa2231', 57600, timeout=5) as arduino:
    while True:
        try:
            current1, current2, current3, dc_current, temp1, temp2 = \
                split_line(arduino.readline())
        except ValueError:
            continue

        # Calculate the current reading for the DFrobot sensors
        # http://www.dfrobot.com/wiki/index.php/50A_Current_Sensor(SKU:SEN0098)
        current1 = current1 * .004
        current2 = current2 * .004
        current3 = current3 * .004

        # Calculate the current reading for the DC load
        # FIXME, currently reports the voltage

        # Calculate the temperature
        temp1 = temp1 * 100
        temp2 = temp2 * 100

        # Handle the parsed datapoints
        handle_data(current1, current2, current3, dc_current, temp1, temp2)
