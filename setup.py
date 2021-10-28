from setuptools import setup, find_packages

long_description = 'Apple Silicon "top" for Mac OS'

setup(
    name='asitop',
    version='0.0.2',
    author='Timothy Liu',
    author_email='tlkh.xms@gmail.com',
    url='https://github.com/tlkh/asitop',
    description='Apple Silicon "top" for Mac OS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'asitop = asitop.asitop:main'
            ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ),
    keywords='asitop',
    install_requires=[
        "dashing",
        "psutil",
    ],
    zip_safe=False
)