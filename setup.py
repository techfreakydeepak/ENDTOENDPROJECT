from setuptools import find_packages, setup

setup(
    name='GemstonePricePrediction',
    version='0.0.1',
    author='Deepak Singh',
    author_email='itsdeepaksingh00@gmail.com',
    description='A package for predicting Gemstone prices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/GemstonePricePrediction',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
         #List your dependencies here
        'numpy',
        'pandas',
         'scikit-learn',
         'matplotlib',
         'seaborn',
         'tensorflow',
         'ipykernel',
    ]
)

setup(
    name='GemstonePricePrediction',
    version='0.0.1',
    author='Deepak Singh',
    author_email='itsdeepaksingh00@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)