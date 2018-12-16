# -*- coding: utf-8 -*-

from img import IMGProc

class Main(object): 
    def main(self):
        test_filepath = "resources/test.jpeg"
        filepath1 = "resources/01.png"
        filepath2 = "resources/02.png"
        img = IMGProc()
        # img.brightness(test_filepath, 50)
        # img.contrast(test_filepath, 0.5)
        # img.histogram(test_filepath)
        # img.median(test_filepath)
        # img.mean(test_filepath)
        # img.fast_median(test_filepath)
        # img.edge_reberts(test_filepath)
        # img.edge_sobel(test_filepath)

        img.mean(filepath1)
        img.median(filepath2)
        img.stop()


if __name__ == "__main__":
    Main().main()