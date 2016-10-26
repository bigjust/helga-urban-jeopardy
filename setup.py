from setuptools import setup, find_packages

version = '0.1.0'

setup(name="helga-urban-jeopardy",
      version=version,
      description=('HALP'),
      classifiers=[
          'Development Status :: 1 - Planning',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='irc bot urban-jeopardy',
      author='bigjust',
      author_email='bigjust@lambdaphil.es',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga_urban-jeopardy'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'urban-jeopardy = helga_urban-jeopardy:urban-jeopardy',
          ],
      ),
)
