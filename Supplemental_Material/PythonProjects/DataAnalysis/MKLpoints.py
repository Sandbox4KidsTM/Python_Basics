# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:36:26 2017

@author: Sandbox999
"""

import simplekml

kml=simplekml.Kml()

kml=kml.newpoint(name="SampleTA",coords=[(15,15)])
print(kml)

kml=kml.save("C:\\out\\points.kml")
    