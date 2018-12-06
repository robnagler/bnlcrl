# -*- coding: utf-8 -*-
u"""bnlcrl setup script

:copyright: Copyright (c) 2016-2018 mrakitin.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
pykern.pksetup.setup(
    name='bnlcrl',
    author='mrakitin',
    description='CRL simulator',
    install_requires=[
        # some "concrete" dependencies in requirements.txt
        'matplotlib',
        'numpy',
        'periodictable',
    ],
    license='http://www.apache.org/licenses/LICENSE-2.0.html',
    url='https://github.com/mrakitin/bnlcrl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
