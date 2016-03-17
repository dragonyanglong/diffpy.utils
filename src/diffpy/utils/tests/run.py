#!/usr/bin/env python3
##############################################################################
#
# diffpy.utils      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2012 The Trustees of Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
##############################################################################

"""Convenience module for executing all unit tests with

python -m diffpy.utils.tests.run
"""

if __name__ == '__main__':
    import sys
    from diffpy.utils.tests import test
    # produce zero exit code for a successful test
    sys.exit(not test().wasSuccessful())

# End of file
