%include	/usr/lib/rpm/macros.python

#
# todo:
# 1. pl description
# 2. %{py_sitedir}/%{pname}/UserConfig/*.py ???
# 3. python-ipython subpackage with all modules
#    - main package will contain only the script to run shell (maybe some docs)
#

%define pname IPython

Summary:	An enhanced Interactive Python shell
Summary(pl):	Interaktywna pow³oka jêzyka Python
Name:		ipython
Version:	0.2.8
Release:	0.1
License:	LGPL
Group:		Applications/Shells
Source0:	http://www-hep.colorado.edu/~fperez/ipython/dist/%{pname}-%{version}.tar.gz
URL:		http://www-hep.colorado.edu/~fperez/ipython/
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%requires_eq	python-modules
%requires_eq	python-pydoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPython is a free software project which tries to:

1. Provide an interactive interpreter superior to Python's default. IPython has
   many features for object introspection, shell access, and its own special
   command system for adding functionality when working interactively.

2. Serve as an embeddable, ready to use interpreter for your own programs.
   IPython can be started with a single call from inside another program,
   providing access to the current namespace. This can be very useful both for
   debugging purposes and for situations where a blend of batch-processing and
   interactive exploration are needed.

3. Offer a flexible framework which can be used as the base environment for
   other systems with Python as the underlying language. Specifically scientific
   environments like Mathematica, IDL and Mathcad inspired its design, but similar
   ideas can be useful in many fields.

%prep
%setup  -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

mv doc/manual/manual.pdf doc/
mv doc/manual/ doc/html/

gzip -9nf *.txt doc/{*.txt,ChangeLog,ToDo,BUGS}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/html doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{pname}
%dir %{py_sitedir}/%{pname}/Extensions
%dir %{py_sitedir}/%{pname}/UserConfig
%{py_sitedir}/%{pname}/*.py?
%{py_sitedir}/%{pname}/Extensions/*.py?
%{py_sitedir}/%{pname}/UserConfig/*.py
