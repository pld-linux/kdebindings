Summary:	KDE bindings to non-C++ languages
Summary(pl):	Dowi±zania KDE dla jêzyków innych ni¿ C++
Name:		kdebindings
Version:	2.2
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.2/src/%{name}-%{version}.tar.bz2
URL:		http://www.kde.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	python-devel >= 2.1
BuildRequires:	zlib-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdelibs-sound-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	fam-devel
%ifnarch ia64
# Remove the "#" when the build system has finally run out of crack
# BuildRequires: mozilla-devel
%endif

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
KDE/DCOP bindings to non-C++ languages.

%description -l pl
Dowi±zania KDE/DCOP dla jêzyków innych ni¿ C++.

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
%{__make} -f Makefile.cvs
QTDIR=%{_prefix}
%configure \
	--without-java \
	--with-pythondir=/usr/lib/python2.1/site-packages

# UGLY workaround for python bug...
cat >fPIC <<EOF
#!/bin/sh
exec %{__cc} -fPIC \$@
EOF
chmod +x fPIC
PATH="$PATH:`pwd`"; export PATH
# end workaround

%{__make}
%{__make} -C dcoppython
cd dcopperl
perl Makefile.PL <<EOF
$QTDIR/include
$QTDIR/lib
%{_includedir}/kde
%{_libdir}
EOF
mkdir -p blib/bin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/python2.1/site-packages
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
%{__make} -C dcoppython install DESTDIR="$RPM_BUILD_ROOT"
%{__make} -C dcopperl install PREFIX="$RPM_BUILD_ROOT%{_prefix}"

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
