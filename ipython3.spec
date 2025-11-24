#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (need to wait for fulfilling dependencies in PLD)

Summary:	An enhanced Interactive Python shell
Summary(pl.UTF-8):	Interaktywna powłoka języka Python
Name:		ipython3
Version:	9.7.0
Release:	1
License:	BSD
Group:		Applications/Shells
#Source0Download: https://pypi.org/simple/ipython/
Source0:	https://files.pythonhosted.org/packages/source/i/ipython/ipython-%{version}.tar.gz
# Source0-md5:	887aeb42be4a3a4e04e5b4009a227250
URL:		https://ipython.org/
BuildRequires:	pydoc3 >= 1:3.11
BuildRequires:	python3-devel >= 1:3.11
BuildRequires:	python3-devel-tools >= 1:3.11
BuildRequires:	python3-setuptools >= 1:77.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.747
%if %{with tests}
BuildRequires:	python3-backcall
# optional (test_extra) as comments
#BuildRequires:	python3-curio
BuildRequires:	python3-decorator >= 4.3.2
BuildRequires:	python3-ipykernel >= 6.30.1
BuildRequires:	python3-ipython-pygments-lexers >= 1.0.0
BuildRequires:	python3-jedi >= 0.18.1
#BuildRequires:	python3-jupyter_ai
#BuildRequires:	python3-matplotlib >= 3.9.1
BuildRequires:	python3-matplotlib_inline >= 0.1.5
#BuildRequires:	python3-nbclient
#BuildRequires:	python3-nbformat
BuildRequires:	python3-numpy >= 1.27
BuildRequires:	python3-packaging >= 20.1.0
#BuildRequires:	python3-pandas >= 2.1.1
BuildRequires:	python3-pexpect > 4.3
BuildRequires:	python3-prompt_toolkit >= 3.0.41
BuildRequires:	python3-prompt_toolkit < 3.1.0
BuildRequires:	python3-pygments >= 2.11.0
BuildRequires:	python3-pytest >= 7.0.0
BuildRequires:	python3-pytest-asyncio >= 1.0.0
BuildRequires:	python3-requests
BuildRequires:	python3-stack-data >= 0.6.0
BuildRequires:	python3-testpath >= 0.2
BuildRequires:	python3-traitlets >= 5.13.0
#BuildRequires:	python3-trio >= 0.1.0
%if "%{py3_ver}" == "3.11"
BuildRequires:	python3-typing_extensions >= 4.6
%endif
%endif
%if %{with doc}
BuildRequires:	python3-docrepr
BuildRequires:	python3-exceptiongroup
BuildRequires:	python3-intersphinx_registry
BuildRequires:	python3-ipykernel
BuildRequires:	python3-matplotlib
BuildRequires:	python3-sphinx_rtd_theme >= 0.1.8
BuildRequires:	python3-sphinx_toml >= 0.0.4
BuildRequires:	python3-typing_extensions
BuildRequires:	sphinx-pdg-3 >= 8.0
%endif
Requires:	python3-ipython = %{version}-%{release}
Suggests:	python3-PyQt5
Suggests:	python3-zmq
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
Requires:	pydoc3 >= 1:3.11
Requires:	python3-devel-tools >= 1:3.11

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

%package -n python3-ipython-apidocs
Summary:	API documentation for Python IPython module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona IPython
Group:		Documentation

%description -n python3-ipython-apidocs
API documentation for Python IPython module.

%description -n python3-ipython-apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona IPython.

%prep
%setup -q -n ipython-%{version}

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	examples/Embedding/embed_class_long.py \
	"examples/IPython Kernel/ipython-get-history.py" \
	"examples/IPython Kernel/gui"/gui-*.py

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	PYTHON=%{__python3} \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py3_install

cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ipython
%attr(755,root,root) %{_bindir}/ipython3
%{_mandir}/man1/ipython.1*

%files -n python3-ipython
%defattr(644,root,root,755)
%doc COPYING.rst LICENSE README.rst
%{py3_sitescriptdir}/IPython
%{py3_sitescriptdir}/ipython-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}

%if %{with doc}
%files -n python3-ipython-apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_images,_static,about,api,config,coredev,development,install,interactive,parallel,whatsnew,*.html,*.js}
%endif
