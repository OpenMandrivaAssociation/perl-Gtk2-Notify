%define realname   Gtk2-Notify

Name:		perl-%{realname}
Version:    0.03
Release:    %mkrel 1
License:	Unknow
Group:		Development/Perl
Summary:    TODO
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Gtk2/Gtk2-Notify-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:  libnotify-devel	
BuildRequires:  perl-Gtk2
%description
TODO

%prep
%setup -q -n Gtk2-Notify-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

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
