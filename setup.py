from setuptools import setup, find_packages


setup(
    name='crystal_engine',
    version='0.0.1',
    license='MIT',
    author="Mikael Chowdhury",
    author_email='mikael@shaficonsultancy.com',
    packages=find_packages('crystal_engien'),
    package_dir={'': 'crystal_engine'},
    url='https://github.com/mikael-chowdhury/crystal-engine',
    keywords='python game-engine 2d pygame-wrapper lightweight',
    install_requires=["pygame", "pickle", "socket", "_thread"],
)