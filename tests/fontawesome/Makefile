# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile _static/css/fontawesome-all.css
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

FONTAWESOME_VERSION = 5.0.13
FONTAWESOME_NAME    = fontawesome-free-${FONTAWESOME_VERSION}
FONTAWESOME_URL     = https://use.fontawesome.com/releases/v${FONTAWESOME_VERSION}/${FONTAWESOME_NAME}.zip
TEMPDIR	            := $(shell mktemp -d)

_static/css/fontawesome-all.css:
	mkdir -p "$(SOURCEDIR)/_static/css" "${TEMPDIR}"
	wget "${FONTAWESOME_URL}" -O "${TEMPDIR}/${FONTAWESOME_NAME}.zip" 
	unzip -q "${TEMPDIR}/${FONTAWESOME_NAME}.zip" -d "${TEMPDIR}"
	-cp -rf "${TEMPDIR}/${FONTAWESOME_NAME}/web-fonts-with-css/css/fontawesome-all.css" "$(SOURCEDIR)/_static/css/"
	-cp -rf "${TEMPDIR}/${FONTAWESOME_NAME}/web-fonts-with-css/webfonts" "$(SOURCEDIR)/_static/" 
	rm -rf "${TEMPDIR}"
