#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-urltools
Version  : 1.7.3
Release  : 14
URL      : https://cran.r-project.org/src/contrib/urltools_1.7.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/urltools_1.7.3.tar.gz
Summary  : Vectorised Tools for URL Handling and Parsing
Group    : Development/Tools
License  : MIT
Requires: R-urltools-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-httr
Requires: R-triebeard
BuildRequires : R-Rcpp
BuildRequires : R-httr
BuildRequires : R-triebeard
BuildRequires : buildreq-R

%description
## urltools
A package for elegantly handling and parsing URLs from within R.
__Author:__ Oliver Keyes, Jay Jacobs<br/>
__License:__ [MIT](http://opensource.org/licenses/MIT)<br/>
__Status:__ Stable

%package lib
Summary: lib components for the R-urltools package.
Group: Libraries

%description lib
lib components for the R-urltools package.


%prep
%setup -q -c -n urltools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555300086

%install
export SOURCE_DATE_EPOCH=1555300086
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urltools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library urltools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc urltools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/urltools/DESCRIPTION
/usr/lib64/R/library/urltools/INDEX
/usr/lib64/R/library/urltools/LICENSE
/usr/lib64/R/library/urltools/Meta/Rd.rds
/usr/lib64/R/library/urltools/Meta/data.rds
/usr/lib64/R/library/urltools/Meta/features.rds
/usr/lib64/R/library/urltools/Meta/hsearch.rds
/usr/lib64/R/library/urltools/Meta/links.rds
/usr/lib64/R/library/urltools/Meta/nsInfo.rds
/usr/lib64/R/library/urltools/Meta/package.rds
/usr/lib64/R/library/urltools/Meta/vignette.rds
/usr/lib64/R/library/urltools/NAMESPACE
/usr/lib64/R/library/urltools/NEWS
/usr/lib64/R/library/urltools/R/urltools
/usr/lib64/R/library/urltools/R/urltools.rdb
/usr/lib64/R/library/urltools/R/urltools.rdx
/usr/lib64/R/library/urltools/data/Rdata.rdb
/usr/lib64/R/library/urltools/data/Rdata.rds
/usr/lib64/R/library/urltools/data/Rdata.rdx
/usr/lib64/R/library/urltools/doc/index.html
/usr/lib64/R/library/urltools/doc/urltools.R
/usr/lib64/R/library/urltools/doc/urltools.Rmd
/usr/lib64/R/library/urltools/doc/urltools.html
/usr/lib64/R/library/urltools/help/AnIndex
/usr/lib64/R/library/urltools/help/aliases.rds
/usr/lib64/R/library/urltools/help/paths.rds
/usr/lib64/R/library/urltools/help/urltools.rdb
/usr/lib64/R/library/urltools/help/urltools.rdx
/usr/lib64/R/library/urltools/html/00Index.html
/usr/lib64/R/library/urltools/html/R.css
/usr/lib64/R/library/urltools/tests/testthat.R
/usr/lib64/R/library/urltools/tests/testthat/test_credentials.R
/usr/lib64/R/library/urltools/tests/testthat/test_encoding.R
/usr/lib64/R/library/urltools/tests/testthat/test_get_set.R
/usr/lib64/R/library/urltools/tests/testthat/test_memory.R
/usr/lib64/R/library/urltools/tests/testthat/test_parameters.R
/usr/lib64/R/library/urltools/tests/testthat/test_parsing.R
/usr/lib64/R/library/urltools/tests/testthat/test_puny.R
/usr/lib64/R/library/urltools/tests/testthat/test_suffixes.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/urltools/libs/urltools.so
/usr/lib64/R/library/urltools/libs/urltools.so.avx2
/usr/lib64/R/library/urltools/libs/urltools.so.avx512
