import setuptools

setuptools.setup(
    name="micromap-api",
    version="0.0.1",
    author="Edwin Bennink",
    author_email="H.E.Bennink@umcutrecht.nl",
    description="MicroMap API module",
    packages=['micromap_api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Development Status :: 2 - Pre-Alpha"
    ],
    python_requires='>=3.14',
    install_requires=[
        'fastapi~=0.138.1',
        'uvicorn~=0.49.0',
        'pydantic~=2.13.4',
        'pydantic-settings~=2.14.2',
        'sqlalchemy~=2.0.51',
        'psycopg2-binary~=2.9.12'
    ],
    extras_require={
        'wsgi support': ['a2wsgi~=1.10.10'],
    }
)
