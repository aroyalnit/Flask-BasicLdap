"""
Flask-BasicLDAP
----------------

Basic authentication against ldap for Flask.
"""
from setuptools import setup

setup(
    name='Flask-BasicLDAP',
    version='0.9',
    license='BSD',
    author='Ian Taylor',
    author_email='ian.taylor@tobias.tv',
    description='Basic authentication against ldap for Flask',
    long_description=__doc__,
    packages=['flask_basic_ldap'],
    zip_safe=False,
    install_requires=[
        'Flask',
        'ldapom'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)