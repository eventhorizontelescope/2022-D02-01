# First Sagittarius A&ast; EHT Results: Calibrated Data

**Authors:** The Event Horizon Telescope Collaboration et al.

**Date:** May 12, 2022

**Primary Reference:** [The Event Horizon Telescope Collaboration, et al. 2022b, ApJL, 930, L13 (Sgr A&ast; Paper II)](https://doi.org/10.3847/2041-8213/ac6675)

**Data Product Code:** [2022-D02-01](https://eventhorizontelescope.org/for-astronomers/data)

**Brief Description:**

We release a data set to accompany the *First Sagittarius A&ast; Event
Horizon Telescope Results* paper series (EHT Collaboration et
al. 2022a,b,c,d,e,f).  The data set is derived from the Rev7
Correlation of the Event Horizon Telescope (EHT)'s April 2017
observation campaign (EHT Collaboration et al. 2019c), with further
processing and science validation as described in EHT Collaboration et
al. (2022b).  It is made public simultaneously with four imaging
pipelines (2022-D02-02, EHT Collaboration et al. 2022c).

This data set contains Sagittarius A&ast; (Sgr A&ast;) data for both
low and high bands for two observed days (April 6th and 7th, 2017).
Data from the 2017 observations were processed through two independent
reduction pipelines (Blackburn et al. 2019, Janssen et al. 2019, M87
Paper III, and Sgr A&ast; Paper II, Paper III).  This release includes
the fringe fitted, a-priori calibrated, network calibrated data from
both the EHT-HOPS and rPICARD (CASA) pipelines, which are used in the
First Sgr A* EHT results.  Independent flux calibration is performed
based on estimated station sensitvities during the campaign (Issaoun
et al. 2017, Janssen et al. 2019, Wielgus et al. 2022).  Data were
further calibrated to apply polarimetric gains to remove R-L gain
offsets, amplitude gains obtained from calibrators, amplitude gains on
LMT for its rapid gain fluctuations, and phase gains on JCMT for its
residual phase fluctuations.  A description of the data properties,
their validation, and estimated systematic errors is given in M87
Paper III and Sgr A&ast; Paper II and Paper III with additional
details in Wielgus et al. (2019) and Wielgus et al. (2022).

The data are time averaged to 10 seconds and frequency averaged over
all 32 intermediate frequencies (IFs).  All polarization information
is explicitly removed.  To make the resulting `uvfits` files
compatible with popular very-long-baseline interferometry (VLBI)
software packages, the circularly polarized cross-hand visibilities
`RL` and `LR` are set to zero along with their errors, while
parallel-hands `RR` and `LL` are both set to an estimated Stokes *I*
value.  Measurement errors for `RR` and `LL` are each set to sqrt(2)
times the statistical errors for Stokes *I*.

All `uvfits` files are located in the "`uvfits*/`" subdirectory.
Easy-to-read `csv` and `txt` files are derived from the `uvfits` files
and provided in "`csv*/`" and "`txt*/`", respectively.  Scripts that
generate these files from the processed ER6 data are also included.
Finally, the `run.sh` script in the top directory will convert
`uvfits` files into `csv` and `txt` files.

In addition to the visibility data sets after the above calibrations
in `uvfits/*`, `csv/*`, and `text/*` directories, we have prepared two
additional data sets.  The first additional data set is
lightcurve-normalized data in the `uvfits_norm/*`, `csv_norm/*` and
`text_norm/*` directories, where each of visibility amplitudes is
normalized by the total flux density from the Sgr A&ast;'s light curve
at the corresponding time (Wielgus et al. 2022).  These are the data
files used by all Sgr A&ast; static imaging pipelines in Paper III.
The second additional data set consists of am 100-minute interval of
visibility data cropped from the original (unnormalized) full-night
visibilities.  During this 100-minute interval of time the EHT array
has the best snapshot uv-coverages (see Farah et al. 2022 and Paper
III).  This data set is used in the analysis of short-time-scale
dynamic properties of Sgr A&ast; in Paper III.

The three `tgz` files are gzipped tarballs that contains `uvfits`,
`txt`, and `csv` files, respectively.  They are included in this
repository for convenience.

**File Name Convention:**

The data files are named in the following convention:

    [Data-Release-Tag]_[Source]_[year]_[day-of-year]_[band]_[pipeline]_[stage]_StokesI.[format]

**Station Code Table:**

| UVFITS Code | Station Name                  | Location   |
| ----------- | ----------------------------- | ---------- |
| AA          | ALMA                          | Chile      |
| AP          | APEX                          | Chile      |
| AZ          | Submillimeter Telescope       | Arizona    |
| JC          | James Clerk Maxwell Telescope | Hawai'i    |
| LM          | Large Millimeter Telescope    | Mexico     |
| PV          | IRAM                          | Spain      |
| SM          | Submillimeter Array           | Hawai'i    |
| SP          | South Pole Telescope          | Antarctica |

**References:**

- [EHT Collaboration Data Portal Website](https://eventhorizontelescope.org/for-astronomers/data)
- [The Event Horizon Telescope Collaboration, et al. 2019a, ApJL, 875, L1 (M87 Paper I)](https://doi.org/10.3847/2041-8213/ab0ec7)
- [The Event Horizon Telescope Collaboration, et al. 2019b, ApJL, 875, L2 (M87 Paper II)](https://doi.org/10.3847/2041-8213/ab0c96)
- [The Event Horizon Telescope Collaboration, et al. 2019c, ApJL, 875, L3 (M87 Paper III)](https://doi.org/10.3847/2041-8213/ab0c57)
- [The Event Horizon Telescope Collaboration, et al. 2019d, ApJL, 875, L4 (M87 Paper IV)](https://doi.org/10.3847/2041-8213/ab0e85)
- [The Event Horizon Telescope Collaboration, et al. 2019e, ApJL, 875, L5 (M87 Paper V)](https://doi.org/10.3847/2041-8213/ab0f43)
- [The Event Horizon Telescope Collaboration, et al. 2019f, ApJL, 875, L6 (M87 Paper VI)](https://doi.org/10.3847/2041-8213/ab1141)
- [Blackburn, L., Chan, C.-k., Crew, G., et al. 2019, ApJ, 882, 23](https://doi.org/10.3847/1538-4357/ab328d)
- [Janssen, M., Goddi, C., van Bemmel, I., et al. 2019, A&A, 626A, 75](https://doi.org/10.1051/0004-6361/201935181)
- [Issaoun, S., Folkers, T., Blackburn, L., et al. 2017, EHT Memo 2017-CE-02](https://eventhorizontelescope.org/for-astronomers/memos)
- [Janssen, M., Blackburn, L., Issaoun, S., et al. 2019, EHT Memo 2019-CE-01](https://eventhorizontelescope.org/for-astronomers/memos)
- [Wielgus, M., Blackburn, L., Issaoun, S., et al. 2019, EHT Memo 2019-CE-02](https://eventhorizontelescope.org/for-astronomers/memos)
- [The Event Horizon Telescope Collaboration, et al. 2022a, ApJL, 930, L12 (Sgr A&ast; Paper I)](https://doi.org/10.3847/2041-8213/ac6674)
- [The Event Horizon Telescope Collaboration, et al. 2022b, ApJL, 930, L13 (Sgr A&ast; Paper II)](https://doi.org/10.3847/2041-8213/ac6675)
- [The Event Horizon Telescope Collaboration, et al. 2022c, ApJL, 930, L14 (Sgr A&ast; Paper III)](https://doi.org/10.3847/2041-8213/ac6429)
- [The Event Horizon Telescope Collaboration, et al. 2022d, ApJL, 930, L15 (Sgr A&ast; Paper IV)](https://doi.org/10.3847/2041-8213/ac6736)
- [The Event Horizon Telescope Collaboration, et al. 2022e, ApJL, 930, L16 (Sgr A&ast; Paper V)](https://doi.org/10.3847/2041-8213/ac6672)
- [The Event Horizon Telescope Collaboration, et al. 2022f, ApJL, 930, L17 (Sgr A&ast; Paper VI)](https://doi.org/10.3847/2041-8213/ac6756)
- [Wielgus, M., Marchili, N., Marti-Vidal, I., Keating, G.K., Ramakrishnan, V., et al. 2022, ApJL, 930, L19](https://doi.org/10.3847/2041-8213/ac6428)
