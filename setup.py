from setuptools import setup, find_packages

__author__ = 'Loredana Sideri'
__email__ = "loredana.sideri@gmail.com"

# Get the long description from the README file
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#    long_description = f.read()

setup(name='freeproxies',
      version='0.1',
      description='Rotate proxy ip from free proxy list',
      url='https://github.com/blackat87/freeproxies',
      author='Loredana Sideri',
      author_email='loredana.sideri@gmail.com',
      use_2to3=True,
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',

          "Operating System :: OS Independent",

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3'
      ],
      keywords=['free proxy'],
      install_requires=['fake_useragent',  'urllib3', 'beautifulsoup'],
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "docs"]),
      )