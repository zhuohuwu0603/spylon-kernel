from setuptools import setup, find_packages
import versioneer

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

setup(
    name='spylon-kernel',
    description='Jupyter metakernel for apache spark and scala',
    long_description=long_description,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='http://github.com/mariusvniekerk/spylon-kernel',
    requirements=['spylon', 'metakernel', 'jedi', 'tornado'],
    packages=list(find_packages()),
    author='Marius van Niekerk',
    author_email='marius.v.niekerk+spylon@gmail.com',
    maintainer='Marius van Niekerk',
    maintainer_email='marius.v.niekerk+spylon@gmail.com',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
