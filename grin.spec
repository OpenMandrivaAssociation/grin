%define name	grin
%define version 1.2.1
%define	rel		3
%if %mdkversion	< 201100
%define release	%mkrel %{rel}
%else
%define release %{rel}
%endif

%if %{_use_internal_dependency_generator}
%define __noautoreq 'pythonegg\\(argparse\\)'
%else
%define _requires_exceptions pythonegg(argparse)
%endif

Summary:        A grep-like program for searching directories full of source code
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:		http://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
License:        BSD
Group:          Text tools
Url:            http://pypi.python.org/pypi/grin/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
%if %mdkversion < 201100
Requires:		python-argparse >= 1.1
BuildRequires:  python-argparse >= 1.1
%endif
BuildRequires:	python-setuptools
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%check
nosetests

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt examples/
%_bindir/%{name}*
%py_sitedir/%{name}*
