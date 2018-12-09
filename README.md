# DrEA Project - surya Package

`surya` upload a set of research articles, parse them and summerize a selected part of these papers in pdf format.

## How it works :
	* Parsed data in each article submitted to the solution;
	* Summarize articles;
	* Advanced research inside tagged articles;

## Inputs:
Articles provided in a PDF format.

## Setup :
	* Parse articles :
	The docker image of `science parse` tool for parsing the loaded pdfs :
		* For dowloading the image : `docker pull allenai/scienceparse:2.0.3`
		* For running the docker image : `docker run -d -p 8080:8080 --rm allenai/scienceparse:2.0.3`
		* For parsing a pdf paper : `curl -v -H "Content-type: application/pdf" --data-binary @paper.pdf "http://localhost:8080/v1"`

	* Summarize articles :
	The [sumy python package](https://pypi.org/project/sumy/) for summerizing the loaded papers :
		* Install this package using pip : `pip install sumy`
		* Install the required dependencies of this package : `python -c "import nltk; nltk.download('punkt')"`

## Project Structure:
	* `setup.py`: Source file
	* `requirements.txt`: List of external dependencies
	* `drealib/`: package's modules sources.
	* `tests/`: Development tests of the project.
	* `articles/`: Articles used for development.
	* `parsed_articles/`: Results Directory
	* `buffer/`: used to write Science-Parser results in json format.

### Additional Notes :
	* The original version was based on the [PyTeaser](https://github.com/alanbuxton/PyTeaserPython3) :
		Two options for installing `PyTeaser` :
			1/ https://alanbuxton.wordpress.com/2017/09/12/adventures-in-upgrading-a-python-text-summarisation-library/
			2/ Install from sources using `sudo python setup.py install`

	* Two alternatives of `science parse` were considered :
		* [spv2](https://github.com/allenai/spv2) for science parse version 2 -> This software was not functional and extract only metadata from pdfs
			* A docker image is provided at : `docker pull allenai/spv2:2.10`
			* For running this image : `docker run -d -p 8081:8081 allenai/spv2:2.10`
			* Call the API : `curl -v --data-binary @paper.pdf "http://localhost:8081/v1/json/pdf"`
		* [GROBID](https://github.com/kermitt2/grobid) tool : especially the [grobid-client-python](https://github.com/kermitt2/grobid-client-python)
		This software returns no errors but no outputs. The use of the `GROBID REST API` let parse a paper. The tei.xml output need to reconsider all the load process of a parsed pdf.
			* This API was build from the official docker image:
				* Downloading the image : `docker pull lfoppiano/grobid:0.5.2`
				* Running the API : `docker run -d -t --rm --init -p 8080:8070 -p 8081:8071 lfoppiano/grobid:0.5.2`
