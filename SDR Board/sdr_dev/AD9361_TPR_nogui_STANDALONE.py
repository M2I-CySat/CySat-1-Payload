#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Total Power Radiometer - AD9361
# Author: Matthew E Nelson
# Description: Total power radiometer connecting to a AD9361 SDR
# Generated: Thu Jan  1 00:37:04 1970
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from TPR import TPR  # grc-generated hier_block
from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip


class AD9361_TPR_nogui(gr.top_block, Qt.QWidget):

    def __init__(self, RF_bandwidth=15000000, calib_1=830.54, calib_2=-460.45, dc_gain=10, fftsize=8192, frequency=1.4125e9, integ=2, prefix="/home/analog/Documents/sdr_dev/data/", sample_rate=15e6, spavg=1):
        gr.top_block.__init__(self, "Total Power Radiometer - AD9361")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Total Power Radiometer - AD9361")

        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "AD9361_TPR_nogui")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.RF_bandwidth = RF_bandwidth
        self.calib_1 = calib_1
        self.calib_2 = calib_2
        self.dc_gain = dc_gain
        self.fftsize = fftsize
        self.frequency = frequency
        self.integ = integ
        self.prefix = prefix
        self.sample_rate = sample_rate
        self.spavg = spavg

        ##################################################
        # Variables
        ##################################################
        self.tpr_kelvin_file = tpr_kelvin_file = prefix +  "tpr_kelvin " + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".dat"
        self.tpr_file = tpr_file = prefix +  "tpr " + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".dat"
        self.samp_rate = samp_rate = int(sample_rate)
        self.freq = freq = frequency
        self.file_rate = file_rate = 2.0
        self.det_rate = det_rate = int(20.0)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_1 = qtgui.number_sink(
                gr.sizeof_float,
                0,
                qtgui.NUM_GRAPH_HORIZ,
        	1
        )
        self.qtgui_number_sink_1.set_update_time(.5)
        self.qtgui_number_sink_1.set_title("Calibrated")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, 0)
            self.qtgui_number_sink_1.set_max(i, 300)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
                gr.sizeof_float,
                0,
                qtgui.NUM_GRAPH_HORIZ,
        	1
        )
        self.qtgui_number_sink_0.set_update_time(.5)
        self.qtgui_number_sink_0.set_title("Raw")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1000)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_2_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_2_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_2_0.enable_grid(False)
        self.qtgui_freq_sink_x_2_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_2_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_2_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_2_0_win)
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c("localhost", int(freq), int(sample_rate), RF_bandwidth, True, False, 0x8000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((calib_1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((dc_gain, ))
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_float*1, int(det_rate/file_rate))
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, "tpr_raw_shay.dat", False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/analog/Documents/sdr_dev/data/tpr_kelvin_shay.dat", False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((calib_2, ))
        self.TPR_0 = TPR(
            det_rate=det_rate,
            integ=integ,
            samp_rate=samp_rate,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.TPR_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.TPR_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.qtgui_number_sink_1, 0))    
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_keep_one_in_n_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.TPR_0, 0))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.qtgui_freq_sink_x_2_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "AD9361_TPR_nogui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_RF_bandwidth(self):
        return self.RF_bandwidth

    def set_RF_bandwidth(self, RF_bandwidth):
        self.RF_bandwidth = RF_bandwidth
        self.iio_fmcomms2_source_0.set_params(int(self.freq), int(self.sample_rate), self.RF_bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)

    def get_calib_1(self):
        return self.calib_1

    def set_calib_1(self, calib_1):
        self.calib_1 = calib_1
        self.blocks_multiply_const_vxx_1.set_k((self.calib_1, ))

    def get_calib_2(self):
        return self.calib_2

    def set_calib_2(self, calib_2):
        self.calib_2 = calib_2
        self.blocks_add_const_vxx_1.set_k((self.calib_2, ))

    def get_dc_gain(self):
        return self.dc_gain

    def set_dc_gain(self, dc_gain):
        self.dc_gain = dc_gain
        self.blocks_multiply_const_vxx_0.set_k((self.dc_gain, ))

    def get_fftsize(self):
        return self.fftsize

    def set_fftsize(self, fftsize):
        self.fftsize = fftsize

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_freq(self.frequency)

    def get_integ(self):
        return self.integ

    def set_integ(self, integ):
        self.integ = integ
        self.TPR_0.set_integ(self.integ)

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_tpr_file(self.prefix +  "tpr " + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".dat")
        self.set_tpr_kelvin_file(self.prefix +  "tpr_kelvin " + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".dat")

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.set_samp_rate(int(self.sample_rate))
        self.iio_fmcomms2_source_0.set_params(int(self.freq), int(self.sample_rate), self.RF_bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)

    def get_spavg(self):
        return self.spavg

    def set_spavg(self, spavg):
        self.spavg = spavg

    def get_tpr_kelvin_file(self):
        return self.tpr_kelvin_file

    def set_tpr_kelvin_file(self, tpr_kelvin_file):
        self.tpr_kelvin_file = tpr_kelvin_file

    def get_tpr_file(self):
        return self.tpr_file

    def set_tpr_file(self, tpr_file):
        self.tpr_file = tpr_file

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.TPR_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_2_0.set_frequency_range(0, self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.iio_fmcomms2_source_0.set_params(int(self.freq), int(self.sample_rate), self.RF_bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)

    def get_file_rate(self):
        return self.file_rate

    def set_file_rate(self, file_rate):
        self.file_rate = file_rate
        self.blocks_keep_one_in_n_1.set_n(int(self.det_rate/self.file_rate))

    def get_det_rate(self):
        return self.det_rate

    def set_det_rate(self, det_rate):
        self.det_rate = det_rate
        self.TPR_0.set_det_rate(self.det_rate)
        self.blocks_keep_one_in_n_1.set_n(int(self.det_rate/self.file_rate))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--RF-bandwidth", dest="RF_bandwidth", type="intx", default=15000000,
        help="Set RF bandwidth (Hz) [default=%default]")
    parser.add_option("", "--calib-1", dest="calib_1", type="eng_float", default=eng_notation.num_to_str(830.54),
        help="Set Calibration value 1 [default=%default]")
    parser.add_option("", "--calib-2", dest="calib_2", type="eng_float", default=eng_notation.num_to_str(-460.45),
        help="Set Calibration value 2 [default=%default]")
    parser.add_option("", "--fftsize", dest="fftsize", type="intx", default=8192,
        help="Set fftsize [default=%default]")
    parser.add_option("", "--frequency", dest="frequency", type="eng_float", default=eng_notation.num_to_str(1.4125e9),
        help="Set Center Frequency [default=%default]")
    parser.add_option("", "--integ", dest="integ", type="eng_float", default=eng_notation.num_to_str(2),
        help="Set Integration Time (seconds) [default=%default]")
    parser.add_option("", "--prefix", dest="prefix", type="string", default="/home/analog/Documents/sdr_dev/data/",
        help="Set prefix [default=%default]")
    parser.add_option("", "--spavg", dest="spavg", type="intx", default=1,
        help="Set Spectral Averaging (Seconds) [default=%default]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = AD9361_TPR_nogui(RF_bandwidth=options.RF_bandwidth, calib_1=options.calib_1, calib_2=options.calib_2, fftsize=options.fftsize, frequency=options.frequency, integ=options.integ, prefix=options.prefix, spavg=options.spavg)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
