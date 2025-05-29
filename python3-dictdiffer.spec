# TODO: finish tests (package dependencies)
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define		module		dictdiffer
Summary:	Dictdiffer - a library that helps you to diff and patch dictionaries
Summary(pl.UTF-8):	Dictdiffer - biblioteka pomagająca porównywać i łatać słowniki
Name:		python3-%{module}
Version:	0.9.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dictdiffer/
Source0:	https://files.pythonhosted.org/packages/source/d/dictdiffer/%{module}-%{version}.tar.gz
# Source0-md5:	524b353b969300d4dc6aa6720c953657
URL:		https://github.com/inveniosoftware/dictdiffer
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pytest-runner >= 2.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 3.1.0
%if %{with tests}
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-pytest-cov >= 2.10.1
BuildRequires:	python3-pytest-isort >= 1.2.0
BuildRequires:	python3-pytest-pycodestyle >= 2.2.0
BuildRequires:	python3-pytest-pydocstyle >= 2.2.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme >= 0.2
BuildRequires:	sphinx-pdg-3 >= 3
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dictdiffer is a helper module that helps you to diff and patch
dictionaries.

%description -l pl.UTF-8
Dictdiffer to moduł pomocniczy, pomagający porównywać i łatać
słowniki.

%package apidocs
Summary:	API documentation for Python dictdiffer module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona dictdiffer
Group:		Documentation

%description apidocs
API documentation for Python dictdiffer module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona dictdiffer.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin,... \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES CONTRIBUTING.rst MAINTAINERS README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
