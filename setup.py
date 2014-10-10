from setuptools import setup, find_packages

setup(
    name='viewdns',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/MiquelT/viewdns-api.git',
    # install_requires=["PyCrypto", "asyncssh-unofficial"],
    license='BSD',
    author='MiquelTur',
    author_email='miquel.tur.m@gmail.com',
    description='API for http://viewdns.info',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ]
)