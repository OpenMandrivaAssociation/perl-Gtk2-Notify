%define upstream_name    Gtk2-Notify
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:    Perl interface to libnotify
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Gtk2-Notify-0.05-libnotify-0.7.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  perl-Gtk2
BuildRequires:  perl-Test-Exception
BuildRequires:	perl-devel

%description
Perl interface to libnotify.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .libnotify7~

%build
%define _disable_ld_no_undefined 1
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OTHERLDFLAGS="%ldflags"

%check
# test requires dbus service and X11 to be used 
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-6
+ Revision: 765294
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri May 27 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.50.0-4
+ Revision: 680361
- clean out old junk
- fix libnotify api patch

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 0.50.0-3
+ Revision: 650837
- add fedora patch to build with latest libnotify

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 564485
- rebuild for perl 5.12.1

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 406061
- rebuild using %%perl_convert_version

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 302824
- update to new version 0.05

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2008.1
+ Revision: 152109
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2008.1
+ Revision: 97494
- update to new version 0.04

* Wed Jun 27 2007 Michael Scherer <misc@mandriva.org> 0.03-1mdv2008.0
+ Revision: 44932
- Import perl-Gtk2-Notify



* Sun Jun 03 2007 Michael Scherer <misc@mandriva.org> 0.03-1mdv2008.0
- First Mandriva package
