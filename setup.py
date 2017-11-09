from setuptools import setup, find_packages

setup(
    name='webdriver_pool',
    version='1.0.1',
    description='A package for building Webdriver Pool when using Selenium',
    packages=find_packages(),
    url='https://github.com/Jiramew/webdriver_pool',
    license='BSD License',
    author='Jiramew',
    author_email='hanbingflying@sina.com',
    maintainer='Jiramew',
    maintainer_email='hanbingflying@sina.com',
    platforms=["all"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'selenium>=3.5.0',
    ]
)
