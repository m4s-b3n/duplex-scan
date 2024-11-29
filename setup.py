"""Setup script for the project."""

from setuptools import find_packages, setup

setup(
    name="duplex-scan",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["Flask", "pypdf"],
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": [
            "duplex-scan=your_package.module:main_function",  # Adjust as needed
        ],
    },
)
