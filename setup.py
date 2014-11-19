from setuptools import setup, find_packages

setup(
    name="ircyall",
    version='0.1',
    author="Yuvi Panda",
    author_email="yuvipanda@gmail.com",
    description="IRC Notifier that accepts input via HTTP",
    license="Apache2",
    url="https://pypi.python.org/pypi/ircnotifier/0.0.2",
    packages=find_packages(),
    scripts=['scripts/ircyall']
)
