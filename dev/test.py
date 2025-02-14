import brightway2 as bw

from premise import *

bw.projects.set_current("new")

scenarios = [
    {"model": "remind", "pathway": "SSP1-Base", "year": 2005},
    {"model": "image", "pathway": "SSP2-Base", "year": 2100},
    {"model": "remind", "pathway": "SSP5-Base", "year": 2050},
]

ndb = NewDatabase(
    scenarios=scenarios,
    source_db="ecoinvent 3.8 cutoff",
    source_version="3.8",
    key=b"tUePmX_S5B8ieZkkM7WUU2CnO8SmShwmAeWK9x2rTFo=",
)

ndb.update_all()
ndb.write_datapackage(name="my_dp")