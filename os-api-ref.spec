#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : os-api-ref
Version  : 2.1.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/a9/35/e8c15cec076cbff90262b22b446486950c5f57c0197a1d8697969a13a246/os-api-ref-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a9/35/e8c15cec076cbff90262b22b446486950c5f57c0197a1d8697969a13a246/os-api-ref-2.1.0.tar.gz
Summary  : Sphinx Extensions to support API reference sites in OpenStack
Group    : Development/Tools
License  : Apache-2.0
Requires: os-api-ref-license = %{version}-%{release}
Requires: os-api-ref-python = %{version}-%{release}
Requires: os-api-ref-python3 = %{version}-%{release}
Requires: PyYAML
Requires: Sphinx
Requires: openstackdocstheme
Requires: pbr
Requires: six
BuildRequires : PyYAML
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : openstackdocstheme
BuildRequires : pbr
BuildRequires : six

%description
Team and repository tags
        ========================

%package license
Summary: license components for the os-api-ref package.
Group: Default

%description license
license components for the os-api-ref package.


%package python
Summary: python components for the os-api-ref package.
Group: Default
Requires: os-api-ref-python3 = %{version}-%{release}

%description python
python components for the os-api-ref package.


%package python3
Summary: python3 components for the os-api-ref package.
Group: Default
Requires: python3-core
Provides: pypi(os_api_ref)
Requires: pypi(openstackdocstheme)
Requires: pypi(pbr)
Requires: pypi(pyyaml)
Requires: pypi(six)
Requires: pypi(sphinx)

%description python3
python3 components for the os-api-ref package.


%prep
%setup -q -n os-api-ref-2.1.0
cd %{_builddir}/os-api-ref-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592585107
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-api-ref
cp %{_builddir}/os-api-ref-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/os-api-ref/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-api-ref/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
