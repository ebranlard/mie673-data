import sys
import os

pythonExe = sys.executable            # path to Python executable
curDir = os.getcwd()                  # path to current system folder
scriptDir = os.path.dirname(__file__) # current directory of this script
print('')
print(f'Python exe       : {pythonExe}')
print(f'Current directory: {curDir}')
print(f'Script directoty:  {scriptDir}')
print('')
try:
    import numpy
    print('[ OK ] Numpy path           : {}'.format(numpy.__file__))
except ModuleNotFoundError:
    print('[FAIL] Numpy not installed')
try:
    import openfast_toolbox
    print('[ OK ] openfast_toolbox path: {}'.format(numpy.__file__))
except ModuleNotFoundError:
    print('[FAIL] openfast_toolbox not installed')
