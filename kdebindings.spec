# --with-java	enable java, requires jdk (java-[sun,ibm,blackdown])
# The commented pkgs are not provided, because I have no reason to believe they work, but the 
# commented stuff works. KDE jsut does not provide the commented packages at the moment, but they will be
# available in 3.2, since Richard Dale returned to KDE (he is the maintainer of kdebindings and was away
# for some time).

%define		_state		unstable
%define		_kdever		kde-3.1-rc3

Summary:	KDE bindings to non-C++ languages
Summary(pl):	Dowi±zania KDE dla jêzyków innych ni¿ C++
Summary(pt_BR):	Bindings para KDE
Name:		kdebindings
Version:	3.1
Release:	0.5
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
Patch1:		%{name}-dcopperl.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://www.kde.org/
BuildRequires:	python-devel >= 2.1
BuildRequires:	zlib-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	pnet >= 0.4.8
BuildRequires:	perl-modules >= 5.6.1
BuildRequires:	python-devel
BuildRequires:	mono-devel
#BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
# Well... what's that?? :)
%{?_with_java:BuildRequires:	jdk}
#BuildRequires:	some-working-Java-SDK
#BuildRequires:	gcc-objc
%ifnarch ia64
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
Dowi±zania KDE/qt dla jêzyków innych ni¿ C++.

%description -l pt_BR
Bindings para o K Desktop Environment:
Provê interfaces para diferentes linguagens de programação
para uso da interface nativa do KDE


%package dcop-c
Summary:        C bindings for dcop
Summary(pl):    Dowi±zania jêzyka C dla dcop
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       libgcc

%description dcop-c
C bindings for qt

%description dcop-c -l pl
Dowi±zania jêzyka C dla dcop

#%package dcop-java
#Summary:        Java bindings for dcop
#Summary(pl):    Dowi±zania jêzyka java dla dcop
#Group:          X11/Development/Libraries
#Requires:       %{name} = %{version}
#Requires:       jdk

#%description dcop-java
#Java bindings for dcop

#%description dcop-java -l pl
#Dowi±zania jêzyka java dla dcop

#%package dcop-perl
#Summary:	Perl bindings for dcop
#Summary(pl):	Dowi±zania jêzyka perl dla dcop
#Group:		X11/Development/Libraries
#Requires:	%{name} = %{version}
#Requires:  perl-modules >= 5.6.1

#%description dcop-perl
#3Perl bindings for dcop

#%description dcop-perl -l pl
#Dowi±zania jêzyka perl dla dcop

#%package dcop-python
#Summary:	Python bindings for qt
#Summary(pl):	Dowi±zania jêzyka python dla qt
#Group:          X11/Development/Libraries
#Requires:       %{name} = %{version}
#Requires:	python-devel >= 2.1

#%description dcop-python
#Python bindings for dcop

#%description dcop-python -l pl
#Dowi±zania jêzyka python dla dcop


%ifnarch ia64
%package kmozilla
Summary:	Mozilla kpart
Summary(pl):	KPart mozilli
Group:		X11/Applications
Requires:	mozilla

%description kmozilla
This KPart allows using mozilla as a browser engine.

%description kmozilla -l pl
Kpart umozliwiajacy uzywanie mozilli jako enginu przegladarki
zamiast khtml.
%endif

%package qt-c
Summary:        C bindings for qt
Summary(pl):    Dowi±zania jêzyka C dla qt
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       libgcc
Requires:	qt >= 3.1

%description qt-c
C bindings for qt

%description qt-c -l pl
Dowi±zania jêzyka C dla qt

%package qt-csharp
Summary:        CSharp bindings for qt
Summary(pl):    Dowi±zania jêzyka CSharp dla qt
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       mono-devel >= 0.16
Requires:	pnet >= 0.4.8
Requires:	qt >= 3.1

%description qt-csharp
CSharp bindings for qt

%description qt-csharp -l pl
Dowi±zania jêzyka CSharp dla qt

%package qt-java
Summary:        Java bindings for qt
Summary(pl):    Dowi±zania jêzyka java dla qt
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       jdk
Requires:	qt >= 3.1


%description qt-java
Java bindings for qt

%description qt-java -l pl
Dowi±zania jêzyka java dla qt

#%package qt-objc
#Summary:        ObjC bindings for qt
#Summary(pl):    Dowi±zania jêzyka ObjC dla qt
#Group:          X11/Development/Libraries
#Requires:       %{name} = %{version}
#Requires:       libobjc
#Requires:	qt >= 3.1


#%description qt-objc
#ObjC bindings for qt

#%description qt-objc -l pl
#Dowi±zania jêzyka ObjC dla qt

%package kde-c
Summary:        C bindings for kde
Summary(pl):    Dowi±zania jêzyka C dla kde
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       libgcc
Requires:	kdelibs >= 3.1

%description kde-c
C bindings for kde

%description kde-c -l pl
Dowi±zania jêzyka C dla kde

%package kde-java
Summary:        Java bindings for kde
Summary(pl):    Dowi±zania jêzyka java dla kde
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}
Requires:       jdk
Requires:	kdelibs >= 3.1


%description kde-java
Java bindings for kde

%description kde-java -l pl
Dowi±zania jêzyka java dla kde

#%package kde-objc
#Summary:        ObjC bindings for kde
#Summary(pl):    Dowi±zania jêzyka ObjC dla kde
#Group:          X11/Development/Libraries
#Requires:       %{name} = %{version}
#Requires:       libobjc
#Requires:	kdelibs >= 3.1


#%description kde-objc
#ObjC bindings for kde

#%description kde-objc -l pl
#Dowi±zania jêzyka ObjC dla kde

%package smoke-qt
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka smoke dla qt
Group:		X11/Development/Libraries
Requires:	kdelibs >= 3.1

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla qt

%description smoke-qt -l pl
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla qt

%package xparts-gtk
Summary:	XParts technology for gtk
Summary(pl):	Technologia XParts dla gtk
Group:          X11/Development/Libraries
Requires:       kdelibs >= 3.1

%description xparts-gtk
XParts technology: gtk embedding.

%description xparts-gtk -l pl
Technologia XParts: zagniezd¿anie gtk.

%package xparts-kde
Summary:	XParts technology for kde
Summary(pl):	Technologia XParts dla kde
Group:          X11/Development/Libraries
Requires:       kdelibs >= 3.1

%description xparts-kde
XParts technology: kde embedding.

%description xparts-kde -l pl
Technologia XParts: zagniezd¿anie kde.

%package xparts-interfaces

Summary:	Common libraries for XParts technology
Summary(pl):	Wspó³dzielone biblioteki dla technologii XParts
Group:          X11/Development/Libraries
Requires:       kdelibs >= 3.1

%description xparts-interfaces
Common libraries for XParts technology

%description xparts-interfaces -l pl
Wspó³dzielone biblioteki dla technologii XParts


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%{__make} -f Makefile.cvs
export QTDIR=/usr/X11R6
%configure \
	%{?_with_java:--with-java=/usr/lib/java} \
	%{!?_with_java:--without-java} \
        --with-pythondir=/usr/lib/python2.1/site-packages 	
%{__make}
%{__make} -c dcopjava
%{__make} -c dcoppython
# dcop perl bindings compilation

#cd dcopperl
perl Makefile.PL <<EOF
$QTDIR/include/qt
$QTDIR/lib
%{_includedir}/kde
%{_libdir}
EOF
mkdir -p blib/bin
%{__make}
# This one should stay commented (takes too long)
#%{__make} test 
cd ..

# kalyptus compilation
cd kalyptus
%{__autoconf}
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/lib/python2.1/site-packages

%{__make} install DESTDIR="$RPM_BUILD_ROOT" destdir="$RPM_BUILD_ROOT"

# dcop perl bindings installation
%{__make} -C dcopperl install PREFIX="$RPM_BUILD_ROOT%{_prefix}"

# kalyptus instalation
cd kalyptus
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
cd ..

%{__make} -c dcopjava install DESTDIR="$RPM_BUILD_ROOT"
%{__make} -c dcoppython install DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtc.so.*
%attr(755,root,root) %{_libdir}/lib*xparts.so.*

#%files devel
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libqtc.??
#%attr(755,root,root) %{_libdir}/lib*xparts.??
#%{_includedir}/xkparts
#%{_includedir}/qtc

%ifnarch ia64
%files kmozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmozilla
%{_libdir}/*mozilla*
/usr/share/services/kmozilla.desktop
# ??? %{_applnkdir}/???/kmozilla.desktop
%endif

#%files perl
#%defattr(644,root,root,755)
#/usr/lib/perl5/site_perl/*/*/auto/qt/*
#/usr/lib/perl5/site_perl/*/*/auto/qt/.packlist
#/usr/lib/perl5/site_perl/*/*/qt.pm
#/usr/lib/perl5/site_perl/*/*/qt/Object.pm
#%{_mandir}/man3/qt.3pm*

#%files python
#%defattr(644,root,root,755)
#/usr/lib/python2.1/*/*
