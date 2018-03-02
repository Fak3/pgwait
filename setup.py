from setuptools import setup, find_packages


setup(
    name='pgwait',
    version='0.1',
    description='wait for postgres defined in django settings to be up',
    long_description='pgwait path.to.settings',
    author='Roman Evstifeev',
    author_email='someuniquename@gmail.com',
    url='https://github.com/Fak3/pgwait',
    license='MIT',
    py_modules=['wait_for_postgres'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pgwait = wait_for_postgres:main'],
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Android',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
