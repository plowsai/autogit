from setuptools import setup, find_packages

setup(
    name='autocommit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'autocommit=autocommit.autocommit:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Automatically commit and push changes to a git repository.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/autocommit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
