#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		dictdiffer
Summary:	Dictdiffer is a library that helps you to diff and patch dictionaries
Name:		python-%{module}
Version:	0.8.1
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dictdiffer/
Source0:	https://files.pythonhosted.org/packages/source/d/dictdiffer/%{module}-%{version}.tar.gz
# Source0-md5:	3185fe683d976282bf6313de14b7c7e9
URL:		https://github.com/inveniosoftware/dictdiffer
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dictdiffer is a helper module that helps you to diff and patch
dictionaries.

%package -n python3-%{module}
Summary:	Dictdiffer is a library that helps you to diff and patch dictionaries
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
Dictdiffer is a helper module that helps you to diff and patch
dictionaries.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES CONTRIBUTING.rst MAINTAINERS README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES CONTRIBUTING.rst MAINTAINERS README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
