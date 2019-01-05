# DrEA Project - surya Package

`surya` upload a set of research articles, parse and summerize a selected part of these papers.

## How it works :
	1. Parsed data in each article uploaded (in PDF format);
	2. Summarize articles;
	3. Advanced research inside tagged articles;

## Inputs:
Articles provided in a PDF format.

## Setup :
	1. Parse articles :
	The docker image of `science parse` tool for parsing the loaded pdfs :
		* For dowloading the image : `docker pull allenai/scienceparse:2.0.3`
		* For running the docker image : `docker run -d -p 8080:8080 --rm allenai/scienceparse:2.0.3`
		* For parsing a pdf paper : `curl -v -H "Content-type: application/pdf" --data-binary @paper.pdf "http://localhost:8080/v1"`

	2. Summarize articles :
	The [sumy python package](https://pypi.org/project/sumy/) for summerizing the loaded papers :
		* Install this package using pip : `pip install sumy`
		* Install the required dependencies of this package : `python -c "import nltk; nltk.download('punkt')"`

## Project Structure:
	1. `setup.py`: setup file
	2. `requirements.txt`: List of external dependencies
	3. `surya/`: package's sources.
		* `__init__.py` : Project global variables and logging config
		* `paper.py` : Paper class
		* `paper_utils.py` : Module with utils functions for papers manipulation (parsing, summerize etc..)
		* `text_cleaner.py` : Module with methods for cleaning texts.
	4. `tests/`: Development tests of the project:
		* `unit/` : Unit tests related to functionnalities
		* `integration/` : Integration test related to summary production
		* `fixtures/` : Pdfs exemple articles (from different journal) for developement and tests.
	5. `laboratory_experimentations`: Experimentations about some other unused librairies. Especially about summerization.

### Additional Notes :
	1. The original version was based on the [PyTeaser](https://github.com/alanbuxton/PyTeaserPython3) :
		Two options for installing `PyTeaser` :
			* https://alanbuxton.wordpress.com/2017/09/12/adventures-in-upgrading-a-python-text-summarisation-library/
			* Install from sources using `sudo python setup.py install`

	2. Two alternatives of `science parse` were considered :
		* [spv2](https://github.com/allenai/spv2) for science parse version 2 -> This software was not functional and extract only metadata from pdfs
			- A docker image is provided at : `docker pull allenai/spv2:2.10`
			- For running this image : `docker run -d -p 8081:8081 allenai/spv2:2.10`
			- Call the API : `curl -v --data-binary @paper.pdf "http://localhost:8081/v1/json/pdf"`
		* [GROBID](https://github.com/kermitt2/grobid) tool : especially the [grobid-client-python](https://github.com/kermitt2/grobid-client-python)
		This software returns no errors but no outputs. The use of the `GROBID REST API` let parse a paper. The tei.xml output need to reconsider all the load process of a parsed pdf.
			- This API was build from the official docker image:
				- Downloading the image : `docker pull lfoppiano/grobid:0.5.2`
				- Running the API : `docker run -d -t --rm --init -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.5.2`
