install_dependencies:
	pip install -r requirements.txt

create_venv:
	virtualenv -p python3.7 twitter

run:
	python bots/get_twitter.py