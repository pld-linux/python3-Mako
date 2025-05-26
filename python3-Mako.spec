# TODO: beaker, dogpile.cache, lingua<4 for tests
#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Templating system for Python
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python3-Mako
Version:	1.3.10
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mako/
Source0:	https://files.pythonhosted.org/packages/source/M/Mako/mako-%{version}.tar.gz
# Source0-md5:	c9dfb2bf42827459dd505c60f2262a7c
URL:		https://www.makotemplates.org/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-devel >= 1:3.8
# import timeit
BuildRequires:	python3-devel-tools >= 1:3.8
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:47
%if %{with tests}
BuildRequires:	python3-babel
BuildRequires:	python3-markupsafe >= 0.9.2
BuildRequires:	python3-pygments >= 1.4
BuildRequires:	python3-pytest >= 3.1.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.4
Conflicts:	python-Mako < 1.1.6-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance.

%description -l pl.UTF-8
Mako jest biblioteką szablonów napisaną w języku Python. Zapewnia
przyjazną, nie XML-ową składnię, która jest kompilowana do modułów
Pythona dla zwiększenia wydajności.

%package doc
Summary:	Documentation for Python Mako module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona Mako
Group:		Documentation

%description doc
Documentation for Python Mako module.

%description doc -l pl.UTF-8
Dokumentacja do modułu Pythona Mako.

%prep
%setup -q -n mako-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/mako-render{,-3}
ln -sf mako-render-3 $RPM_BUILD_ROOT%{_bindir}/mako-render

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%attr(755,root,root) %{_bindir}/mako-render
%attr(755,root,root) %{_bindir}/mako-render-3
%{py3_sitescriptdir}/mako
%{py3_sitescriptdir}/Mako-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc doc/{_static,*.html,*.js}
