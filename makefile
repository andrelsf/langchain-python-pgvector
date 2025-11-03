.ONESHELL:
.PHONY: install clean ingest search chat

install: 
	python3 -m pip install -r requirements.txt
	python3 -m pip install --upgrade pip

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +

ingest:
	python3 init_ingest.py

search:
	python3 init_search.py

chat:
	python3 init_chat.py