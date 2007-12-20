%define realname   Gtk2-Notify

Name:		perl-%{realname}
Version:    0.04
Release:    %mkrel 1
License:	GPL
Group:		Development/Perl
Summary:    Perl interface to libnotify
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Gtk2/Gtk2-Notify-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  libnotify-devel	
BuildRequires:  perl-Gtk2
BuildRequires:  perl-Test-Exception
%description
Perl interface to libnotify.

%prep
%setup -q -n Gtk2-Notify-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# test requires dbus service and X11 to be used 
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*
