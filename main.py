# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 18:38:02 2023

@author: MusangKing

main.py as the entry of debugging
"""
import fullcontrol as fc

# import plotly.io as pio
# pio.renderers.default = 'notebook'

def demo_1():
    # create an empty list called steps
    steps=[]
    # add points to the list
    steps.append(fc.Point(x=40,y=40,z=0.2))
    steps.append(fc.Point(x=50,y=50))
    steps.append(fc.Point(x=60,y=40))
    # turn the extruder on or off
    steps.append(fc.Extruder(on=False))
    steps.append(fc.Point(x=40,y=40,z=0.4))
    steps.append(fc.Extruder(on=True))
    steps.append(fc.Point(x=50,y=50))
    steps.append(fc.Point(x=60,y=40))
    # transform the design into a plot
    fc.transform(steps, 'plot')

def main():
    demo_1()

if __name__ == "__main__":
    main()
    
    