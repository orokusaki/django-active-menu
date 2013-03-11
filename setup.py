from setuptools import setup, find_packages


# Calculate the version based on active_menu.VERSION
version = '.'.join([str(v) for v in __import__('active_menu').VERSION])

setup(
    name='active_menu',
    description=(
        'A model-less Django app providing a template tag for adding '
        'class="active" to links whose views (or parents\') are active '
    ),
    version=version,
    author='Michael Angeletti',
    author_email='michael [at] angelettigroup [dot] com',
    url='https://github.com/orokusaki/django-active-menu/',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
)
