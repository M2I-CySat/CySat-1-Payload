#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: RADIOMETER READER AND RECORDER
# Author: NOLAN JESSEN
# Description: PROGRAM CREATED BY HUMANS ON EARTH
# Generated: Thu Jan  1 00:03:34 1970
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import iio
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys


class sat_scan(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RADIOMETER READER AND RECORDER")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RADIOMETER READER AND RECORDER")
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

        self.settings = Qt.QSettings("GNU Radio", "sat_scan")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.bandwidth = bandwidth = 10000000
        self.spavg = spavg = 1
        self.samp_rate = samp_rate = bandwidth*2
        self.integ = integ = 2
        self.freq = freq = 1412500000
        self.file_rate = file_rate = 2.0
        self.fftsize = fftsize = 8192
        self.calib_2 = calib_2 = -342.774
        self.calib = calib = 4075.5

        ##################################################
        # Blocks
        ##################################################
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(1.0/((samp_rate*integ)/2.0), 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	bandwidth, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/4, samp_rate/64, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/4, samp_rate/64, firdes.WIN_HAMMING, 6.76))
        self.iio_fmcomms2_source_0 = iio.fmcomms2_source_f32c("localhost", freq, samp_rate, bandwidth, True, False, 0x8000, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)
        self.blocks_keep_one_in_n_4 = blocks.keep_one_in_n(gr.sizeof_float*1, 10000)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_float*1, "spectrum.dat", False)
        self.blocks_file_sink_1_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.single_pole_iir_filter_xx_0, 0))    
        self.connect((self.blocks_keep_one_in_n_4, 0), (self.blocks_file_sink_1_0, 0))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.iio_fmcomms2_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.low_pass_filter_0_0_0, 0))    
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_keep_one_in_n_4, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sat_scan")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        self.set_samp_rate(self.bandwidth*2)
        self.iio_fmcomms2_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.bandwidth)

    def get_spavg(self):
        return self.spavg

    def set_spavg(self, spavg):
        self.spavg = spavg

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.iio_fmcomms2_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/4, self.samp_rate/64, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/4, self.samp_rate/64, firdes.WIN_HAMMING, 6.76))
        self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.samp_rate*self.integ)/2.0))

    def get_integ(self):
        return self.integ

    def set_integ(self, integ):
        self.integ = integ
        self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.samp_rate*self.integ)/2.0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.iio_fmcomms2_source_0.set_params(self.freq, self.samp_rate, self.bandwidth, True, True, True, "manual", 64.0, "manual", 64.0, "A_BALANCED", "", True)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.freq, self.bandwidth)

    def get_file_rate(self):
        return self.file_rate

    def set_file_rate(self, file_rate):
        self.file_rate = file_rate

    def get_fftsize(self):
        return self.fftsize

    def set_fftsize(self, fftsize):
        self.fftsize = fftsize

    def get_calib_2(self):
        return self.calib_2

    def set_calib_2(self, calib_2):
        self.calib_2 = calib_2

    def get_calib(self):
        return self.calib

    def set_calib(self, calib):
        self.calib = calib


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = sat_scan()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
