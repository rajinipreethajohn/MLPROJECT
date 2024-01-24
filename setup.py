from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str) ->List[str]:
   '''
   this function will return a list of requirements
   '''
   requirements= []
   with open('requirements.txt', encoding='utf-8')as f:
       requirements=f.readlines()
       requirements=[req.replace("\n", " ") for req in requirements]
       
       if HYPHEN_E_DOT in requirements:
           requirements.remove(HYPHEN_E_DOT)
   return requirements

    
setup(
  name='mlproject',
  version='0.0.1',
  author='preetha',
  author_email='rajinipreethaj@hotmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)