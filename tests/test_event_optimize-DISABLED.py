#!/usr/bin/env python
from __future__ import division, print_function
import sys, os
from StringIO import StringIO
import unittest
import numpy as np
import pint.scripts.event_optimize as event_optimize
from pinttestdata import testdir, datadir

parfile = os.path.join(datadir, 'PSRJ0030+0451_psrcat.p')
eventfile = os.path.join(datadir, 'J0030+0451_P8_15.0deg_239557517_458611204_ft1weights_GEO_wt.gt.0.4.fits')
temfile = os.path.join(datadir, 'templateJ0030.3gauss')

class TestEventOptimize(unittest.TestCase):

    def test_result(self):
        saved_stdout, event_optimize.sys.stdout = event_optimize.sys.stdout, StringIO('_')
        cmd = '{0} {1} {2} --weightcol=PSRJ0030+0451 --minWeight=0.9 --nwalkers=10 --nsteps=50 --burnin 10'.format(eventfile,parfile,temfile)
        event_optimize.main(cmd.split())
        lines = event_optimize.sys.stdout.getvalue()
        # Need to add some check here.
        event_optimize.sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
