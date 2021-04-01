import setuptools

try:
    with open('README.rst', 'r') as readme:
        long_description = readme.read()
except Exception:
    long_description = None

with open('requirements.txt') as f:
    requirements = f.readlines()

version = "0.0.6"

setuptools.setup(
    name="furiousflemingo-mohithg",
    version=version,
    author="Mohith G",
    license='MIT License',
    author_email="mohithgm@gmail.com",
    description="Command line wrapper for git and dvc",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="https://github.com/mohithg/furious-flemingo",
    packages=setuptools.find_packages(exclude=("tests",)),
    entry_points={
        'console_scripts': [
            'ff=ff.cli:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)