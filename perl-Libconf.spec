%define version 0.42.00
%define release %mkrel 8

Summary: Configuration file abstraction layer
Name: perl-Libconf
Version: %{version}
Release: %{release}
URL: http://www.libconf.net/
Source: http://libconf.net/download/%{name}-%{version}.tar.bz2
Patch0: perl-Libconf-0.39.9-fix-drakups.patch
Patch1: perl-Libconf-fix-doc-build.patch
License: GPL
Group: Development/Perl
#BuildArch: noarch
BuildRequires: perl-XML-LibXML perl-Text-DelimMatch
BuildRequires: perl-devel
# not automatically detected:

#%define _requires_exceptions perl(Libconf::Glueconf::KeyValue)

%description
Libconf is a wrapper to the main configuration files of the system. It's mainly
a generic parser plus many templates

%package gui
Summary: Graphic User Interface generator for any libconf module
Group: Development/Perl

%description gui
This module is able to generate a standard Gtk2 interface representing any high
level libconf module, that can be used in other Gtk2 programs.

%package samples
Summary: Set of examples programs using libconf
Group: Development/Perl
Requires: %{name}

%description samples
This module is a set of programs, using libconf. Its goal is to give
example and proof of concept around the libconf project.

%package devel
Summary: Libconf devel
Group: Development/Perl
Requires: %{name}

%description devel
Libconf devel files.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%make all CFLAGS="$RPM_OPT_FLAGSS -Wall -O2 -fpic" BINDINGS="bash c"
%make -s check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX="$RPM_BUILD_ROOT%{_prefix}" LIB_DIR="$RPM_BUILD_ROOT%{_libdir}" NAME=%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%doc ChangeLog
%{perl_vendorlib}/Libconf.pm
%{perl_vendorlib}/Libconf/*
%exclude %{perl_vendorlib}/Libconf/GUI

%files gui
%defattr(-,root,root)
%doc COPYING
%doc ChangeLog
%{perl_vendorlib}/Libconf/GUI

%files samples
%defattr(-,root,root)
%doc COPYING
%doc ChangeLog
%{_bindir}/*

%files devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libconf2xml.so
%{_includedir}/*

