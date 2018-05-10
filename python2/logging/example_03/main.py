
import sys
sys.path.append(r"C:\cases\python_guide\logging\example_03\package")

import logging
from networking import http
import media
import media.audio
from media.video import avitools


if __name__ == "__main__":
	#logging.basicConfig(level=logging.DEBUG)
	#logging.info("start")
	
	http.Http().do_get("http://sample_url")
		



