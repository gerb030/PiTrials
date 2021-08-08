# PiTrials

This project contains some trial code I've been writing for the Raspberry Pi. This directory contains a bunch of Python scripts that require the Pimoroni Unicorn HAT.
 
## UnicornHAT

The [Unicorn HAT](https://github.com/pimoroni/unicorn-hat) is fun little square matrix LED display. The scripts in this directory require Python 3.



1. Install Python3 (IDLE is optional):

```
sudo apt install python3 idle3
```

2. Install the UnicornHAT libraries:

```sudo apt-get install python3-pip python3-dev
sudo pip3 install unicornhat
```

3. Don't forget to enable SPI:

```
sudo raspi-config nonint do_spi 0
sudo reboot
```

3. Requires Pillow.

```
python3 -m pip install Pillow
```

