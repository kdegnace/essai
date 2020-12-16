import glob
import os

chemin = glob.glob(os.path.dirname(__file__)+'*')
for name in chemin :
    print(name)
