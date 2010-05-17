#
# Copyright (c) 2006-2009 rPath, Inc.
#
# This program is distributed under the terms of the Common Public License,
# version 1.0. A copy of this license should have been distributed with this
# source file in a file called LICENSE. If it is not present, the license
# is always available at http://www.rpath.com/permanent/licenses/CPL-1.0.
#
# This program is distributed in the hope that it will be useful, but
# without any warranty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the Common Public License for
# full details.
#

all: default-subdirs default-all

.PHONY: clean dist install html docs

export TOPDIR = $(shell pwd)
# DISTDIR is not a typo: "rpath-product-definition" is the name
# of the package that contains the code; "product-definition" is
# the name of packages containing a product definition
export DISTDIR = $(TOPDIR)/rpath-product-definition-$(VERSION)

SUBDIRS=rpath_proddef xsd doc

dist_files = $(extra_files)

.PHONY: clean dist install subdirs

subdirs: default-subdirs

install: install-subdirs install-compat

clean: clean-subdirs default-clean


generate:
	make -C rpath_proddef generate

validate-schema:
	make -C xsd validate-schema



install-compat:
	# Compatibility stubs for old rbuild (RPCL-63)
	mkdir -p $(DESTDIR)$(sitedir)rpath_common/proddef
	echo "from rpath_proddef.api1 import *" >$(DESTDIR)$(sitedir)rpath_common/proddef/__init__.py
	echo "from rpath_proddef.api1 import *" >$(DESTDIR)$(sitedir)rpath_common/proddef/api1.py
	python -c "from compileall import *; compile_dir('$(DESTDIR)$(sitedir)rpath_common/proddef', 10, '$(sitedir)rpath_common/proddef')"
	python -O -c "from compileall import *; compile_dir('$(DESTDIR)$(sitedir)rpath_common/proddef', 10, '$(sitedir)rpath_common/proddef')"

dist:
	if ! grep "^Changes in $(VERSION)" NEWS > /dev/null 2>&1; then \
		echo "no NEWS entry"; \
		exit 1; \
	fi
	$(MAKE) forcedist


archive:
	hg archive --exclude .hgignore -t tbz2 $(DISTDIR).tar.bz2

forcedist: archive

doc: html
html: default-subdirs
	scripts/generate_docs.sh

forcetag:
	hg tag -f product-definition-$(VERSION)
tag:
	hg tag product-definition-$(VERSION)

clean: clean-subdirs default-clean
	@rm -rf $(DISTDIR).tar.bz2

include Make.rules
include Make.defs
 
# vim: set sts=8 sw=8 noexpandtab :
