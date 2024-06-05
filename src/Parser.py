from optparse import OptionParser


class Parser(OptionParser):
    def __int__(self):
        super().__init__(usage="usage: %prog [options] tag value filename(s)")
        # OptionParser.__init__(self,usage="usage: %prog [options] tag value filename(s)")

    def parse_args(self):

        self.add_option("-v", action="count", dest="verbose", help="verbose", default=False)
        self.add_option("-s", action="store_true", dest="search", help="search for new usb connection", default=True)

        self.options, self.args = super().parse_args()


