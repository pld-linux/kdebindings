%define is_release 1
%define beta %{nil}
%define rel 3
%define DATE 20010805
Version: 2.2
Name: kdebindings
%if %{is_release}
%if "%{beta}" != ""
Release: 1.%{beta}.%{rel}
Source: %{name}-%{version}-%{beta}.tar.bz2
%else
Release: %{rel}
Source: %{name}-%{version}.tar.bz2
%endif
%else
Release: 1.cvs%{DATE}.%{rel}
Source: %{name}-%{DATE}.tar.bz2
%endif
Summary: KDE bindings to non-C++ languages.
URL: http://www.kde.org/
License: GPL
Group: User Interface/Desktops
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: python2 >= 2.1 zlib-devel kdelibs-devel kdelibs-sound-devel python2-devel >= 2.1 libjpeg-devel libpng-devel fam-devel
Requires: kdelibs >= 2.2 kdebase >= 2.2
%ifnarch ia64
# Remove the "#" when the build system has finally run out of crack
# BuildRequires: mozilla-devel
%endif

%description
KDE/DCOP bindings to non-C++ languages.


%package devel
Summary: Development files for kdebindings.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the KDE bindings.

Install kdebindings-devel if you want to develop non-KDE applications
that talk to KDE.

%package kmozilla
Summary: KDE bindings to Mozilla.
Group: User Interface/Desktops
Requires: mozilla kdebase >= 2.2

%description kmozilla
KDE bindings to Mozilla.


%package perl
Summary: Perl bindings to DCOP.
Group: Development/Libraries
Requires: kdelibs >= %{version}, perl >= 5.6.0

%description perl
Perl bindings to the DCOP interprocess communication protocol used by
KDE.

%package python
Summary: Python bindings to DCOP.
Group: Development/Libraries
Requires: kdelibs >= %{version}, python2 >= 2.1

%description python
Python bindings to the DCOP interprocess communication protocol used by KDE.


%prep
%if %{is_release}
%setup -q
%else
%setup -q -n %{name}
%endif
make -f Makefile.cvs
unset QTDIR || :
. /etc/profile.d/qt.sh
./configure --prefix=%{prefix} --mandir=%{_mandir} --without-java --with-pythondir=/usr/lib/python2.1/site-packages

%build
unset QTDIR || :
. /etc/profile.d/qt.sh
# UGLY workaround for python bug...
cat >fPIC <<EOF
#!/bin/sh
exec gcc -fPIC \$@
EOF
chmod +x fPIC
export PATH="$PATH:`pwd`"
# end workaround

make %{?smp_mflags}
make %{?smp_mflags} -C dcoppython
cd dcopperl
perl Makefile.PL <<EOF
$QTDIR/include
$QTDIR/lib
%{_prefix}/include/kde
%{_libdir}
EOF
mkdir -p blib/bin
make %{?smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages
make install DESTDIR="$RPM_BUILD_ROOT"
make -C dcoppython install DESTDIR="$RPM_BUILD_ROOT"
make -C dcopperl install PREFIX="$RPM_BUILD_ROOT%{_prefix}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/lib/libdcopc.so.*
/usr/lib/lib*xparts.so.*

%files python
%defattr(-,root,root)
/usr/lib/python2.1/*/*

%files devel
%defattr(-,root,root)
/usr/lib/libdcopc.??
/usr/lib/lib*xparts.??
%dir /usr/include/xkparts
%dir /usr/include/dcopc
/usr/include/xkparts/*
/usr/include/dcopc/*

%ifnarch ia64
%files kmozilla
%defattr(-,root,root)
/usr/bin/kmozilla
/usr/lib/*mozilla*
/usr/share/services/kmozilla.desktop
%endif

%files perl
%defattr(-,root,root)
%{prefix}/lib/perl5/site_perl/*/*/auto/DCOP/*
%{prefix}/lib/perl5/site_perl/*/*/auto/DCOP/.packlist
%{prefix}/lib/perl5/site_perl/*/*/DCOP.pm
%{prefix}/lib/perl5/site_perl/*/*/DCOP/Object.pm
%{_mandir}/man3/DCOP.3pm*

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Thu Aug  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-2
- Make sure %{name}-kmozilla isn't built on ia64

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010723.2
- Move python bindings to separate package
- Add perl bindings
- Shut up rpmlint

* Wed Feb 21 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.1

* Sun Jan 28 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- initial RPM
