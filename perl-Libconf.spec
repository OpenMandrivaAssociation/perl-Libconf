Summary:	Configuration file abstraction layer
Name:		perl-Libconf
Version:	0.42.10
Release:	8
License:	GPLv2+
Group:		Development/Perl
URL:		http://www.libconf.net/
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

%define debug_package %{nil}

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

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.42.10-6mdv2012.0
+ Revision: 765387
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.42.10-5
+ Revision: 763903
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.42.10-4
+ Revision: 763282
- force it
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.42.10-3
+ Revision: 676493
- fix build
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.42.10-2mdv2011.0
+ Revision: 426515
- rebuild

* Wed Jul 23 2008 Adam Williamson <awilliamson@mandriva.org> 0.42.10-1mdv2009.0
+ Revision: 241229
- add perl510.patch to fix build with perl 5.10
- new release 0.42.10
- don't package COPYING
- new license policy
- clean spec and descriptions

  + Thierry Vignaud <tv@mandriva.org>
    - fix "#%%define is forbidden"
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.42.00-8mdv2008.0
+ Revision: 69027
- patch 1: fix build with unversionnated doc directories
- sanitize
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.42.00-6mdv2008.0
+ Revision: 23366
- rebuild


* Mon Dec 05 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.42.00-5mdk
- add BuildRequires: perl-devel perl-Text-DelimMatch

* Fri Dec 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.42.00-4mdk
- fix build on x86_64

* Fri Nov 25 2005 Antoine Ginies <aginies@n3.mandriva.com> 0.42.00-3mdk
- waiting for next release, new name (libconf):
- remove bindings to do not provides ruby lib in a perl-Libconf package...

* Thu Nov 24 2005 Antoine Ginies <aginies@n3.mandriva.com> 0.42.00-2mdk
- add bindings
- fix requires pb (remove all perl requires)
- remove builarch: noarch

* Mon Nov 21 2005 Antoine Ginies <aginies@n3.mandriva.com> 0.42.00-1mdk
- 0.42.00 release

* Thu Nov 03 2005 Antoine Ginies <aginies@n1.mandriva.com> 0.40.00-1mdk
- 0.40.00 version :
  - a lot of bug corrections
  - DelimMatch is now used as delimiter engine
  - better comments support in high level layer
  - warnings/errors have now their handler, and verbosity is customisable

* Wed Jun 29 2005 Antoine Ginies <aginies@n2.mandriva.com> 0.39.21-1mdk
- now use official Sshd template
- release 0.39.21

* Mon Jun 13 2005 Antoine Ginies <aginies@n2.mandrakesoft.com> 0.39.19-1mdk
- 0.39.19 release

* Tue Jun 07 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.39.18-2mdk
- add Ssshd_config.pm for testing purpose (need to fix tabulation pb)

* Thu Jun 02 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.39.18-1mdk
- 0.39.18 release

* Tue May 31 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.39.16-3mdk
- need nightly build to get Samba wizard working

* Tue May 31 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.39.16-2mdk
- add missing requires

* Wed May 25 2005 Antoine Giniès <aginies@mandriva.com> 0.39.16-1mdk
- 0.39.16 release

* Thu Feb 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.39.9-2mdk
- patch 0: fix reading empty nut config file

* Thu Feb 10 2005 Michael Scherer <misc@mandrake.org> 0.39.9-1mdk
- new release
- rpmbuildupdatable
- use wildcard

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.33-2mdk 
- BuildRequires

* Thu Apr 22 2004 dams <dams@libconf.net> 0.33-1mdk
- basically desktop section in systemconf added
- some bug fixes and corrections
- synchronization for ng-drakdm

* Wed Apr 07 2004 dams <dams@libconf.net> 0.32-2mdk
- corrected rpm url
- included full changelog

* Wed Apr 07 2004 dams <dams@libconf.net> 0.32-1mdk
- glueconf hierarchy change debug for SystemConf

* Wed Apr 07 2004 dams <dams@libconf.net> 0.31-1mdk
- glueconf hierarchy change debug for applications

* Tue Apr 06 2004 dams <dams@libconf.net> 0.30-1mdk
- new templates (exported[c]shell)
- debugging
- various cleaning and ordering tasks
- work in progress with drakxtools-ng (sourceforge)

* Fri Mar 05 2004 dams <dams@tuxfamily.org> 0.29-1mdk
- new glueconf hierarchy
- xf86config libconf template
- cleanup

* Tue Jan 13 2004 dams <dams@tuxfamily.org> 0.27-1mdk
- added upsusers template
- some xml export/import premises. Still alpha

* Thu Nov 27 2003 dams <dams@tuxfamily.org> 0.26-1mdk
- cleaning, debugging, corrections
- titi joined the party, making libconf perl_checker compliant
- libconf_isdn_answering added

* Fri Nov 14 2003 dams <dams@tuxfamily.org> 0.25-1mdk
- minor corrections
- libconf_lan added

* Fri Nov 14 2003 dams <dams@tuxfamily.org> 0.24-1mdk
- rewrote comments handler, corrected bug
- corrected DirectoryWrapper
- added interfaces list and fetures in lan_conf

* Sun Nov 02 2003 dams <dams@tuxfamily.org> 0.23-1mdk
- better data validation
- improved GUI
- more glueconf modules
- network system module completed
- lot of other stuff...
- packaging and miscellaneous corrections, thanks to tvignaud

* Wed Aug 27 2003 dams <dams@tuxfamily.org> 0.22-1mdk
- added more glueconf modules
- best gui generator
- best data specification / mapping
- new package -samples, provides executables as prototypes

* Tue Jul 29 2003 dams <dams@tuxfamily.org> 0.21-1mdk
- samba template rewritten
- swat-clone application initiated
- gui generator getBestWidget added
- data specification added in samba template, and implemented in main libconf module.

* Sat Jun 14 2003 dams <dams@tuxfamily.org> 0.20-1mdk
- version 0.20
- added Libconf GUI GTK2 module

* Wed Jun 04 2003 dams <dams@tuxfamily.org> 0.19-1mdk
- version 0.19
- added Samba Glueconf module
- various fix and improvements

* Sun May 25 2003 dams <dams@tuxfamily.org> 0.18-1mdk
- version 0.18
- corrected Glueconf installation
- added Libconf::System in tarball and rpm

* Sat May 24 2003 dams <dams@tuxfamily.org> 0.17-1mdk
- version 0.17
- new comments handler (inline comments are supported)
- rewritten System/DirectoryWrapper.pm

* Sun Apr 06 2003 dams <dams@tuxfamily.org> 0.16-1mdk
- version 0.16

* Sun Feb 02 2003 dams <dams@tuxfamily.org> 0.1-1mdk
- first mdk package

