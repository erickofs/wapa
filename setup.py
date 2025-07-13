from setuptools import setup, find_packages

setup(
    name="wapa",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "keyboard",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    author="erickofs",
    description="A text-based RPG game inspired by Hero Wars",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/erickofs/wapa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "wapa=src.core.game_state:main",
        ],
    },
)
