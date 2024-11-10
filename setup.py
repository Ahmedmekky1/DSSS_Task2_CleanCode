from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # You can list any external dependencies here if needed, for now it's empty.
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Define the command to run the quiz
        ],
    },
    author="Ahmed",
    author_email="ahmedmekki768@gmail.com",
    description="DSSS task 2 for version control and clean code ",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Ahmedmekky1/DSSS_Task2_CleanCode.git",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
