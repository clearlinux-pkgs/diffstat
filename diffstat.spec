#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : diffstat
Version  : 1.63
Release  : 10
URL      : https://invisible-mirror.net/archives/diffstat/diffstat-1.63.tgz
Source0  : https://invisible-mirror.net/archives/diffstat/diffstat-1.63.tgz
Source1 : https://invisible-mirror.net/archives/diffstat/diffstat-1.63.tgz.asc
Summary  : diffstat - make histogram from diff-output
Group    : Development/Tools
License  : HPND ICU MIT
Requires: diffstat-bin = %{version}-%{release}
Requires: diffstat-license = %{version}-%{release}
Requires: diffstat-man = %{version}-%{release}
BuildRequires : cppcheck
BuildRequires : ctags
BuildRequires : groff

%description
Diffstat is is useful for reviewing large, complex patch files.  It reads from
one or more input files which contain output from diff, producing a histogram
of the total lines changed for each file referenced.

%package bin
Summary: bin components for the diffstat package.
Group: Binaries
Requires: diffstat-license = %{version}-%{release}

%description bin
bin components for the diffstat package.


%package license
Summary: license components for the diffstat package.
Group: Default

%description license
license components for the diffstat package.


%package man
Summary: man components for the diffstat package.
Group: Default

%description man
man components for the diffstat package.


%prep
%setup -q -n diffstat-1.63
cd %{_builddir}/diffstat-1.63

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575329293
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1575329293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/diffstat
cp %{_builddir}/diffstat-1.63/COPYING %{buildroot}/usr/share/package-licenses/diffstat/92d8347e8f891ad54727eb829efeb009804778ce
cp %{_builddir}/diffstat-1.63/package/debian/copyright %{buildroot}/usr/share/package-licenses/diffstat/98852db66a19300e840d8a1c78e50e85ffebc3fa
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffstat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/diffstat/92d8347e8f891ad54727eb829efeb009804778ce
/usr/share/package-licenses/diffstat/98852db66a19300e840d8a1c78e50e85ffebc3fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/diffstat.1
