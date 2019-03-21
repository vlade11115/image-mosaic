import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='image-mosaic',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/vlade11115/image-mosaic',
    license='BSD 3-Clause License',
    description='Produce a mosaic from images.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pillow',
    ],
    entry_points={'console_scripts': [
        'mosaic = mosaic.colour_mosaic:main'
    ]},
)
