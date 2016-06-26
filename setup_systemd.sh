#!/bin/sh
#
# This script sets up the RRD file and sets up systemd services for any
# .service file in the current directory.
#
# Pretty much everything assumes you've unpacked this to /home/pi/Laser_Monitor

if [ ! -f readings.rrd ]; then
	rrdtool create readings.rrd --step 1 \
		DS:current1:GAUGE:30:U:U \
		DS:current2:GAUGE:30:U:U \
		DS:current3:GAUGE:30:U:U \
		DS:dc_current:GAUGE:30:U:U \
		DS:temp1:GAUGE:30:U:U \
		DS:temp2:GAUGE:30:U:U \
		RRA:AVERAGE:0.5:1:24 RRA:AVERAGE:0.5:6:10
fi

for svc in *.service; do
        svc_name=$(basename $svc .service)

	if [ ! -f /lib/systemd/system/$svc ]; then
		echo '*** Setting up service' $svc_name
		sudo ln $PWD/$svc /lib/systemd/system/$svc
		sudo systemctl daemon-reload
		sudo systemctl enable $svc_name
		sudo systemctl start $svc_name
	fi
done
