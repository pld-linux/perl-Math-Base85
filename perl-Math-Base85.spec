#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Base85
Summary:	Math::Base85 Perl module for base 85 numbers, as referenced by RFC 1924
Summary(pl.UTF-8):	Moduł Perla Math::Base85 do liczb o podstawie 85, opisanych w RFC 1924
Name:		perl-Math-Base85
Version:	0.2
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a2914651dc680fd22661f35213211d3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC 1924 (1 April 1996) describes a compact, fixed-size representation
of IPv6 addresses which uses a base 85 number system. This module
handles some of the uglier details of it.

%description -l pl.UTF-8
RFC 1924 (z 1 kwietnia 1996) opisuje zwartą, o stałym rozmiarze
reprezentację adresów IPv6, używającą systemu o podstawie 85. Ten
moduł obsługuje parę brzydszych szczegółów tej reprezentacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Base85.pm
%{_mandir}/man3/*
