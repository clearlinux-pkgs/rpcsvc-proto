#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpcsvc-proto
Version  : 1.4.2
Release  : 1
URL      : https://github.com/thkukuk/rpcsvc-proto/releases/download/v1.4.2/rpcsvc-proto-1.4.2.tar.xz
Source0  : https://github.com/thkukuk/rpcsvc-proto/releases/download/v1.4.2/rpcsvc-proto-1.4.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rpcsvc-proto-bin = %{version}-%{release}
Requires: rpcsvc-proto-license = %{version}-%{release}
Requires: rpcsvc-proto-man = %{version}-%{release}

%description
This package contains rpcsvc proto.x files from glibc, which are
missing in libtirpc. Additional it contains rpcgen, which is needed
to create header files and sources from protocol files.
This package is only needed, if glibc is installed without the
deprecated sunrpc functionality and libtirpc should replace it.

%package bin
Summary: bin components for the rpcsvc-proto package.
Group: Binaries
Requires: rpcsvc-proto-license = %{version}-%{release}

%description bin
bin components for the rpcsvc-proto package.


%package dev
Summary: dev components for the rpcsvc-proto package.
Group: Development
Requires: rpcsvc-proto-bin = %{version}-%{release}
Provides: rpcsvc-proto-devel = %{version}-%{release}
Requires: rpcsvc-proto = %{version}-%{release}

%description dev
dev components for the rpcsvc-proto package.


%package license
Summary: license components for the rpcsvc-proto package.
Group: Default

%description license
license components for the rpcsvc-proto package.


%package man
Summary: man components for the rpcsvc-proto package.
Group: Default

%description man
man components for the rpcsvc-proto package.


%prep
%setup -q -n rpcsvc-proto-1.4.2
cd %{_builddir}/rpcsvc-proto-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606231456
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1606231456
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rpcsvc-proto
cp %{_builddir}/rpcsvc-proto-1.4.2/COPYING %{buildroot}/usr/share/package-licenses/rpcsvc-proto/a3baa18584850f7bb17db5740736189b382de31f
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rpcgen

%files dev
%defattr(-,root,root,-)
/usr/include/rpcsvc/bootparam_prot.h
/usr/include/rpcsvc/bootparam_prot.x
/usr/include/rpcsvc/key_prot.h
/usr/include/rpcsvc/key_prot.x
/usr/include/rpcsvc/klm_prot.h
/usr/include/rpcsvc/klm_prot.x
/usr/include/rpcsvc/mount.h
/usr/include/rpcsvc/mount.x
/usr/include/rpcsvc/nfs_prot.h
/usr/include/rpcsvc/nfs_prot.x
/usr/include/rpcsvc/nlm_prot.h
/usr/include/rpcsvc/nlm_prot.x
/usr/include/rpcsvc/rex.h
/usr/include/rpcsvc/rex.x
/usr/include/rpcsvc/rquota.h
/usr/include/rpcsvc/rquota.x
/usr/include/rpcsvc/rstat.h
/usr/include/rpcsvc/rstat.x
/usr/include/rpcsvc/rusers.h
/usr/include/rpcsvc/rusers.x
/usr/include/rpcsvc/sm_inter.h
/usr/include/rpcsvc/sm_inter.x
/usr/include/rpcsvc/spray.h
/usr/include/rpcsvc/spray.x

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rpcsvc-proto/a3baa18584850f7bb17db5740736189b382de31f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rpcgen.1
