#
# Conditional build:
%bcond_with	java	# enable java, requires jdk (java-[sun,ibm,blackdown])
#
# The commented pkgs are not provided, because I have no reason to believe they
# work, but the commented stuff works. KDE jsut does not provide the commented
# packages at the moment, but they will be available in 3.2, since Richard Dale
# returned to KDE (he is the maintainer of kdebindings and was away for some
# time).

%define		_state		stable
%define		_ver		3.2.2

Summary:	KDE bindings to non-C++ languages
Summary(pl):	Dowi±zania KDE dla jêzyków innych ni¿ C++
Summary(pt_BR):	Bindings para KDE
Name:		kdebindings
Version:	%{_ver}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5c00277c009ea97e7ca70c613f5fc87b
Patch0:		%{name}-am.patch
Patch1:		%{name}-dcopperl.patch
Patch2:		%{name}-DESTDIR.patch
# This is an ugly hack to make am work without regenerating
Patch3:		%{name}-am_hack.patch
URL:		http://www.kde.org/
#BuildRequires:	fam-devel
#BuildRequires:	gcc-objc
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
%{?with_java:BuildRequires:	jdk}
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	mono-devel >= 0.16
BuildRequires:	pnet >= 0.4.8
#BuildRequires:	perl-modules >= 5.6.1
#BuildRequires:	python-devel >= 2.1
%ifnarch ia64
BuildRequires:	mozilla-devel
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bindings for the K Desktop Environment: provide interfaces to many
diferent programming languages to use KDE native resources and
widgets.

%description -l pl
Dowi±zania KDE/qt dla jêzyków innych ni¿ C++ pozwalaj±ce u¿ywaæ
natywnych dla KDE zasobów i widgetów.

%description -l pt_BR
Bindings para o K Desktop Environment:
Provê interfaces para diferentes linguagens de programação
para uso da interface nativa do KDE.

%package dcop-c
Summary:	C bindings for DCOP
Summary(pl):	Dowi±zania jêzyka C dla DCOP
Group:		X11/Development/Libraries
Requires:	libgcc
Requires:	kdelibs >= 9:%{version}
Requires:	gtk+ >= 1.2.6

%description dcop-c
C bindings for DCOP.

%description dcop-c -l pl
Dowi±zania jêzyka C dla DCOP.

%package dcop-c-devel
Summary:	dcop-c header files
Summary(pl):	Pliki nag³ówkowe dla dcop-c
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	gtk+-devel >= 1.2.6
Requires:	%{name}-dcop-c = %{version}-%{release}

%description dcop-c-devel
dcop-c header files.

%description dcop-c-devel -l pl
Pliki nag³ówkowe dla dcop-c.

#%package dcop-java
#Summary:	Java bindings for DCOP
#Summary(pl):	Dowi±zania jêzyka Java dla DCOP
#Group:		X11/Development/Libraries
#Requires:	jdk
#Requires:	kdelibs >= 9:%{version}
#Requires:	qt >= 3.1
#Requires:	libart_lgpl

#%description dcop-java
#Java bindings for DCOP.

#%description dcop-java -l pl
#Dowi±zania jêzyka Java dla DCOP.

#%package dcop-perl
#Summary:	Perl bindings for DCOP
#Summary(pl):	Dowi±zania jêzyka Perl dla DCOP
#Group:		X11/Development/Libraries
#Requires:	perl-modules >= 5.6.1
#Requires:	kdelibs >= 9:%{version}
#Requires:	qt >= 3.1

#%description dcop-perl
#Perl bindings for DCOP.

#%description dcop-perl -l pl
#Dowi±zania jêzyka Perl dla DCOP.

#%package dcop-python
#Summary:	Python bindings for DCOP
#Summary(pl):	Dowi±zania jêzyka Python dla DCOP
#Group:		X11/Development/Libraries
#Requires:	python-devel >= 2.1
#Requires:	kdelibs >= 9:%{version}
#Requires:	qt >= 3.1

#%description dcop-python
#Python bindings for DCOP

#%description dcop-python -l pl
#Dowi±zania jêzyka Python dla DCOP.

#%package kalyptus
#Summary:	QT/KDE bindings generator
#Summary(pl):	Generator dowi±zañ do QT/KDE
#Group:		X11/Development/Libraries
#Requires:	perl >= 5.6.1
#Requires:	kdelibs >= 9:%{version}
#Requires:	qt >= 3.1

#%description kalyptus
#KALYPTUS creates language bindings for Qt and KDE C++ libraries
#directly from the headers.
#
#%description kalyptus -l pl
#Kalyptus s³u¿y do generowania dowi±zañ do QT/KDE bezpo¶rednio
#z plików nag³ówkowych.

%package kde-c
Summary:	C bindings for KDE
Summary(pl):	Dowi±zania jêzyka C dla KDE
Group:		X11/Development/Libraries
Requires:	libgcc
Requires:	%{name}-qt-c = %{version}-%{release}
Requires:	kdelibs >= 9:%{version}

%description kde-c
C bindings for KDE.

%description kde-c -l pl
Dowi±zania jêzyka C dla KDE.

%package kde-java
Summary:	Java bindings for KDE
Summary(pl):	Dowi±zania jêzyka Java dla KDE
Group:		X11/Development/Libraries
Requires:	jdk
Requires:	%{name}-qt-java = %{version}-%{release}
Requires:	kdelibs >= 9:%{version}

%description kde-java
Java bindings for KDE.

%description kde-java -l pl
Dowi±zania jêzyka Java dla KDE.

%package kde-java-devel
Summary:	kde-java header files
Summary(pl):	Pliki nag³ówkowe dla kde-java
Group:		X11/Development/Libraries
Requires:	%{name}-kde-java = %{version}-%{release}
Requires:	%{name}-qt-java-devel = %{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

%description kde-java-devel
kde-java header files.

%description kde-java-devel -l pl
Pliki nag³ówkowe dla kde-java.

%package kjsembed
Summary:	A library for embedding the KJS Javascript interpreter
Summary(pl):	Biblioteka pozwalaj±ca na zagnie¿d¿anie intepretera KJS
Group:		X11/Development/Libraries
Requires:	kdelibs >= 9:%{version}

%description kjsembed
A library for embedding the KJS Javascript interpreter in application.

%description kjsembed -l pl
Biblioteka pozwalaj±ca na zagnie¿d¿anie intepretera javascript - KJS,
w dowolnej aplikacji.

%package  kjsembed-devel
Summary:	kjsembed header files
Summary(pl):	Pliki nag³ówkowe dla kjsembed
Group:		X11/Development/Libraries
Requires:	%{name}-kjsembed = %{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

%description kjsembed-devel
kjsembed header files.

%description kjsembed-devel -l pl
Pliki nag³ówkowe dla kjsembed.

%package kmozilla
Summary:	Mozilla kpart
Summary(pl):	KPart mozilli
Group:		X11/Applications
Requires:	mozilla
Requires:	kdelibs >= 9:%{version}
Requires:	%{name}-xparts-kde = %{version}-%{release}

%description kmozilla
This KPart allows using mozilla as a browser engine.

%description kmozilla -l pl
Kpart umo¿liwiaj±cy u¿ywanie mozilli jako silnika przegl±darki
zamiast khtml.

#%package kde-objc
#Summary:	ObjC bindings for KDE
#Summary(pl):	Dowi±zania jêzyka ObjC dla KDE
#Group:		X11/Development/Libraries
#Requires:	%{name} = %{version}
#Requires:	libobjc
#Requires:	kdelibs >= 3.1

#%description kde-objc
#ObjC bindings for KDE.

#%description kde-objc -l pl
#Dowi±zania jêzyka ObjC dla KDE.

%package qt-c
Summary:	C bindings for qt
Summary(pl):	Dowi±zania jêzyka C dla qt
Group:		X11/Development/Libraries
Requires:	libgcc
Requires:	qt >= 3.1

%description qt-c
C bindings for qt.

%description qt-c -l pl
Dowi±zania jêzyka C dla qt.

%package qt-csharp
Summary:	C# bindings for qt
Summary(pl):	Dowi±zania jêzyka C# dla qt
Group:		X11/Development/Libraries
Requires:	mono-devel >= 0.16
Requires:	pnet >= 0.4.8
Requires:	qt >= 3.1

%description qt-csharp
C# bindings for qt.

%description qt-csharp -l pl
Dowi±zania jêzyka C# dla qt.

%package qt-java
Summary:	Java bindings for qt
Summary(pl):	Dowi±zania jêzyka Java dla qt
Group:		X11/Development/Libraries
Requires:	jdk
Requires:	qt >= 3.1

%description qt-java
Java bindings for qt.

%description qt-java -l pl
Dowi±zania jêzyka Java dla qt.

%package qt-java-devel
Summary:	qt-java header files
Summary(pl):	Pliki nag³ówkowe dla qt-java
Group:		X11/Development/Libraries
Requires:	%{name}-qt-java = %{version}
Requires:		qt-devel >= 3.1

%description qt-java-devel
qt-java header files.

%description qt-java-devel -l pl
Pliki nag³ówkowe dla qt-java.

#%package qt-objc
#Summary:	ObjC bindings for qt
#Summary(pl):	Dowi±zania jêzyka ObjC dla qt
#Group:		X11/Development/Libraries
#Requires:	libobjc
#Requires:	qt >= 3.1

#%description qt-objc
#ObjC bindings for qt.

#%description qt-objc -l pl
#Dowi±zania jêzyka ObjC dla qt.

%package smoke-qt
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries
Requires:	qt >= 3.1
Requires:	perl >= 5.6.1

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla qt.

%description smoke-qt -l pl
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla qt.

%package smoke-qt-devel
Summary:	smoke-qt header files
Summary(pl):	Pliki nag³ówkowe dla smoke-qt
Group:		X11/Development/Libraries
Requires:	%{name}-smoke-qt = %{version}-%{release}
Requires:	qt-devel >= 3.1
Requires:	perl-modules >= 5.6.1

%description smoke-qt-devel
smoke-qt header files.

%description smoke-qt-devel -l pl
Pliki nag³ówkowe dla smoke-qt.

%package xparts-gtk
Summary:	XParts technology for gtk
Summary(pl):	Technologia XParts dla gtk
Group:		X11/Development/Libraries
Requires:	%{name}-dcop-c = %{version}-%{release}

%description xparts-gtk
XParts technology: gtk embedding.

%description xparts-gtk -l pl
Technologia XParts: zagnie¿d¿anie gtk.

%package xparts-gtk-devel
Summary:	xparts-gtk header files
Summary(pl):	Pliki nag³ówkowe dla xparts-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-dcop-c-devel = %{version}-%{release}

%description xparts-gtk-devel
xparts-gtk header files.

%description xparts-gtk-devel -l pl
Pliki nag³ówkowe dla xparts-gtk.

%package xparts-interfaces
Summary:	Common libraries for XParts technology
Summary(pl):	Wspó³dzielone biblioteki dla technologii XParts
Group:		X11/Development/Libraries
Requires:	%{name}-xparts-kde = %{version}-%{release}

%description xparts-interfaces
Common libraries for XParts technology.

%description xparts-interfaces -l pl
Wspó³dzielone biblioteki dla technologii XParts.

%package  xparts-interfaces-devel
Summary:	xparts-interfaces header files
Summary(pl):	Pliki nag³ówkowe dla xparts-interfaces
Group:		X11/Development/Libraries
Requires:	%{name}-xparts-interfaces = %{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

%description xparts-interfaces-devel
xparts-interfaces header files.

%description xparts-interfaces-devel -l pl
Pliki nag³ówkowe dla xparts-interfaces.

%package xparts-kde
Summary:	XParts technology for KDE
Summary(pl):	Technologia XParts dla KDE
Group:		X11/Development/Libraries
Requires:	kdelibs >= 9:%{version}

%description xparts-kde
XParts technology: KDE embedding.

%description xparts-kde -l pl
Technologia XParts: osadzanie KDE.

%package xparts-notepad
Summary:	An example use of XParts technology: notepad
Summary(pl):	Przyk³adowe wykorzystanie technologii XParts: notatnik
Group:		X11/Development/Libraries
Requires:	%{name}-xparts-kde = %{version}-%{release}

%description xparts-notepad
An example use of XParts technology: notepad.

%description xparts-notepad -l pl
Przyk³adowe wykorzystanie technologii XParts: notatnik.

%prep
%setup -q
##%patch0 -p1
##%patch1 -p1
##%patch2 -p1
%patch3 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
#%%{__make} -f Makefile.cvs
export QTDIR=/usr
%configure  \
	--with-pythondir=/usr/lib/python2.1/site-packages \
	--with%{!?with_java:out}-java%{?with_java:=/usr/lib/java} \
	--%{?debug:en}%{!?debug:dis}able-debug

#%%{__make}
#{__make} -C dcopjava
#{__make} -C dcoppython

# dcop perl bindings compilation
#cd dcopperl
#perl Makefile.PL <<EOF
#$QTDIR/include/qt
#$QTDIR/lib
#%%{_includedir}/kde
#%%{_libdir}
#EOF
#mkdir -p blib/bin
#%%{__make}
# This one should stay commented (takes too long)
#%%{__make} test
#cd ..

# kalyptus compilation
#cd kalyptus
#%%{__autoconf}
#%%configure
#%%{__make}
#cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	destdir=$RPM_BUILD_ROOT

# dcop perl bindings installation
#%%{__make} -C dcopperl install PREFIX="$RPM_BUILD_ROOT%{_prefix}"

# kalyptus instalation
#cd kalyptus
#%%{__make} install DESTDIR="$RPM_BUILD_ROOT"
#cd ..

#%%{__make} -C dcopjava install DESTDIR="$RPM_BUILD_ROOT"
#%%{__make} -C dcoppython install DESTDIR="$RPM_BUILD_ROOT"
rm -rf $RPM_BUILD_ROOT%{_bindir}/uicsharp
cd $RPM_BUILD_ROOT%{_bindir}
ln -sf uicsharp.exe uicsharp
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files dcop-c
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdcopc.so.1.0.0

%files dcop-c-devel
%defattr(644,root,root,755)
%{_includedir}/dcopc
%{_libdir}/libdcopc.la
%attr(755,root,root) %{_libdir}/libdcopc.so
%attr(755,root,root) %{_libdir}/libdcopc.so.1

#%if %{with java}
#%files dcop-java
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/dcopidl2java
#%%{_libdir}/libdcopc.la
#%attr(755,root,root) %{_libdir}/libjavadcop.so
#%%{_libdir}/java/org/kde/DCOP/*.class
#%endif

#%files dcop-perl
#%defattr(644,root,root,755)
#%%{_libdir}/perl5

#%files dcop-python
#%defattr(644,root,root,755)
#%%{_usr}/lib/

#%files kalyptus
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kalyptus
#%%{_datadir}/kalyptus

%files kde-c
%defattr(644,root,root,755)
%{_libdir}/*kdec.la
%attr(755,root,root) %{_libdir}/*kdec.so*

%if %{with java}
%files kde-java
%defattr(644,root,root,755)
%dir %{_libdir}/java/org/kde
%{_libdir}/java/org/kde/koala
%{_libdir}/java/koala.jar
%{_libdir}/*kdejava.la
%attr(755,root,root) %{_libdir}/*kdejava.so.1.0.0

%files kde-java-devel
%defattr(644,root,root,755)
%{_includedir}/kdejava
%attr(755,root,root) %{_libdir}/*kdejava.so
%attr(755,root,root) %{_libdir}/*kdejava.so.1
%endif

%files kjsembed
%defattr(644,root,root,755)
%{_libdir}/*kjsembed.la
%attr(755,root,root) %{_libdir}/*kjsembed.so.1.0.0

%files kjsembed-devel
%defattr(644,root,root,755)
%{_includedir}/kjsembed
%attr(755,root,root) %{_libdir}/*kjsembed.so
%attr(755,root,root) %{_libdir}/*kjsembed.so.1

%ifnarch ia64
%files kmozilla
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmozilla
%{_libdir}/libkmozillapart.la
%attr(755,root,root) %{_libdir}/libkmozillapart.so*
%{_datadir}/services/kmozilla.desktop
%endif

%files qt-c
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clib
%{_libdir}/*qtc.la
%attr(755,root,root) %{_libdir}/*qtc.so*

%files qt-csharp
%defattr(644,root,root,755)
%doc qtsharp/src/examples/samples/*.cs qtsharp/src/examples/tutorials/*.cs
%attr(755,root,root) %{_bindir}/*uicsharp*
%{_libdir}/*qtsharp.la
%attr(755,root,root) %{_libdir}/Qt.dll
%attr(755,root,root) %{_libdir}/*qtsharp.so*
# ???
#%%{_datadir}/doc/

%if %{with java}
%files qt-java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/javalib
# ???
#%%{_prefix}/doc/javalib
%doc qtjava/javalib/docs/en/*
%{_libdir}/*qtjava.la
%attr(755,root,root) %{_libdir}/*qtjava.so.1.*
%{_libdir}/java/org/kde/qt
%{_libdir}/java/qtjava.jar

%files qt-java-devel
%defattr(644,root,root,755)
%{_includedir}/qtjava
%attr(755,root,root) %{_libdir}/*qtjava.so
%attr(755,root,root) %{_libdir}/*qtjava.so.1
%endif

%files smoke-qt
%defattr(644,root,root,755)
%{_libdir}/*smokeqt.la
%attr(755,root,root) %{_libdir}/*smokeqt.so.1.0.0

%files smoke-qt-devel
%defattr(644,root,root,755)
%{_includedir}/smoke.h
%attr(755,root,root) %{_libdir}/*smokeqt.so
%attr(755,root,root) %{_libdir}/*smokeqt.so.1

%files xparts-gtk
%defattr(644,root,root,755)
%{_libdir}/*gtkxparts.la
%attr(755,root,root) %{_libdir}/*gtkxparts.so.0.0.0

%files xparts-gtk-devel
%defattr(644,root,root,755)
%{_includedir}/xkparts/gtk*.h
%attr(755,root,root) %{_libdir}/*gtkxparts.so
%attr(755,root,root) %{_libdir}/*gtkxparts.so.?

%files xparts-interfaces
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/shell_xparthost

%files xparts-interfaces-devel
%defattr(644,root,root,755)
%{_includedir}/xkparts/xpart*.h

%files xparts-kde
%defattr(644,root,root,755)
%{_libdir}/*kdexparts.la
%attr(755,root,root) %{_libdir}/*kdexparts.so*

%files xparts-notepad
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xp_notepad
%{_libdir}/*notepadpart.la
%attr(755,root,root) %{_libdir}/*notepadpart.so*
%{_datadir}/services/*notepad.desktop
