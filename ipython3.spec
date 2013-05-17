# TODO:
# - check docs folder for valuable files
#
%define		pname	IPython
%define		mname	ipython
Summary:	An enhanced Interactive Python shell
Summary(pl.UTF-8):	Interaktywna powłoka języka Python
Name:		ipython3
Version:	0.13.2
Release:	1
License:	BSD
Group:		Applications/Shells
Source0:	http://archive.ipython.org/release/%{version}/%{mname}-%{version}.tar.gz
# Source0-md5:	ead3b7eb70c653b537fb9d96d71b8b2a
URL:		http://ipython.org
BuildRequires:	pydoc3
BuildRequires:	python3-devel
BuildRequires:	python3-devel-tools
BuildRequires:	python3-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python3-%{mname} = %{version}-%{release}
Suggests:	python3-zmq
Suggests:	python3-rpy2
Suggests:	python3-tornado
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPython is a free software project which tries to:

1. Provide an interactive interpreter superior to Python's default.
IPython has many features for object introspection, shell access, and
its own special command system for adding functionality when working
interactively.

2. Serve as an embeddable, ready to use interpreter for your own
programs. IPython can be started with a single call from inside
another program, providing access to the current namespace. This can
be very useful both for debugging purposes and for situations where a
blend of batch-processing and interactive exploration are needed.

3. Offer a flexible framework which can be used as the base
environment for other systems with Python as the underlying language.
Specifically scientific environments like Mathematica, IDL and Mathcad
inspired its design, but similar ideas can be useful in many fields.

This package contains IPython shell.

%description -l pl.UTF-8
IPython jest wolnym oprogramowaniem, którego celem jest:

1. Dostarczenie interaktywnej powłoki lepszej od standardowej
dostarczanej z językiem Python. IPython umożliwia badanie obiektów,
dostęp do powłoki oraz własny system poleceń, który umożliwia
rozszerzanie funkcjonalności podczas pracy interaktywnej.

2. Dostarczenie gotowego interpretera, który można dołączać do własnej
aplikacji. IPython może zostać uruchomiony za pomocą wywołania jednej
funkcji z poziomu innego programu umożliwiając jednocześnie dostęp do
aktualnej przestrzeni nazw tego programu. Może to być bardzo użyteczne
do celów takich jak śledzenie programu czy też sytuacji gdzie jest
wymagane połączenie przetwarzania wsadowego z interaktywną
introspekcją.

3. Dostarczenie szkieletu, który może zostać użyty jako podstawa
systemu, którego polecenia opierają się na zasadach języka Python.
Projekt został zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mogą być realizowane
w wielu przypadkach.

Pakiet ten zawiera powłokę IPython.

%package -n python3-ipython
Summary:	An enhanced Interactive Python shell modules
Summary(pl.UTF-8):	Moduły interaktywnej powłoki języka Python
Group:		Libraries/Python
%pyrequires_eq	python3-devel-tools
%pyrequires_eq	pydoc3

%description -n python3-ipython
IPython is a free software project which tries to:

1. Provide an interactive interpreter superior to Python's default.
IPython has many features for object introspection, shell access, and
its own special command system for adding functionality when working
interactively.

2. Serve as an embeddable, ready to use interpreter for your own
programs. IPython can be started with a single call from inside
another program, providing access to the current namespace. This can
be very useful both for debugging purposes and for situations where a
blend of batch-processing and interactive exploration are needed.

3. Offer a flexible framework which can be used as the base
environment for other systems with Python as the underlying language.
Specifically scientific environments like Mathematica, IDL and Mathcad
inspired its design, but similar ideas can be useful in many fields.

This package contains IPython modules.

%description -n python3-ipython -l pl.UTF-8
IPython jest wolnym oprogramowaniem, którego celem jest:

1. Dostarczenie interaktywnej powłoki lepszej od standardowej
dostarczanej z językiem Python. IPython umożliwia badanie obiektów,
dostęp do powłoki oraz własny system poleceń, który umożliwia
rozszerzanie funkcjonalności podczas pracy interaktywnej.

2. Dostarczenie gotowego interpretera, który można dołączać do własnej
aplikacji. IPython może zostać uruchomiony za pomocą wywołania jednej
funkcji z poziomu innego programu umożliwiając jednocześnie dostęp do
aktualnej przestrzeni nazw tego programu. Może to być bardzo użyteczne
do celów takich jak śledzenie programu czy też sytuacji gdzie jest
wymagane połączenie przetwarzania wsadowego z interaktywną
introspekcją.

3. Dostarczenie szkieletu, który może zostać użyty jako podstawa
systemu, którego polecenia opierają się na zasadach języka Python.
Projekt został zainspirowany przez oprogramowanie naukowe takie jak
Mathematica, IDL oraz Mathcad, gdzie podobne idee mogą być realizowane
w wielu przypadkach.

Pakiet ten zawiera moduły interaktywnej powłoki języka Python.

%prep
%setup -q -n %{mname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

python3 ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

for p in ipcluster ipcontroller ipengine iplogger ipython irunner pycolor; do
	mv $RPM_BUILD_ROOT%{_mandir}/man1/{$p.1,${p}3.1}
done

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/i*3.1.gz
%{_mandir}/man1/pycolor3.1.gz

%files -n python3-ipython
%defattr(644,root,root,755)
%doc docs/README.txt
%{py3_sitescriptdir}/%{pname}
%{py3_sitescriptdir}/*.egg-info
