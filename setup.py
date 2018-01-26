from setuptools import setup


def readme():
    with open('README.md') as readme_:
        return readme_.read()

setup(
    name='coral_client',
    version='0.1',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    description='Sample client & mock API created for HotelsPro Coral API',
    url="https://github.com/gurayinan/coral_api",
    author="Guray Inan",
    author_email="gurayinan@windowslive.com",
    license="MIT",
    packages=['cli_app'],
    install_requires=['flask', 'requests'],
    long_description=readme(),
    entry_points="""
    [console_scripts]
    coral_api = cli_app.client:main
    """
)
