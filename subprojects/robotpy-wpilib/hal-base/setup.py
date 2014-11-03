#!/usr/bin/env python3

from os.path import dirname, exists, join
import sys, subprocess
from setuptools import setup

setup_dir = dirname(__file__)
base_package = 'hal'

# Automatically generate a version.py based on the git version
if exists(join(setup_dir, '..', '.git')):
    p = subprocess.Popen(["git", "describe", "--tags", "--dirty=-dirty"],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()
    # Make sure the git version has at least one tag
    if err:
        print("Error: You need to create a tag for this repo to use the builder")
        sys.exit(1)
    
    # Create the version.py file
    with open(join(setup_dir, base_package, 'version.py'), 'w') as fp:
        fp.write("# Autogenerated by setup.py\n__version__ = '{0}'".format(out.decode('utf-8').rstrip()))

with open(join(setup_dir, base_package, 'version.py'), 'r') as fp:
    exec(fp.read(), globals())

with open(join(setup_dir, 'README.rst'), 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='robotpy-hal-base',
    version=__version__,
    description='WPILib Harware Abstration Layer base',
    long_description=long_description,
    author='Peter Johnson, Dustin Spicuzza',
    author_email='johnson.peter@gmail.com',
    url='https://github.com/robotpy',
    keywords='frc first robotics hal can',
    packages=['hal']
    )
