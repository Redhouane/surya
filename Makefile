PART = patch

run-sp:
	docker run -d -p 8080:8080 --rm allenai/scienceparse:2.0.3

test-upload-s3-pypi:
	s3pypi --bucket tests-pypi.mycoretechs.com --private

upload-s3-pypi:
	s3pypi --bucket pypi.mycoretechs.com --private

update-version-number:
	bumpversion $(PART)