%define name	grin
%define version 1.2.1
%define release %mkrel 1

Summary:        A grep-like program for searching directories full of source code
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:        %{name}-%{version}.tar.gz
License:        BSD
Group:          Text tools
Url:            http://pypi.python.org/pypi/grin/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Requires:       python-argparse >= 1.1
BuildRequires:  python-argparse >= 1.1, python-setuptools
BuildRequires:	python-nose >= 0.10
%py_requires -d

%description
Grin is a tool for searching through directories full of source code. Although
similar to grep, it has a number of unique features:

* Recurse directories by default.
* Do not go into directories with specified names.
* Do not search files with specified extensions.
* Be able to show context lines before and after matched lines.
* Python regex syntax.
* Unless suppressed via a command line option, display the filename regardless
  of the number of files.
* Accept a file (or stdin) with a list of newline-separated filenames.
* Grep through gzipped text files.
* Be useful as a library to build custom tools quickly.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%check
nosetests

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt examples/

