import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="du.py",
    version="1.0.0",
    author="Stylix58",
    author_email="lateman-jpeg@outlook.fr",
    description="A API wrapper for Dangerous Users Data Base",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Stylix58/du.py",
    project_urls={
        "Bug Tracker": "https://github.com/Stylix58/du.py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
