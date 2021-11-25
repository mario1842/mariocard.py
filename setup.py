from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='mariocard.py',
  version='1.0.0',
  description='This is simple maker for cards in discord bot.',
  long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='mario1842',
  author_email='mario1842.info@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord level card welcome',
  packages=find_packages(),
  install_requires=['Pillow','easy-pil', 'discord.py'] 
)
