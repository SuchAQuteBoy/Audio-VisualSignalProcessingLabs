# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from ReadWAVFile import rff, wtf
from dpcl import Dpcl

class Main(object):

    def _read_file(self, filename):
        file = rff(filename)
        data = file.getFrameListData()
        data, rebuild, err, snr = Dpcl(data).return_data()
        self._data = data
        self._rebuild = rebuild
        self._err = err
        self._snr = snr

    def _write_err_file(self, filename):
        wtf(filename, self._err)

    def _write_rebuild_file(self, filename):
        wtf(filename, self._rebuild)
    
    def _print_snr(self, filename):
        string = "SNR for {0} : {1}".format(filename, self._snr)
        print(string)

    def main(self):
        for i in range(1, 11):
            filename_wav = "../resources/" + str(i) + ".wav"
            filename_err = "../out/" + str(i) + ".dpc"
            filename_rebuild = "../out/" + str(i) + ".pcm"
            self._read_file(filename_wav)
            self._write_err_file(filename_err)
            self._write_rebuild_file(filename_rebuild)
            self._print_snr(filename_wav)


if __name__ == '__main__':
    Main().main()
