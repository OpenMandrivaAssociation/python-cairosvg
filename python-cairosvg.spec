%global pypi_name cairosvg
%global pypi_oname CairoSVG


Name:           python-%{pypi_name}
Version:        2.2.1
Release:        1
Group:          Development/Python
Summary:        A Simple SVG Converter for Cairo
License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest-runner
#Requires:       %{pypi_name}
Requires:       python-cairoccfi
Requires:       python-cssselect2
Requires:       python-tinycss2
Requires:       python-defusedxml

%rename python3-%{pypi_name}

%description
A Simple SVG Converter for Cairo

%package -n %{pypi_name}
Summary:        A Simple SVG Converter for Cairo
Group:          Development/Python

%description -n %{pypi_name}
A Simple SVG Converter for Cairo

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches


%build
%{__python} setup.py build


%install

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py%{py_ver}.egg-info

%files -n %{pypi_name}
%_bindir/cairosvg


