""" 
- Open an AeroDyn blade file
- Plot the chord as function of span
"""

import os
import matplotlib.pyplot as plt
from openfast_toolbox.io import FASTInputFile

# Get current directory so this script can be called from any location
scriptDir = os.path.dirname(__file__)

df = FASTInputFile(os.path.join(scriptDir, '../03.4MW/AeroDyn_blade.dat')).toDataFrame()
print(df.keys())
plt.plot(df['BlSpn_[m]'], df['BlChord_[m]'])
plt.xlabel('Span [m]')
plt.ylabel('Chord [m]')

if __name__ == '__main__':
    plt.show()
