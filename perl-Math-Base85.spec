#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Base85
Summary:	Math::Base85 Perl module for base 85 numbers, as referenced by RFC 1924
Summary(pl):	Modu³ Perla Math::Base85 do liczb o podstawie 85, opisanych w RFC 1924
Name:		perl-Math-Base85
Version:	0.2
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC 1924 (1 April 1996) describes a compact, fixed-size representation
of IPv6 addresses which uses a base 85 number system. This module
handles some of the uglier details of it.

%description -l pl
RFC 1924 (z 1 kwietnia 1996) opisuje zwart±, o sta³ym rozmiarze
reprezentacjê adresów IPv6, u¿ywaj±c± systemu o podstawie 85. Ten
modu³ obs³uguje parê brzydszych szczegó³ów tej reprezentacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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
