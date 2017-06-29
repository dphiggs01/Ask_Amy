# ask_amy
Alex skills development framework for Python
pip install ask_amy -t /path/to/project-dir/dist


##### framework promotion commands
* python setup.py register
* python setup.py sdist
* python setup.py sdist upload

ask-amy-cli deploy --deploy-json-file cli_config.json
ask-amy-cli logs --log-group-name /aws/lambda/insulin_calc_skill

sphinx-apidoc -o aaa/ ~/Code/AWS/alexa/ask_amy/ask_amy
find . -type d -name dist -exec rm -rf {} \;
