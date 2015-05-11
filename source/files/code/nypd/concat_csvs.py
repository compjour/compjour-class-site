"""

File 2006 has a large number of
for y in $(seq 2003 2014); do
    head -n 1 $y.csv; done | grep -oE '[^,"]+' | sort | uniq -c | sort | column -c 80

   1 adrnum       11 stname       12 cs_casng     12 othrweap     12 rf_vcact
   1 adrpct       12 ac_assoc     12 cs_cloth     12 pct          12 rf_vcrim
   1 cro          12 ac_cgdir     12 cs_descr     12 perobs       12 rf_verbl
   1 detail1_     12 ac_evasv     12 cs_drgtr     12 perstop      12 riflshot
   1 details_     12 ac_incid     12 cs_furtv     12 pf_baton     12 sb_admis
   1 dettyp_c     12 ac_inves     12 cs_lkout     12 pf_drwep     12 sb_hdobj
   1 premtyp      12 ac_other     12 cs_objcs     12 pf_grnd      12 sb_other
   1 prenam       12 ac_proxm     12 cs_other     12 pf_hands     12 sb_outln
   1 rescod       12 ac_rept      12 cs_vcrim     12 pf_hcuff     12 searched
   1 strintr      12 ac_stsnd     12 datestop     12 pf_other     12 sector
   1 strname      12 ac_time      12 dob          12 pf_pepsp     12 ser_num
   1 wepfound     12 addrtyp      12 explnstp     12 pf_ptwep     12 sex
   2 det          12 adtlrept     12 eyecolor     12 pf_wall      12 state
   2 dettypCM     12 age          12 frisked      12 pistol       12 sumissue
   2 lineCM       12 aptnum       12 haircolr     12 post         12 sumoffen
   4 forceuse     12 arstmade     12 ht_feet      12 race         12 timestop
   9 det          12 arstoffn     12 ht_inch      12 radio        12 trhsloc
   9 dettypcm     12 asltweap     12 inout        12 recstat      12 typeofid
   9 linecm       12 beat         12 knifcuti     12 repcmd       12 weight
  11 addrnum      12 build        12 machgun      12 revcmd       12 xcoord
  11 addrpct      12 city         12 officrid     12 rf_attir     12 ycoord
  11 crossst      12 comppct      12 offshld      12 rf_bulg      12 year
  11 premname     12 compyear     12 offunif      12 rf_furt      12 zip
  11 premtype     12 contrabn     12 offverb      12 rf_knowl
  11 rescode      12 crimsusp     12 othfeatr     12 rf_othsw
  11 stinter      12 cs_bulge     12 othpers      12 rf_rfcmp
"""

import os.path
import pandas as pd
from glob import glob

NYPD_RAW_PATH = 'data-hold/raw'
NYPD_CONCAT_CSV = 'data-hold/concat.csv'

alldf = DataFra

for csvname in glob(os.path.join(NYPD_RAW_PATH, '*.csv')):
    print("Adding", csvname)
    df = pd.read_csv(csvname, encoding = ' iso-8859-1')
    alldf = alldf.append(df[ALL_COLS])
