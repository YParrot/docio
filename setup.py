import setuptools


install_requires = []


def readme() -> str:
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    name='docio',
    version='0.0.1',
    packages=setuptools.find_packages(),
    description="Input/Output text",
    long_descriptiondescription=readme(),
    classifiers=[
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    license='GPLv3',
    author='Motoki Naruse',
    author_email='motoki@naru.se',
    url='https://github.com/narusemotoki/docio',
    keywords='text extract',
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'flake8',
        ],
    }
)
