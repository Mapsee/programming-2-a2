# mapit.py - tool to search physical addresses
# usage -- python mapit.py 6600 Williams Road Richmond
    # output: should take us to the address in gMaps

import webbrowser
import sys

address = " ".join(sys.argv[1:])

# TODO: open the browser at a GMAPS page with the arguments
prefix = "https://google.come/maps/place/"
webbrowser.open(prefix+address)

# TODO: add feature to grab address from clipyard