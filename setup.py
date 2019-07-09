from setuptools import setup

# Dependencies.
with open('requirements.txt') as f:
    tests_require = f.readlines()
install_requires = [t.strip() for t in tests_require]

with open('README.md') as f:
    long_description = f.read()

setup(name='movingpandas',
      version='0.99.0.dev',
      description='Trajectory handling based on GeoPandas',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/anitagraser/movingpandas',
      author='Anita Graser',
      author_email='anitagraser@gmx.at',
      license='3-Clause BSD',
      packages=['movingpandas'],
      package_data={'': ['requirements.txt']},
      classifiers=[
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: Implementation :: CPython',
      ],
      python_requires='==3.6',
      install_requires=install_requires,
      zip_safe=False)
