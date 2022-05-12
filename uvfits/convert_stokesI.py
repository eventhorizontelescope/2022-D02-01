#!/usr/bin/env python3
#
# Copyright (C) 2022 The Event Horizon Telescope Collaboration
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from hallmark import ParaFrame
import numpy as np
import ehtim as eh

tag  = 'ER6'
src  = 'SGRA'
year = 2017
doy  = {3597:'095',3598:'096',3599:'097',3600:'100',3601:'101'}

pf = ParaFrame('../ER6_SGRA/{expt:04d}/{pipeline}/{pipeline}_{expt:04d}_SGRA_{band}_{stage}.uvfits')
pf = pf(stage=['netcal_LMTcal_10s'])(band=['HI','LO'])

for k in set(pf.keys()) - {'path'}:
    globals()[k] = np.unique(pf[k])
    print(k, globals()[k][:16])

for _, r in pf.iterrows():
    # load from uvfits file
    f0stokes = eh.obsdata.load_uvfits(r.path, polrep='stokes')

    for col in ['qvis','uvis','vvis','qsigma','usigma']:
        # remove non-Stokes I components but keep Stokes V errors for consistent
        # treatment of errors magnitude with Stokes / pseudo Stokes data present
        f0stokes.data[col] *= 0 # this operation is nan-preserving

    # remove record of single polarization pseudo-I construction (remove nan)
    f0stokes.data['vvis']   = 0. * f0stokes.data['vis']
    f0stokes.data['vsigma'] = 1. * f0stokes.data['sigma']

    # save the uvfits file
    yd      = f'{year}_{doy[r.expt]}'
    band    = r.band.lower()
    stage   = r.stage.replace('_10s', '').replace('_', '-')
    outname = f'{tag}_{src}_{yd}_{band}_{r.pipeline}_{stage}_StokesI.uvfits'
    f0stokes.save_uvfits(outname)
