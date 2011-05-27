%define upstream_name    Gtk2-Notify
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Perl interface to libnotify
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		Gtk2-Notify-0.05-libnotify-0.7.patch
BuildRequires:	gtk+2-devel
BuildRequires:  libnotify-devel	
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
