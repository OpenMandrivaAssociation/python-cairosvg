%global pypi_name cairosvg
%global pypi_oname CairoSVG

%define python3 0

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

%description
A Simple SVG Converter for Cairo

%package -n %{pypi_name}
Summary:        A Simple SVG Converter for Cairo
Group:          Development/Python

%description -n %{pypi_name}
A Simple SVG Converter for Cairo

%if %python3
%package -n python3-%{pypi_name}
Summary:        A Simple SVG Converter for Cairo
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
A Simple SVG Converter for Cairo
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches

%if %python3
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if %python3
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if %python3
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py%{py_ver}.egg-info

%files -n %{pypi_name}
%_bindir/cairosvg

%if %python3
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}*
%{python3_sitelib}/%{pypi_oname}-%version-py%{py3_ver}.egg-info
%endif

