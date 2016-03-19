%define debug_package %{nil}

Summary:	Configuration file abstraction layer
Name:		perl-Libconf
Version:	0.42.10
Release:	18
License:	GPLv2+
Group:		Development/Perl
Url:		http://www.libconf.net/
Source0:	http://libconf.net/download/%{name}-%{version}.tar.bz2
Source1:	%{name}.rpmlintrc
Patch0:		perl-Libconf-0.39.9-fix-drakups.patch
Patch1:		perl-Libconf-fix-doc-build.patch
# Fix build for perl 5.10: suggested by http://patches.ubuntu.com/by-release/extracted/debian/o/openser/1.3.0-3/04_perl_for_perl5.10.dpatch
# for a similar issue in openser, from Ubuntu - AdamW 2008/07
Patch2:		perl-Libconf-0.42.10-perl510.patch
Patch3:		perl-Libconf-0.42.10-buildfix.diff
BuildRequires:	perl-XML-LibXML
BuildRequires:	perl-Text-DelimMatch
BuildRequires:	perl-devel
# not automatically detected:
#define _requires_exceptions perl(Libconf::Glueconf::KeyValue)

%description
Libconf is a wrapper to the main configuration files of the system.
It's mainly a generic parser plus many templates.

%package gui
Summary:	Graphic User Interface generator for any libconf module
Group:		Development/Perl

%description gui
This module is able to generate a standard GTK+ 2 interface
representing any high level libconf module, that can be used in other
GTK+ 2 programs.

%package samples
Summary:	Set of examples programs using libconf
Group:		Development/Perl
Requires:	%{name}

%description samples
This module is a set of programs, using libconf. Its goal is to give
example and proof of concept around the libconf project.

%package devel
Summary:	Libconf devel
Group:		Development/Perl
Requires:	%{name}

%description devel
Libconf devel files.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1 -b .perl510
%patch3 -p0

%build
%make all CFLAGS="%{optflags} -Wall -O2 -fpic" BINDINGS="bash c"
%make -s check

%install
%makeinstall PREFIX="%{buildroot}%{_prefix}" LIB_DIR="%{buildroot}%{_libdir}" NAME=%{name}

%files
%doc ChangeLog
%{perl_vendorlib}/Libconf.pm
%{perl_vendorlib}/Libconf/*
%exclude %{perl_vendorlib}/Libconf/GUI

%files gui
%doc ChangeLog
%{perl_vendorlib}/Libconf/GUI

%files samples
%doc ChangeLog
%{_bindir}/*

%files devel
%{_libdir}/libconf2xml.so
%{_includedir}/*

