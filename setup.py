
from setuptools import setup

setup(name='krisk',
      version='0.1.0',
      description='Echarts Statistical Visualization for Python Data Science',
      author='Jonathan Napitupulu',
      author_email='napitupulu.jon@gmail.com',
      download_url='https://github.com/napjon/krisk/',
      url='https://github.com/napjon/krisk/',
      license='BSD (3-clause)',
      packages=['krisk',
                'krisk.plot'],
      package_data={'krisk':['static/*.js',
                             'static/*.html']},
      classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD 3-clause License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5']
     )