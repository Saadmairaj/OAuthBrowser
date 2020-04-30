from setuptools import setup


def long_description():
    with open('README.md') as f:
        long_dis = f.read()
    try:
        with open('Changelog.md') as f:
            long_dis += str('\n'+f.read())
    except:
        pass
    return long_dis

install_requires = []

setup(
    name="OAuthBrowser",
    version="0.0.1",
    description="OAuthBrowser is module to do authentications and web scraping.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Saadmairaj/OAuthBrowser",
    author="Saad Mairaj",
    author_email="Saadmairaj@yahoo.in",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: MacOS X"
    ],
    keywords=['web scraping', 'macos', 'OAuth 2.0',
              'authentication', 'login in', 'automation'],
    packages=["OAuthBrowser"],
    include_package_data=True,
    install_requires=install_requires
)
