import glob
import os

chemin = glob.glob(os.path.dirname(__file__)+'/*pdf')
print(chemin)
for name in chemin :
    print(name)
