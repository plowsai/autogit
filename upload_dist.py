import os
import subprocess

dist_dir = 'dist'
files = os.listdir(dist_dir)
files = [os.path.join(dist_dir, f) for f in files]

subprocess.run(['twine', 'upload'] + files, check=True)
