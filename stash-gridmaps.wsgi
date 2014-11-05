import os 
import sys	
sys.path.append('/home/tiles/TileStache')

import TileStache
application = TileStache.WSGITileServer('/home/tiles/TileStache/tilestache-gridmaps.cfg')
