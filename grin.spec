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
Url:            https://pypi.python.org/pypi/grin/
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


%changelog
* Thu Jul 12 2012 Lev Givon <lev@mandriva.org> 1.2.1-3
+ Revision: 809061
- Bump to rebuild.
- Remove explicit requirement of python-argparse in 2011 and later.

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 1.2.1-2mdv2011.0
+ Revision: 590804
- rebuild for py2.7

* Wed Oct 27 2010 Lev Givon <lev@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 589595
- Update to 1.2.1.

* Fri Aug 06 2010 Lev Givon <lev@mandriva.org> 1.2-1mdv2011.0
+ Revision: 566778
- Update to 1.2.

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2010.0
+ Revision: 437815
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.1.1-2mdv2009.1
+ Revision: 325579
- rebuild

* Wed Dec 10 2008 Lev Givon <lev@mandriva.org> 1.1.1-1mdv2009.1
+ Revision: 312530
- Update to 1.1.1.

* Thu Jul 17 2008 Lev Givon <lev@mandriva.org> 1.1-1mdv2009.0
+ Revision: 237805
- import grin


* Thu Jul 17 2008 Lev Givon <lev@mandriva.org> 1.1-1mdv2008.1
- Package for Mandriva.
