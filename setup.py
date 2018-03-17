import setuptools

with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='orgmodeparse',
    version="0.0.1",
    description='Parsing basic orgmode files from Python.',
    long_description=readme,
    url='https://github.com/fangohr/orgmodeparse',
    author='Hans Fangohr',
    #author_email='jupyteroommf@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas'],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: BSD License',
                 #'Topic :: Scientific/Engineering :: Physics',
                 #'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3 :: Only']
)
