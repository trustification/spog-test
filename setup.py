from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements=f.read().splitlines()

setup(
    name="spog-ui-tests",
    version="0.0.1",
    author="RHTC QE team",
    author_email="rhtc-qe@redhat.com",
    description="UI Tests for Trustification SPoG",
    url="https://github.com/trustification/spog-test.git",
    pakages=find_packages(),
     install_requires=[
         requirements
    ],
    extras_require={
        'lint':[
            'black',
            'isort'
        ]
    }
)