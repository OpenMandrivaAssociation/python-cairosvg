%global pypi_name cairosvg
%global pypi_oname CairoSVG

%define python2 1

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1
Group:          Development/Python
Summary:        A Simple SVG Converter for Cairo
License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
Requires:       %{pypi_name}

%rename python3-%{pypi_name}

%description
A Simple SVG Converter for Cairo

%package -n %{pypi_name}
Summary:        A Simple SVG Converter for Cairo
Group:          Development/Python

%description -n %{pypi_name}
A Simple SVG Converter for Cairo

%if %python2
%package -n python2-%{pypi_name}
Summary:        A Simple SVG Converter for Cairo
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools

%description -n python2-%{pypi_name}
A Simple SVG Converter for Cairo
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches

%if %python2
cp -a . %{py2dir}
%endif

%build
%{__python} setup.py build

%if %python2
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif

%install
%if %python2
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py%{py_ver}.egg-info

%files -n %{pypi_name}
%_bindir/cairosvg

%if %python2
%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}*
%{python2_sitelib}/%{pypi_oname}-%version-py%{py2_ver}.egg-info
%endif

