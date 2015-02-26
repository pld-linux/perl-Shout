#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Shout - Perl glue for libshout streaming source library
Summary(pl.UTF-8):	Shout - perlowy interfejs do biblioteki strumieni libshout
Name:		perl-Shout
Version:	2.1
Release:	9
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://downloads.xiph.org/releases/libshout/Shout-%{version}.tar.gz
# Source0-md5:	7171eb8f9e60d6c5cc6c469ba0f32dc9
URL:		http://icecast.org/
BuildRequires:	libshout-devel >= 2.1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an object-oriented interface to libshout, an Ogg Vorbis
and MP3 streaming library that allows applications to easily
communicate and broadcast to an Icecast streaming media server. It
handles the socket connections, metadata communication, and data
streaming for the calling application, and lets developers focus on
feature sets instead of implementation details.

%description -l pl.UTF-8
Ten moduł jest zorientowanym obiektowo interfejsem do libshout -
biblioteki strumieni Ogg Vorbis i MP3 umożliwiającej aplikacjom łatwe
komunikowanie się i rozgłaszanie do serwera strumieni multimedialnych
Icecast. Obsługuje połączenia przez gniazda, komunikację z metadanymi,
strumienie danych dla aplikacji wywołującej oraz pozwala programistom
skupić się na możliwościach zamiast szczegółach implementacji.

%prep
%setup -q -n Shout-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Shout.pm
%dir %{perl_vendorarch}/auto/Shout
%{perl_vendorarch}/auto/Shout/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Shout/Shout.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/Shout.3*
