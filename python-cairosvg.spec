%global pypi_name cairosvg
%global pypi_oname CairoSVG


Name:           python-%{pypi_name}
Version:	2.4.1
Release:	1
Group:          Development/Python
Summary:        A Simple SVG Converter for Cairo
License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/e7/a8/ea6866828347a7e6bd3c11cf6eef888d13537e8786bc0cec9643f5a761d3/CairoSVG-2.4.1.tar.gz
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
