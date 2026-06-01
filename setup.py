# To package a Python project, we need to create a setup.py file that contains the necessary information about the project and its dependencies. Below is an example of what the setup.py file might look like for a machine learning project.
# General information about the project

from setuptools import setup, find_packages
from typing import List


# def read_requirements(requirements_file='requirements.txt'):
#     requirements = []
#     with open(os.path.join(os.path.dirname(__file__), requirements_file), 'r') as f:
#         requirements = [line.strip() for line in f]
#     return requirements

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',  # Name of the project
    version='0.1.0',  # Version of the project
    author='Margi Pandya',
    packages=find_packages(),  # Automatically find all packages
    install_requires=get_requirements('requirements.txt'),  # List of dependencies
)
