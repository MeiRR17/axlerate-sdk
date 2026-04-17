from setuptools import setup, find_packages

setup(
    name="axlerate-sdk",
    version="1.0.0",
    author="CMA Team",
    author_email="support@cma.local",
    description="Cisco Unified Communications SDK for AXLerate platform",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MeiRR17/CMA",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "zeep>=4.0.0",
        "lxml>=4.6.0",
        "urllib3>=1.26.0",
        "certifi>=2021.5.25",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    keywords="cisco cucm uccx axl soap telephony communications",
    project_urls={
        "Bug Reports": "https://github.com/MeiRR17/CMA/issues",
        "Source": "https://github.com/MeiRR17/CMA",
        "Documentation": "https://github.com/MeiRR17/CMA/wiki",
    },
)
