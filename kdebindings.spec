#
# Conditional build:
%bcond_with java # enable java

%define		_state	stable
%define		_ver	3.3.0

Summary:	KDE bindings to non-C++ languages
Summary(pl):	Dowi±zania KDE dla jêzyków innych ni¿ C++
Summary(pt_BR):	Bindings para KDE
Name:		kdebindings
Version:	%{_ver}
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/3.3/src/%{name}-%{version}.tar.bz2
# Source0-md5:	63f7cd3ae52397c2182527899efb4c80
Patch100:	%{name}-branch.diff
Patch0:		%{name}-ac.patch
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	fam-devel
#BuildRequires:	gcc-objc
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
%{?with_java:BuildRequires:	jdk}
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
#BuildRequires:	mono-devel >= 0.16
#BuildRequires:	pnet >= 0.4.8
BuildRequires:	perl-modules >= 1:5.8.0
BuildRequires:	python-devel >= 2.1
BuildRequires:	ruby-devel
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
Bindings para o K Desktop Environment: Provê interfaces para
diferentes linguagens de programação para uso da interface nativa do
KDE.

%package kalyptus
Summary:	Qt/KDE bindings generator
Summary(pl):	Generator dowi±zañ do Qt/KDE
Group:		X11/Development/Libraries
Requires:	perl >= 5.6.1
Requires:	kdelibs >= 9:%{version}
Requires:	qt >= 6:3.3.3

%description kalyptus
Kalyptus creates language bindings for Qt and KDE C++ libraries
directly from the headers.

%description kalyptus -l pl
Kalyptus s³u¿y do generowania dowi±zañ do Qt/KDE bezpo¶rednio z plików
nag³ówkowych.

# c bindings
%package c-dcop
Summary:	C bindings for DCOP
Summary(pl):	Dowi±zania w jêzyku C dla DCOP
Group:		X11/Development/Libraries
Requires:	libgcc
Requires:	kdelibs >= 9:%{version}
Requires:	gtk+ >= 1.2.6
Obsoletes:	kdebindings-dcop-c

%description c-dcop
C bindings for the Desktop COmmunications Protocol used by KDE
applications to share information and communicate between each other.

%description c-dcop -l pl
Dowi±zania jêzyka C do Desktop COmmunications Protocol (DCOP)
u¿ywanego przez aplikacje KDE to wymiany informacji i komunikowania
siê miêdzy sob±.

%package c-dcop-devel
Summary:	C bindings for DCOP [development files]
Summary(pl):	Dowi±zania w jêzyku C dla DCOP [nag³ówki]
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	gtk+-devel >= 1.2.6
Requires:	%{name}-c-dcop = %{version}-%{release}
Obsoletes:	kdebindings-dcop-c-devel

%description c-dcop-devel
c-dcop header files.

%description c-dcop-devel -l pl
Pliki nag³ówkowe dla c-dcop.

# java bindings
%package	java-dcop
Summary:	Java bindings for DCOP
Summary(pl):	Dowi±zania jêzyka Java dla DCOP
Group:		X11/Development/Libraries
Requires:	jdk
Requires:	kdelibs >= 9:%{version}
Requires:	qt >= 6:3.3.3
Requires:	libart_lgpl
Obsoletes:	kdebindings-dcop-java

%description java-dcop
Java bindings for the Desktop COmmunications Protocol used by KDE
applications to share information and communicate between each other.

%description java-dcop -l pl
Dowi±zania jêzyka Java do Desktop COmmunications Protocol (DCOP)
u¿ywanego przez aplikacje KDE to wymiany informacji i komunikowania
siê miêdzy sob±.

%package java-qt
Summary:	Java bindings for qt
Summary(pl):	Dowi±zania jêzyka Java dla qt
Group:		X11/Development/Libraries
Requires:	jdk
Requires:	qt >= 6:3.3.3
Obsoletes:	kdebindings-qt-java

%description java-qt
Java bindings for qt.

%description java-qt -l pl
Dowi±zania jêzyka Java dla qt.

%package java-kde
Summary:	Java bindings for KDE
Summary(pl):	Dowi±zania jêzyka Java dla KDE
Group:		X11/Development/Libraries
Requires:	jdk
Requires:	%{name}-qt-java = %{version}-%{release}
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdebindings-kde-java

%description java-kde
Java bindings for KDE.

%description java-kde -l pl
Dowi±zania jêzyka Java dla KDE.

# javascript scripting for KDE applications

%package kjsembed
Summary:	A library for embedding the KJS JavaScript interpreter
Summary(pl):	Biblioteka pozwalaj±ca na zagnie¿d¿anie interpretera KJS
Group:		X11/Development/Libraries
Requires:	kdelibs >= 9:%{version}

%description kjsembed
A library for embedding the KJS JavaScript interpreter in application.

%description kjsembed -l pl
Biblioteka pozwalaj±ca na zagnie¿d¿anie interpretera JavaScript - KJS,
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

# mozilla kpart - not working

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
Kpart umo¿liwiaj±cy u¿ywanie mozilli jako silnika przegl±darki zamiast
khtml.

# perl bindings

%package perl-dcop
Summary:	Perl bindings for DCOP
Summary(pl):	Dowi±zania jêzyka Perl dla DCOP
Group:		X11/Development/Libraries
Requires:	perl-modules >= 5.6.1
Requires:	kdelibs >= 9:%{version}
Requires:	qt >= 6:3.3.3
Obsoletes:	kdebindings-dcop-perl

%description perl-dcop
Perl bindings for the Desktop COmmunications Protocol used by KDE
applications to share information and communicate between each other.

%description perl-dcop -l pl
Dowi±zania jêzyka Perl do Desktop COmmunications Protocol (DCOP)
u¿ywanego przez aplikacje KDE to wymiany informacji i komunikowania
siê miêdzy sob±.

# python bindings, only dcop as qt and kde ones are in py{Qt,KDE}.spec
%package python-dcop
Summary:	Python bindings for DCOP
Summary(pl):	Dowi±zania jêzyka Python dla DCOP
Group:		X11/Development/Libraries
Requires:	python-devel >= 2.1
Requires:	kdelibs >= 9:%{version}
Requires:	qt >= 6:3.3.3
Obsoletes:	kdebindings-dcop-python

%description python-dcop
Python bindings for the Desktop COmmunications Protocol used by KDE
applications to share information and communicate between each other.

%description python-dcop -l pl
Dowi±zania jêzyka Python do Desktop COmmunications Protocol (DCOP)
u¿ywanego przez aplikacje KDE to wymiany informacji i komunikowania
siê miêdzy sob±.

%package ruby-qt
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries
Requires:	qt >= 6:3.3.3
Requires:	ruby
Requires:	%{name}-smoke-qt = %{version}-%{release}

%description ruby-qt
A Qt bindings for Ruby using the SMOKE technology.

%description ruby-qt -l pl
Dowi±zania Qt dla Ruby przy u¿yciu technologii SMOKE.

%package ruby-kde
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries
Requires:	qt >= 6:3.3.3
Requires:	kdelibs >= 9:%{version}
Requires:	%{name}-ruby-qt = %{version}-%{release}
Requires:	%{name}-smoke-kde = %{version}-%{release}

%description ruby-kde
A KDE bindings for Ruby using the SMOKE technology.

%description ruby-kde -l pl
Dowi±zania KDE dla Ruby przy u¿yciu technologii SMOKE.

%package smoke-qt
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries
Requires:	qt >= 6:3.3.3

%description smoke-qt
SMOKE library (Scripting Meta Object Kompiler Engine) dla qt.

%description smoke-qt -l pl
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla qt.

%package smoke-qt-devel
Summary:	smoke-qt header files
Summary(pl):	Pliki nag³ówkowe dla smoke-qt
Group:		X11/Development/Libraries
Requires:	%{name}-smoke-qt = %{version}-%{release}
Requires:	qt-devel >= 6:3.3.3

%description smoke-qt-devel
smoke-qt header files.

%description smoke-qt-devel -l pl
Pliki nag³ówkowe dla smoke-qt.

%package smoke-kde
Summary:	A SMOKE library for qt
Summary(pl):	Biblioteka SMOKE dla qt
Group:		X11/Development/Libraries
Requires:	%{name}-smoke-qt = %{version}-%{release}
Requires:	kdelibs >= 9:%{version}

%description smoke-kde
SMOKE library (Scripting Meta Object Kompiler Engine) dla KDE.

%description smoke-kde -l pl
Biblioteka SMOKE (Silnik kompilatora metaobiektów skryptowych) dla
KDE.

%package smoke-kde-devel
Summary:	smoke-qt header files
Summary(pl):	Pliki nag³ówkowe dla smoke-qt
Group:		X11/Development/Libraries
Requires:	%{name}-smoke-qt-devel = %{version}-%{release}
Requires:	%{name}-smoke-kde = %{version}-%{release}
Requires:	kdelibs-devel >= 9:%{version}

%description smoke-kde-devel
smoke-kde header files.

%description smoke-kde-devel -l pl
Pliki nag³ówkowe dla smoke-kde.

# xparts, don't work (dcopc doesn't work)

%package xparts-gtk
Summary:	XParts technology for gtk
Summary(pl):	Technologia XParts dla gtk
Group:		X11/Development/Libraries
Requires:	%{name}-c-dcop = %{version}-%{release}

%description xparts-gtk
XParts technology: gtk embedding.

%description xparts-gtk -l pl
Technologia XParts: zagnie¿d¿anie gtk.

%package xparts-gtk-devel
Summary:	xparts-gtk header files
Summary(pl):	Pliki nag³ówkowe dla xparts-gtk
Group:		X11/Development/Libraries
Requires:	%{name}-c-dcop-devel = %{version}-%{release}

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
%patch100 -p1
%patch0 -p1 -b .niedakh
##%patch2 -p1

%build

# dont build pyQt and pyKDE since we build it from a separate spec
echo "DO_NOT_COMPILE=\"\$DO_NOT_COMPILE python\"" > python/configure.in.in

cp %{_datadir}/automake/config.sub admin
#export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure  \
	--with%{!?with_java:out}-java%{?with_java:=%{_libdir}/java} \
	--%{?debug:en}%{!?debug:dis}able-debug \
	--with-extra-includes=%{py_incdir} \
	--with-pythondir=%{py_libdir} \
	--with-qt-libraries=%{_libdir}

%{__make}

cd kalyptus
%{__autoconf}
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	destdir=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%{__make} -C kalyptus install \
	DESTDIR=$RPM_BUILD_ROOT \
	destdir=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} 

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pcop.la \
	$RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/1.8/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	kjsembed -p /sbin/ldconfig
%postun	kjsembed -p /sbin/ldconfig

%post	smoke-qt -p /sbin/ldconfig
%postun	smoke-qt -p /sbin/ldconfig

%post	smoke-kde -p /sbin/ldconfig
%postun	smoke-kde -p /sbin/ldconfig

%post	java-qt -p /sbin/ldconfig
%postun	java-qt -p /sbin/ldconfig

# Javascript scripting for KDE applications

%files kjsembed
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsaccess
%attr(755,root,root) %{_bindir}/kjscmd
%attr(755,root,root) %{_libdir}/*kjsembed.so.1.0.0
%{_libdir}/kde3/libcustomobjectplugin.la
%attr(755,root,root) %{_libdir}/kde3/libcustomobjectplugin.so
%{_libdir}/kde3/libcustomqobjectplugin.la
%attr(755,root,root) %{_libdir}/kde3/libcustomqobjectplugin.so
%{_libdir}/kde3/libimagefxplugin.la
%attr(755,root,root) %{_libdir}/kde3/libimagefxplugin.so
%{_libdir}/kde3/libjsconsoleplugin.la
%attr(755,root,root) %{_libdir}/kde3/libjsconsoleplugin.so
%{_libdir}/kde3/libqprocessplugin.la
%attr(755,root,root) %{_libdir}/kde3/libqprocessplugin.so
%{_desktopdir}/kde/kjscmd.desktop
%dir %{_datadir}/apps/kjsembed
%{_datadir}/apps/kjsembed/cmdline.js
%{_datadir}/services/customobject_plugin.desktop
%{_datadir}/services/customqobject_plugin.desktop
%{_datadir}/services/imagefx_plugin.desktop
%{_datadir}/services/qprocess_plugin.desktop
%{_datadir}/servicetypes/binding_type.desktop
%{_mandir}/man1/kjscmd.1*

%files kjsembed-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*kjsembed.so
%{_libdir}/*kjsembed.la
%{_includedir}/kjsembed

# python bindings for dcop, others wont be built

%files python-dcop
%defattr(644,root,root,755)
%{py_libdir}/pydcop.py
%attr(755,root,root) %{py_libdir}/site-packages/pcop.so

# C bindings for qt and kde using the smoke technology

%files smoke-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*smokeqt.so.1.2.2

%files smoke-qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*smokeqt.so
%{_libdir}/*smokeqt.la
%{_includedir}/smoke.h

%files smoke-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*smokekde.so.1.2.2

%files smoke-kde-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*smokekde.so
%{_libdir}/*smokekde.la
%{_includedir}/smoke.h

# ruby bindings

%files ruby-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtrubyinit
%attr(755,root,root) %{_bindir}/rbqtapi
%attr(755,root,root) %{_bindir}/rbqtsh
%attr(755,root,root) %{_bindir}/rbuic
%{_libdir}/ruby/site_ruby/1.8/Qt.rb
%{_libdir}/ruby/site_ruby/1.8/Qt/qtruby.rb
%attr(755,root,root) %{_libdir}/ruby/site_ruby/1.8/*/qtruby.so.0.0.0

%files ruby-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krubyinit
%{_libdir}/ruby/site_ruby/1.8/KDE/korundum.rb
%{_libdir}/ruby/site_ruby/1.8/Korundum.rb
%attr(755,root,root) %{_libdir}/ruby/site_ruby/1.8/*/korundum.so.0.0.0

# java bindings

%if %{with java}

#%files java-dcop
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/dcopidl2java
#%%{_libdir}/libdcopc.la
#%attr(755,root,root) %{_libdir}/libjavadcop.so
#%%{_libdir}/java/org/kde/DCOP/*.class

%files java-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/javalib
# DONT package it, using %doc on those files instead
#%{_prefix}/doc/javalib
%attr(755,root,root) %{_libdir}/*qtjava*.so.1.0.0
%attr(755,root,root) %{_libdir}/*qtjava*.so
%{_libdir}/*qtjava*.la
%{_libdir}/java/qtjava.jar
%doc qtjava/javalib/docs/en/*.html
%doc qtjava/javalib/docs/en/*.sgml

%files java-kde
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/koala
%attr(755,root,root) %{_libdir}/*kdejava.so.1.0.0
%attr(755,root,root) %{_libdir}/*kdejava.so
%{_libdir}/*kdejava.la
%{_libdir}/java/koala.jar
%endif

# perl bindings
%files perl-dcop
%defattr(644,root,root,755)
%{perl_vendorarch}/DCOP.pm
%dir %{perl_vendorarch}/DCOP
%{perl_vendorarch}/DCOP/Object.pm
%dir %{perl_vendorarch}/auto/DCOP
%{perl_vendorarch}/auto/DCOP/DCOP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DCOP/DCOP.so
%{_mandir}/man3/DCOP.3pm*

# C bindings

#files c-dcop
#defattr(644,root,root,755)
#attr(755,root,root) %{_libdir}/libdcopc.so.1.0.0

#files c-dcop-devel
#defattr(644,root,root,755)
#{_includedir}/dcopc
#{_libdir}/libdcopc.la
#attr(755,root,root) %{_libdir}/libdcopc.so

# kalyptus
%files kalyptus
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalyptus
%{_datadir}/kalyptus

# mozilla embedding
#%ifnarch ia64
#%files kmozilla
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmozilla
#%{_libdir}/libkmozillapart.la
#%attr(755,root,root) %{_libdir}/libkmozillapart.so*
#%{_datadir}/services/kmozilla.desktop
#%endif

# xparts

##%files xparts-gtk
##%defattr(644,root,root,755)
##%{_libdir}/*gtkxparts.la
##%attr(755,root,root) %{_libdir}/*gtkxparts.so.0.0.0

##%files xparts-gtk-devel
##%defattr(644,root,root,755)
##%{_includedir}/xkparts/gtk*.h
##%attr(755,root,root) %{_libdir}/*gtkxparts.so

##%files xparts-interfaces
##%defattr(644,root,root,755)
##%attr(755,root,root) %{_bindir}/shell_xparthost

##%files xparts-interfaces-devel
##%defattr(644,root,root,755)
##%{_includedir}/xkparts/xpart*.h

##%files xparts-kde
##%defattr(644,root,root,755)
##%{_libdir}/*kdexparts.la
##%attr(755,root,root) %{_libdir}/*kdexparts.so*

##%files xparts-notepad
##%defattr(644,root,root,755)
##%attr(755,root,root) %{_bindir}/xp_notepad
##%{_libdir}/*notepadpart.la
##%attr(755,root,root) %{_libdir}/*notepadpart.so*
#%{_datadir}/services/*notepad.desktop
