# Payload

## Team Payload
If it is dealing with RF and its not a radio it goes in here

`SDR Board` contains files related to the SDR chip and AD9361

`SDR Carrier Board` contains files related to the dev carrier board

## Hardware
- [Analog Devices ADRV1-9361-Z7035 (ADRV9361) System-on-a-Chip (SoC) SDR](https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom)
- [Analog Devices ADRV1CRR-FMC Carrier Board](https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/fmc)

## AD9361 Docs
- [CyBox](https://iastate.app.box.com/folder/174136460111)
- [Professor Matthew Nelson Master's Thesis - Radiometer SDR](https://github.com/matgyver/Radiometer-SDR-Thesis)
- [Intro to SDRs](https://greatscottgadgets.com/sdr/)
- `/AD9361 Resources` contains files related to the connection the to the Radiometer
- `/sdr_dev` contains all the dev files running on the SDR chip

To run program on boot-up, I followed the following steps:

1. sudo nano /etc/rc.local
2. added the line "sudo python /home/analog/Documents/sdr_dev/startup_radiometer_app.py &" to the end of the file before "exit 0"
3. sudo reboot
