%define name grin
%define version  1.1
%define release %mkrel 1

Summary: A grep-like program for searching directories full of source code
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: BSD
Group: Text tools
Url: https://svn.enthought.com/enthought/wiki/Grin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python-argparse
BuildRequires: python-devel, python-argparse, python-setuptools
BuildArch: noarch

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
%__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc *.txt examples/

