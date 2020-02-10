import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="the_trials_of_aghrial"
    version="0.0.1",
    author="Kevin Lueke",
    author_email="your@email.com",
    url="https://github.com/kevinlueke/the_trials_of_aghrial",
    description="Python text adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

