Summary:	KDE bindings to non-C++ languages
Summary(pl):	Dowi±zania KDE dla jêzyków innych ni¿ C++
Summary(pt_BR):	Bindings para KDE
Name:		kdebindings
Version:	3.0.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
URL:		http://www.kde.org/
BuildRequires:	python-devel >= 2.1
BuildRequires:	zlib-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
#BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
# Well... what's that?? :)
#BuildRequires:	some-working-Java-SDK
BuildRequires:	gcc-objc
%ifnarch ia64
# Remove the "#" when the build system has finally run out of crack
BuildRequires: mozilla-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

%description
Bindings fot the K Desktop Environment:
Provides interfaces to many diferent programming languages to use KDE native resources and
widgets.

%description -l pl
Dowi±zania KDE/DCOP dla jêzyków innych ni¿ C++.

%description -l pt_BR
Bindings para o K Desktop Environment:
Provê interfaces para diferentes linguagens de programação
para uso da interface nativa do KDE

%package devel
Summary:	Development files for kdebindings
Summary(pl):	Pliki dla programistów u¿ywaj±cych kdebindings
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the KDE bindings.

Install kdebindings-devel if you want to develop non-KDE applications
that talk to KDE.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych KDE bindings, do rozwoju aplikacji
nie-KDE komunikuj±cych siê z KDE.

%package kmozilla
Summary:	KDE bindings to Mozilla
Summary(pl):	Dowi±zania KDE dla Mozilli
Group:		X11/Applications
Requires:	mozilla

%description kmozilla
KDE bindings to Mozilla.

%description kmozilla -l pl
Dowi±zania KDE dla Mozilli.

%package perl
Summary:	Perl bindings to DCOP
Summary(pl):	Dowi±zania DCOP dla Perla
Group:		X11/Development/Libraries
Requires:	perl >= 5.6.0

%description perl
Perl bindings to the DCOP interprocess communication protocol used by
KDE.

%description perl -l pl
Dowi±zania dla Perla do protoko³u komunikacji miêdzyprocesowej DCOP,
u¿ywanego przez KDE.

%package python
Summary:	Python bindings to DCOP
Summary(pl):	Dowi±zania DCOP dla Pythona
Group:		X11/Development/Libraries
Requires:	python >= 2.1

%description python
Python bindings to the DCOP interprocess communication protocol used
by KDE.

%description python -l pl
Dowi±zania dla Pythona do protoko³u komunikacji miêdzyprocesowej DCOP,
u¿ywanego przez KDE.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#%{__make} -f Makefile.cvs

#QTDIR=%{_prefix}

%configure \
	--with-pythondir=/usr/lib/python2.1/site-packages \
	--enable-objc \
	--without-java

## UGLY workaround for python bug...
#cat >fPIC <<EOF
##!/bin/sh
#exec %{__cc} -fPIC \$@
#EOF
#chmod +x fPIC
#PATH="$PATH:`pwd`"; export PATH
## end workaround
#
#%{__make}
#%{__make} -C dcoppython
#cd dcopperl
#perl Makefile.PL <<EOF
#$QTDIR/include
#$QTDIR/lib
#%{_includedir}/kde
#%{_libdir}
#EOF
#mkdir -p blib/bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/lib/python2.1/site-packages

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

#%{__make} -C dcoppython install DESTDIR="$RPM_BUILD_ROOT"
#%{__make} -C dcopperl install PREFIX="$RPM_BUILD_ROOT%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdcopc.so.*
%attr(755,root,root) %{_libdir}/lib*xparts.so.*

%files python
%defattr(644,root,root,755)
/usr/lib/python2.1/*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdcopc.??
%attr(755,root,root) %{_libdir}/lib*xparts.??
%{_includedir}/xkparts
%{_includedir}/dcopc

%ifnarch ia64
%files kmozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmozilla
%{_libdir}/*mozilla*
/usr/share/services/kmozilla.desktop
# ??? %{_applnkdir}/???/kmozilla.desktop
%endif

%files perl
%defattr(644,root,root,755)
/usr/lib/perl5/site_perl/*/*/auto/DCOP/*
/usr/lib/perl5/site_perl/*/*/auto/DCOP/.packlist
/usr/lib/perl5/site_perl/*/*/DCOP.pm
/usr/lib/perl5/site_perl/*/*/DCOP/Object.pm
%{_mandir}/man3/DCOP.3pm*
