from setuptools import find_packages, setup 
from typing import List


Hype_E_Dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of reqirements
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if Hype_E_Dot in requirements:
            requirements.remove(Hype_E_Dot)
    
    return requirements




setup(
  name = 'Dashboard_Analysis_',
  version = '0.0.1',
  author = 'Paul',
  author_email = 'richard7812468@gmail.com',
  packages = find_packages(),
  install_requires = get_requirements('requirements.txt')
)