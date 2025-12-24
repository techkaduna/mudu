from setuptools import setup, find_packages


def read_file(filename):
    with open(filename, "r") as _file:
        output = _file.read()
    return output


setup(
    name="mudu",
    version="1.1.500",
    packages=find_packages(),
    description="A python package for unit-aware numerical data handling.",
    long_description=read_file("README.rst"),
    long_description_content_type="text/x-rst",
    author="Kolawole Andrew",
    author_email="andrewolakola@gmail.com",
    url="https://github.com/techkaduna/mudu",
    py_modules=[
        "mudu",
    ],
    install_requires=[
        "sympy==1.13.3",
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: OS Independent", 
    ],
    keywords = [
        "units", "physics", "engineering",
        "dimension-analysis", "unit-conversion",
    ],
)
