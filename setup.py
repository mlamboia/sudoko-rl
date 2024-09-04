from setuptools import setup, find_packages

setup(
    name="sudoko-rl",
    version="0.0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=["gymnasium==0.29.0", "pygame==2.1.0"],
)
