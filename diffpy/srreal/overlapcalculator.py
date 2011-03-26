#!/usr/bin/env python
##############################################################################
#
# diffpy.srreal     by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2011 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################


"""class OverlapCalculator -- calculator of atom overlaps in a structure.
"""

# module version
__id__ = "$Id$"

# exported items, these also makes them show in pydoc.
__all__ = ['OverlapCalculator']

from diffpy.srreal.wraputils import propertyFromExtDoubleAttr
from diffpy.srreal.wraputils import setattrFromKeywordArguments
from diffpy.srreal.srreal_ext import OverlapCalculator

# property wrappers to C++ double attributes

OverlapCalculator.rmin = propertyFromExtDoubleAttr('rmin',
        '''Lower bound for the bond distances.
        [0 A]''')

OverlapCalculator.rmax = propertyFromExtDoubleAttr('rmax',
        '''Upper bound for the bond distances.
        [5 A]''')

OverlapCalculator.rmaxused = propertyFromExtDoubleAttr('rmaxused',
        '''Effective upper bound for the bond distances.
        rmaxused equals either a double of the maximum atom radius
        in the structure or rmax.
        ''')

# method overrides that support keyword arguments

def _init_kwargs(self, **kwargs):
    '''Create a new instance of OverlapCalculator.
    Keyword arguments can be used to configure
    calculator properties, for example:

    olc = OverlapCalculator(rmax=2.5)

    Raise ValueError for invalid keyword argument.
    '''
    OverlapCalculator.__boostpython__init(self)
    setattrFromKeywordArguments(self, **kwargs)
    return


def _call_kwargs(self, structure, **kwargs):
    '''Return siteSquareOverlaps per each site of the structure.

    structure    -- structure to be evaluated, an instance of diffpy Structure
                    or pyobjcryst Crystal
    kwargs       -- optional parameter settings for this calculator

    Return a numpy array.
    '''
    setattrFromKeywordArguments(self, **kwargs)
    self.eval(structure)
    return self.sitesquareoverlaps


OverlapCalculator.__boostpython__init = OverlapCalculator.__init__
OverlapCalculator.__init__ = _init_kwargs
OverlapCalculator.__call__ = _call_kwargs

# End of file
