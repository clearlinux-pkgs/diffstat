#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x702353E0F7E48EDB (dickey@invisible-island.net)
#
Name     : diffstat
Version  : 1.62
Release  : 8
URL      : https://invisible-mirror.net/archives/diffstat/diffstat-1.62.tgz
Source0  : https://invisible-mirror.net/archives/diffstat/diffstat-1.62.tgz
Source99 : https://invisible-mirror.net/archives/diffstat/diffstat-1.62.tgz.asc
Summary  : diffstat - make histogram from diff-output
Group    : Development/Tools
License  : HPND ICU MIT
Requires: diffstat-bin = %{version}-%{release}
Requires: diffstat-license = %{version}-%{release}
Requires: diffstat-man = %{version}-%{release}
BuildRequires : cppcheck
BuildRequires : groff

%description
Diffstat is is useful for reviewing large, complex patch files.  It reads from
one or more input files which contain output from diff, producing a histogram
of the total lines changed for each file referenced.

%package bin
Summary: bin components for the diffstat package.
Group: Binaries
Requires: diffstat-license = %{version}-%{release}
Requires: diffstat-man = %{version}-%{release}

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
%setup -q -n diffstat-1.62

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542069344
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542069344
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/diffstat
cp COPYING %{buildroot}/usr/share/package-licenses/diffstat/COPYING
cp package/debian/copyright %{buildroot}/usr/share/package-licenses/diffstat/package_debian_copyright
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffstat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/diffstat/COPYING
/usr/share/package-licenses/diffstat/package_debian_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/diffstat.1
