import os
import time
import ctypes
#import pylibi2c
from AD9361_TPR_nogui import AD9361_TPR_nogui
from optparse import OptionParser
from gnuradio.eng_option import eng_option
from gnuradio import eng_notation

"""
Main radiometer application.
This is to be executed on Zynq (linux) startup.
"""
def radiometer_app():

    # Wait 10 min.
    # time.sleep(600)
    print("Radiometer application started.")
    time.sleep(30)

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
    # I2C request to start recording.
    
    # Start recording
    print("Start recording.")
    tb = AD9361_TPR_nogui(calib_1=options.calib_1, calib_2=options.calib_2, fftsize=options.fftsize, frequency=options.frequency, integ=options.integ, spavg=options.spavg)
    tb.start()
    
    # I2C request to stop recording
    time.sleep(30)
    tb.stop()
    tb.wait()
    print("Stop recording.")    

    # I2C request to shut down
    print("Shutting down system in 60 seconds")
    time.sleep(60)    
    # system call to shutdown
    os.system('sudo shutdown -h now')

if __name__ == '__main__':
    radiometer_app()
