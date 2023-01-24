from setuptools import setup, find_packages

with open('D:\\University Work\\Cyber Security Final Year\\COMP3000\\Github\\FaceCCTV\\AI\\face_detection\\__init__.py') as f:
    info = {}
    for line in f:
      if line.startswith('version'):
            exec(line, info)
            break


setup_info = dict(
      name='face_detection',
      version=1.0,
      author='Harry Parker',
      author_email='hspark5@outlook.com',
      description='A face detection library for Python using Wider Face dataset',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.10',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Scientific/Engineering :: Image Recognition',
            'Topic :: Scientific/Engineering :: Image Processing',
      ],

      # package info
      packages=find_packages(),
)
