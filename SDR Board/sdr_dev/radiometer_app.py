import os
import time
import serial
from AD9361_TPR_nogui import AD9361_TPR_nogui
from optparse import OptionParser
from gnuradio.eng_option import eng_option
from gnuradio import eng_notation

"""
Main radiometer application.
This is to be executed on Zynq (linux) startup.
"""
def main():
    # UART commands
    cmd_record_start = 0x01
    cmd_record_stop = 0x02
    cmd_shutdown = 0x03
    cmd_file_size = 0x04
    cmd_send_tpr_file = 0x05
    cmd_send_kelvin_file = 0x06
    ack = 0xFF

    # Absolute file paths for tpr.dat and tpr_kelvin.dat files
    tpr_dat_path = '/home/analog/Documents/Radiometer-SDR-Thesis-master/Code/tpr.dat'
    tpr_kelvin_dat_path = '/home/analog/Documents/Radiometer-SDR-Thesis-master/Code/tpr_kelvin.dat'

    # Wait 10 min.
    # time.sleep(600)
    print("Radiometer application started.")
    time.sleep(30) # temporarily for debugging

    with serial.Serial('/dev/ttyPS0', 115200, timeout=1) as ser:
        # Wait for UART request to send parameters
        while True:
            # this blocks until a '\n' is received or timeout
    	    data = ser.readline()
            if data == cmd_record_start:
                # Read radiometer parameters from flight computer
                calib_1 = ser.readline()
                calib_2 =ser.readline()
                fftsize = ser.readline()
                frequency = ser.readline()
                integ = ser.readline()
                spavg = ser.readline()
                # Acknowledge that we received these parameters
                ser.write(ack)
                break

        # Start recording
        print("Start recording.")
        parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
        parser.add_option("", "--calib-1", dest="calib_1", type="eng_float", default=eng_notation.num_to_str(4.0755e3),
            help="Set Calibration value 1 [default=%default]")
        parser.add_option("", "--calib-2", dest="calib_2", type="eng_float", default=eng_notation.num_to_str(-342.774),
            help="Set Calibration value 2 [default=%default]")
        parser.add_option("", "--fftsize", dest="fftsize", type="intx", default=8192,
            help="Set fftsize [default=%default]")
        parser.add_option("", "--frequency", dest="frequency", type="eng_float", default=eng_notation.num_to_str(1.4125e9),
            help="Set Center Frequency [default=%default]")
        parser.add_option("", "--integ", dest="integ", type="eng_float", default=eng_notation.num_to_str(2),
            help="Set Integration Time (seconds) [default=%default]")
        parser.add_option("", "--spavg", dest="spavg", type="intx", default=1,
            help="Set Spectral Averaging (Seconds) [default=%default]")
        (options, args) = parser.parse_args()
        # start radiometer application
        tb = AD9361_TPR_nogui(calib_1=options.calib_1, calib_2=options.calib_2, fftsize=options.fftsize, frequency=options.frequency, integ=options.integ, spavg=options.spavg)
        tb.start()
        
        # Wait for UART request to stop recording.
        while True:
            # this blocks until a '\n' is received or timeout
    	    data = ser.readline()
            if data == cmd_record_stop:
                # Acknowledge that we will stop recording
                ser.write(ack)
                break

        # stop radiometer application
        tb.stop()
        tb.wait()
        print("Stop recording.")

        # Wait for UART request to send tpr file.
        while True:
            # this blocks until a '\n' is received or timeout
    	    data = ser.readline()
            if data == cmd_file_size:
                # Send size of 'tpr.dat' file
                ser.write(os.path.getsize(tpr_dat_path))
            elif data == cmd_send_tpr_file:
                # Send 'tpr.dat' file
                ser.write(open(tpr_dat_path,"rb").read())
            # Check for acknowledge on next loop
            elif data == ack:
                break

         # Wait for UART request to send kelvin file.
        while True:
            # this blocks until a '\n' is received or timeout
    	    data = ser.readline()
            if data == cmd_file_size:
                # Send size of 'tpr_kelvin.dat' file
                ser.write(os.path.getsize(tpr_kelvin_dat_path))
            elif data == cmd_send_kelvin_file:
                # Send 'tpr.dat' file
                ser.write(open(tpr_kelvin_dat_path,"rb").read())
            # Check for acknowledge on next loop
            elif data == ack:
                break

        # Wait for UART request to shut down.
        while True:
            # this blocks until a '\n' is received or timeout
    	    data = ser.readline()
            if data == cmd_shutdown:
                ser.write(ack)
                break

        print("Shutting down system in 60 seconds.")
        time.sleep(60)    
        # system call to shutdown
        os.system('sudo shutdown -h now')

    # Close UART port
    ser.close()

if __name__ == '__main__':
    main()