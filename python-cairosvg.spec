%global pypi_name cairosvg
%global pypi_oname CairoSVG


Name:           python-%{pypi_name}
Version:	2.5.2
Release:	2
Group:          Development/Python
Summary:        A Simple SVG Converter for Cairo
License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/0e/8a/618700c8d6a1dbef8bbe6da97d57c47363aa14b486140a4df9f75f31ba4f/CairoSVG-2.5.2.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pytest-runner
Requires:       python-cairocffi
Requires:       python-cssselect2
Requires:       python-tinycss2
Requires:       python-defusedxml

%rename python3-%{pypi_name}

%description
A Simple SVG Converter for Cairo

%prep
%autosetup -p1 -n %{pypi_oname}-%{version}

%build
%{__python} setup.py build


%install

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%_bindir/cairosvg
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/%{pypi_oname}-%version-py%{py_ver}.egg-info
