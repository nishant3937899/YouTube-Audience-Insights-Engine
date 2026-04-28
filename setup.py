import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()

version='0.0.0'

REPO_Name='YOUTUBE AUDIENCE INSIGHT ENGINE'
AUTHOR_USER_NAME='Nishant Chandra Verma'
SRC_REPO = "youtube_insight_engine"
AUTHOR_EMAIL='nishantchandra987@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=version,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='IN this project we take the top 500 comments of the youtube video and do sentiment analysis on it ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nishant3937899/YouTube-Audience-Insights-Engine',
    package_dir={"":'src'},
    packages=setuptools.find_packages(where="src")
)