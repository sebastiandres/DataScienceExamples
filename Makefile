# SWEET'S MAKEFILE
# .PHONY. allows to always execute the instruction, (no checking for the existence)

TESTS = -5 -4 -3 -2 -1 0 1 2 3 4 5 20 21 22 23 24 25

.PHONY.: options
options:
	@grep [a-z]: Makefile

.PHONY.: pull
pull:
	git pull origin master

.PHONY.: push
push:
	git push -u origin master

.PHONY.: clean
clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.py~" -delete
	@find . -name "*.pyo" -delete
	@rm -rf
