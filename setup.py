import setuptools

__version__ = '0.3.0'
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='portainer-cli',
    version=__version__,
    author='Ilhasoft\'s Web Team',
    author_email='contato@ilhasoft.com.br',
    description='Command line interface to easy communicate to your ' +
                'Portainer application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ilhasoft/portainer-cli',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    scripts=['portainer-cli'],
    install_requires=[
        'plac>=1.4.5',
        'requests>=2.32.5',
        'validators>=0.35.0',
    ],
    python_requires='>=3.13',
)
