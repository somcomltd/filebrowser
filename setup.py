# coding=utf-8
from distutils.core import setup

setup(name='django-filebrowser',
      version='1',
      description='filebrowser application for django 1.3',
      author='SomCom Ltd',
      author_email='bwillmore@somcom.com',
      url='http://github.com/somcomltd/filebrowser',
      packages=['filebrowser','filebrowser.templates','filebrowser.static','filebrowser.media','filebrowser.management','filebrowser.locale'],
	  include_package_data=True,
      classifiers=[
           'Development Status :: 5 - Production/Stable',
           'Environment :: Web Environment',
           'Framework :: Django',
           'Intended Audience :: Developers',
           'Intended Audience :: Education',
           'License :: OSI Approved :: GNU General Public License (GPL)',
           'Natural Language :: English',
           'Operating System :: OS Independent',
           'Programming Language :: Python :: 2.4',
           'Programming Language :: Python :: 2.5',
           'Programming Language :: Python :: 2.6',
           'Programming Language :: Python :: 2.7',
           'Topic :: Education',
           'Topic :: Internet :: WWW/HTTP :: Site Management',
           'Topic :: Printing',
      ],
      )
