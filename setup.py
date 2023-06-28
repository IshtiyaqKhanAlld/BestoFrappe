from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bestofrappe/__init__.py
from bestofrappe import __version__ as version

setup(
	name="bestofrappe",
	version=version,
	description="Theme Customization",
	author="Mahemudhusain K Manusiya",
	author_email="mahemudmanusiya52@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
