import setuptools
setuptools.setup(
    name="boosted_depth",
    version="0.0.1",
    author="Chris Careaga",
    author_email="chris_careaga@sfu.ca",
    description='a packaged version of the code for BoostingMonocularDepth',
    url="",
    packages=setuptools.find_packages(),
    license="",
    python_requires=">3.6",
    install_requires=[
        'torch>=2.0.1',
        'torchvision>=0.15.2',
        'numpy>=1.23.5',
        'opencv-python>=4.8.0.76',
    ]
)
