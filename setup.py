from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """"
    this function will return the list of nrequirements
    """
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements




        


setup(

name="ml_project",
version="0.0.1",
author="kaustubh",
author_email="22222@iiitu.ac.in",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)