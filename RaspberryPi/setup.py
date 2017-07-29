from setuptools import setup, find_packages


setup(
    name="echoserver",
    version='1.0',
    packages=find_packages(),
    install_requires=['logbook', 'flask', 'tornado', 'click', 'ujson', 'requests', 'rxv'],
    entry_points={
        'console_scripts': [
            'echoserverd = echoserver.run_server:main'
        ]
    }
)
