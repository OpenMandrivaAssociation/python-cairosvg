%global module cairosvg
%global oname CairoSVG

Name:		python-cairosvg
Version:	2.9.0
Release:	1
Group:		Development/Python
Summary:	A Simple SVG Converter based on Cairo
License:	LGPL-3.0-or-later
URL:		https://pypi.python.org/pypi/cairosvg
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cairocffi)
BuildRequires:	python%{pyver}dist(cssselect2)
BuildRequires:	python%{pyver}dist(defusedxml)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tinycss2)

%rename python3-%{module}

%description
A Simple SVG Converter based on Cairo.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%_bindir/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%version-py%{py_ver}.egg-info
