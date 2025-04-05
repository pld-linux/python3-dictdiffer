%define		module		dictdiffer
Summary:	Dictdiffer - a library that helps you to diff and patch dictionaries
Summary(pl.UTF-8):	Dictdiffer - biblioteka pomagająca porównywać i łatać słowniki
Name:		python3-%{module}
Version:	0.9.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dictdiffer/
Source0:	https://files.pythonhosted.org/packages/source/d/dictdiffer/%{module}-%{version}.tar.gz
# Source0-md5:	524b353b969300d4dc6aa6720c953657
URL:		https://github.com/inveniosoftware/dictdiffer
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-pytest-runner >= 2.7
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dictdiffer is a helper module that helps you to diff and patch
dictionaries.

%description -l pl.UTF-8
Dictdiffer to moduł pomocniczy, pomagający porównywać i łatać
słowniki.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS CHANGES CONTRIBUTING.rst MAINTAINERS README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
