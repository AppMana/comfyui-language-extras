from os import path
from platform import system
from urllib import parse

from setuptools import setup, find_packages

package_name = "comfyui_language_extras"

setup_dir = path.dirname(path.abspath(__file__))
if system() != 'Windows' and ' ' in setup_dir:
    setup_dir = parse.quote(setup_dir)

our_requirements = open("requirements.txt").readlines()
our_requirements = [req.replace("{root:uri}", f"file://{setup_dir}") for req in our_requirements]

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(),
    install_requires=our_requirements,
    author='',
    author_email='',
    description='',
    include_package_data=True,
    entry_points={
        'comfyui.custom_nodes': [
            f'{package_name} = {package_name}',
        ],
    },
    package_data={
        package_name: ['**/*.json', '**/spiece.model']
    },
)
