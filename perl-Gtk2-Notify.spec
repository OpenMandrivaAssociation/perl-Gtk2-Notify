%define modname	Gtk2-Notify
%define modver	0.05

Summary:	Perl interface to libnotify
Name:		perl-%{modname}
Version:	%{modver}
Release:	21
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Gtk2-Notify
Source0:	https://cpan.metacpan.org/authors/id/F/FL/FLORA/Gtk2-Notify-%{modver}.tar.gz
Source1:	perl-Gtk2-Notify.rpmlintrc
Patch0:		Gtk2-Notify-0.05-libnotify-0.7.patch
BuildRequires:	make
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Gtk2
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-devel

%description
Perl interface to libnotify.

%prep
%setup -qn %{modname}-%{modver}
%autopatch -p1

%build
%define _disable_ld_no_undefined 1
%__perl Makefile.PL INSTALLDIRS=vendor
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

