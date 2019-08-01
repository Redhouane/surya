# surya Package

**surya** is a python package that upload a set of research articles, parse and summarize the entire corpus or some selected sections (method, results, etc...).

## Input:
A directory containing articles to study in a PDF format.

## How it works :
1. Parse each article and transform it to an instance of Paper class;
2. Summarize selected sections;
3. Match usefull nformation into a set of articles (objectives, methods, results, etc...);

## Setup :
### Parse articles :
surya use `science parse`, an open source article parser integrated as a docker version :

- To download the `science parse` docker image : `docker pull allenai/scienceparse:2.0.3`
- To this image : `docker run -d -p 8080:8080 --rm allenai/scienceparse:2.0.3`
- To parse an article : `curl -v -H "Content-type: application/pdf" --data-binary @paper.pdf "http://localhost:8080/v1"`
    
### Summarize articles :
We use the [sumy package](https://pypi.org/project/sumy/) for summarizing the loaded papers :

* Install this package using pip : `pip install sumy`
* Install this package's required dependencies : `python -c "import nltk; nltk.download('punkt')"`

## Project Structure:
1. `setup.py`: s=Setup file
2. `Pipfile` and `Pipfile.lock`: List of external dependencies
3. `Makefile`: Contains a set of command lines
4. `surya-s3-pypi.json`: Our AWS CloudFormation architecture template used to deploy this package
5. `.bumpversion.cfg` : Configuration script for automatically increment package's version number
6. `surya/`: package's sources.
    * `__init__.py` : Project global variables and logging config
    * `paper.py` : Paper class
    * `paper_utils.py` : Module with utils functions for papers manipulation (parsing, summerize etc..)
    * `text_cleaner.py` : Module with methods for cleaning texts.
    * `paper_charts.py` : Module with functions that produce data to display within charts
7. `tests/`: Development tests of the project:
    * `unit/` : Unit tests related to features
    * `integration/` : Integration test related to summary production
    * `fixtures/` : Set of PDFs articles (from different journals) for development and tests.
8. `laboratory_experimentations/`: Experiences about some other unused libraries. Especially about to summarize.

### Additional Notes :
1. The original summarize version was based on the [PyTeaser](https://github.com/alanbuxton/PyTeaserPython3) :
    Two options for installing `PyTeaser` :
    
    * https://alanbuxton.wordpress.com/2017/09/12/adventures-in-upgrading-a-python-text-summarisation-library/
    * Install from sources using `sudo python setup.py install`

2. Two alternatives of `science parse` were considered :
    * [spv2](https://github.com/allenai/spv2) for science parse version 2 -> This software was not functional and extract only metadata from pdfs
        - A docker image is provided at : `docker pull allenai/spv2:2.10`
        - For running this image : `docker run -d -p 8081:8081 allenai/spv2:2.10`
        - Call the API : `curl -v --data-binary @paper.pdf "http://localhost:8081/v1/json/pdf"`
    * [GROBID](https://github.com/kermitt2/grobid) tool : especially the [grobid-client-python](https://github.com/kermitt2/grobid-client-python)
    This software returns no errors but no outputs. The use of the `GROBID REST API` let parse a paper. The `tei.xml` output need to reconsider all the load process of a parsed pdf.
        - This API was build from the official docker image:
            - Downloading the image : `docker pull lfoppiano/grobid:0.5.2`
            - Running the API : `docker run -d -t --rm --init -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.5.2`
