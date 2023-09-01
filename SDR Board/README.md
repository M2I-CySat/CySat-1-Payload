# Software-Defined Radio (SDR) Radiometer Application for CySat

## Hardware
- [Analog Devices ADRV1-9361-Z7035 (ADRV9361) System-on-a-Chip (SoC) SDR](https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom)
- [Analog Devices ADRV1CRR-FMC Carrier Board](https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/fmc)

## AD9361 Docs
- [CyBox](https://iastate.app.box.com/folder/174136460111)
- [Professor Matthew Nelson Master's Thesis - Radiometer SDR](https://github.com/matgyver/Radiometer-SDR-Thesis)
- [Intro to SDRs](https://greatscottgadgets.com/sdr/)
- `/AD9361 Resources` contains files related to the connection the to the Radiometer
- `/sdr_dev` contains all the dev files running on the SDR chip

## Instructions
The SDR board has been confirmed to output the correct data from the radiometer application
(radiometer_app.py), which instantiates the auto-generated python code
‘AD9361_TPR_nogui.py’ that was generated from the GNURadio Companion design
`AD9361_radiometer_nogui.grc`. This GNURadio Companion design was based from Matt
Nelson’s Thesis’ design `N200_radiometer.grc`. The SDR board has been confirmed to have
working UART from a host computer, however we were unable to verify a functioning UART
connection between the SDR board and Flight Computer due to hardware complications. We
also confirmed that our python code properly ran on system startup. This was done by calling
our `uart_test.py` script from `sat_scan.py`, which was already configured by an earlier team to
execute on system startup.

The Flight Computer has a GPIO pin (to be referred to as SDR_EN=OBC_OUT1), which is
routed via PC104 bus pin ​H2-3​ through the LNA and SDR carrier board to the Power Enable
Signal (JX1 pin 5). The SDR will communicate with the Flight Computer via UART: Rx = JX4 Pin
99 and Tx = JX4 Pin 98, which will be traced through the SDR Carrier board to the PC104 bus
pins: H1-39 and H1-40 respectively. These correlate to the Flight Computer’s system UART
Tx/Rx.

### SDR Board sequence

1. Flight Computer sets a SDR_EN pin high.
2. This will boot the board, which runs the Radiometer python script on startup.
3. This Radiometer python script will wait some ​T.B.D.​ amount of time then wait for a
   command to start recording data (See note 1 below).
4. The Flight Computer will tell the SDR board to start recording via UART command.
5. The Flight Computer will tell the SDR board the eight radiometer parameters via UART
   command.
6. The SDR board will acknowledge that it received these parameters and will start
   recording.
7. The Flight Computer will tell the SDR board to stop recording via UART command.
8. The SDR board will acknowledge that it will stop recording.
9. The SDR board will stop recording and close data files: ‘tpr.dat’ and ‘tpr_kelvn.dat’.
   10.The Flight Computer will request the size of the ‘tpr.dat’ file via UART.
   11.The SDR board will reply the size via UART.
   12.The Flight Computer will request the data via UART.
   13.The SDR board will reply with the data via UART.
   14.The Flight Computer will request the size of the ‘tpr_kelvin.dat’ file via UART.
   15.The SDR board will reply the size via UART.
   16.The Flight Computer will request the data via UART.
   17.The SDR board will reply with the data via UART.
   18.The Flight Computer will tell the SDR board via I2C to shutdown.
   19.The SDR board will acknowledge that it will shut itself down.
   20.The SDR board will run the system shutdown call (sudo shutdown -h now)
   21.The Flight Computer pulls the SDR_EN pin low.

### Notes

1. The T.B.D. amount of time is for “SDR warmup” (system temperature) per Matt Nelson.
   Matt said 10-minute warm-up should suffice.

To recreate SDR application from scratch:

1. Download and setup the linux image from
   https://wiki.analog.com/resources/tools-software/linux-software/zynq_images​ and follow
   its instructions.
2. This image may or may not include, but the following libraries may need to be installed:
   a. gr-iio
   b. libiio
   c. libad9361-iio
   d. rtl-sdr
3. Clone the radiometer project from CySat Payload GitHub repository.
4. Set the “radiometer_app” python executable to run on startup:
   a. Copy radiometer_app.py in the home directory, and ensure the first line of the
   script says “#!/usr/bin/python”
   b. Run `chmod +x radiometer_app.py`
   c. Run ‘cd /etc/init.d`d. Run`sudo vim radiometer_app`, and press ‘i’ then type
  `sudo /home/analog/radiometer_app.py`followed by escape key then`:wq`e. Run`sudo chmod +x radiometer_app`f. Run`sudo update-rc.d radiometer_app defaults`
5. Download and install pyserial on the SDR board
   a. Download here on to your computer:
   https://files.pythonhosted.org/packages/cc/74/11b04703ec416717b247d
   77269d567db575d2fd88f25d9767fe3d/pyserial-3.4.tar.gz
   b. Setup SDR ethernet interface
   i. Connect ethernet cable to the eth0 RJ45 jack and your computer
   ii. Run `sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0` on the
   SDR board
   iii. Configure the ethernet interface on your computer to have an IP address
   of 192.168.1.2, netmask of 255.255.255.0 and gateway of 192.168.1.
   iv. Run `scp ~/Downloads/pyserial-3.4.tar.gz analog@192.168.1.10:~/` on
   your computer to securely copy over pyserial tarball over the ethernet
   interface
   v. On the SDR board, run ‘tar -xvf pyserial-3.4.tar.gz’ to extract the contents
   of the tarball.
   vi. Change to this directory by running: `cd pyserial-3.4`
   vii. Install pyserial 3.4 via `sudo setup.py install`

This should now be ready to test.

**To verify the radiometer application output:**

1. Copy ‘tpr.dat’ and ‘tpr_kelvin.dat’ files to your machine
2. Open a terminal and run ipython
3. Import scipy: `import scipy`
4. Import data via `tpr = scipy.fromfile(open("tpr.dat"), dtype=scipy.float32)’
5. Verify array contains data via: ‘tpr’
6. Import data via: ‘tpr_kelvin = scipy.fromfile(open("tpr_kelvin.dat"), dtype=scipy.float32)’
7. Verify array contains data via: ‘tpr_kelvin’
