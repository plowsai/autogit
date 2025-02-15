from setuptools import setup

setup(
    name='watch-and-push',
    version='0.1.0',
    description='A tool to automatically push changes to GitHub when files are modified.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/watch-and-push',  # Update with your GitHub URL
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=[],
    scripts=['watch_and_push.sh'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
) 