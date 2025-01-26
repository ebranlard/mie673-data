""" 
- Open an AeroDyn blade file
- Plot the chord as function of span

"""

import os
import matplotlib.pyplot as plt
from openfast_toolbox.io import FASTInputFile

def blade_chord(bladefile):
    """ Function that returns blade raidus and chord for a given AeroDyn blade file
        NOTE: This is a simple function to illustrate some good practice in creating "library code"
             where there is no "global variables", and functions that you reuse are placed into a single 
             file. Small examples are placed in the "main" section of the python file. 
    """
    # Read blade aerodynamic properties from an input file
    df = FASTInputFile(bladefile).toDataFrame()
    print(df.keys())
    r = df['BlSpn_[m]']
    chord = df['BlChord_[m]']
    return r, chord


if __name__ == '__main__':
    # Get current directory so this script can be called from any location
    scriptDir = os.path.dirname(__file__)

    # Read chord from AeroDyn file
    r, chord = blade_chord(os.path.join(scriptDir, '../22.0MW/AeroDyn_blade.dat'))

    # --- Plot
    fig = plt.figure()
    plt.plot(r, chord)
    plt.xlabel('Span [m]')
    plt.ylabel('Chord [m]')
    plt.show()
