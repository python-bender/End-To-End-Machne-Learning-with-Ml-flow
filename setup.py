import setuptools

with open("README.md", 'r',encoding='utf-8') as f:
    long_description = f.read()
    
    
__version__="0.0.0"

REPO_NAME ="End-To-End-Machne-Learning-with-Ml-flow"
AUTHOR_USER_NAME = "AgbajeAbdulAzeez"
SRC_REPO = 'mlproject'
AUTHOR_EMAIL="agbajeabdula111@gmail.com"


setuptools.setup(
    nam=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python packagefor ml app",
    long_description_content=long_description,
    url=f'https//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        
    },
    package_dir ={"":"src"},
    packages=setuptools.find_packages(where='src')
)