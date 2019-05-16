from setuptools import setup

setup(
    name='QuentinCLI',
    version='0.1',
    description='CLI that will blow your mind',
    author='Taha Shabbir Saifuddin',
    license='MIT',
    packages=['quentin'],
    package_data={'': ['*.ini']},
    install_requires=[
        'Click'
    ],
    python_requires='~=3.6',
    entry_points='''
        [console_scripts]
        quentin-cli=quentin.quentin:cli
        quentin=quentin.quentin:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: CLI Tool',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ]
)
