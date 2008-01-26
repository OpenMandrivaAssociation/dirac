%define name dirac
%define version 0.9.1
%define release %mkrel 1
%define major 0.1
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary: Video Codec based on Wavelets
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/%name/%{name}-%{version}.tar.gz
Patch: dirac-0.7.0-werror.patch
License: MPL/GPL/LGPL
Group: Video
Url: http://sf.net/projects/dirac
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: doxygen
BuildRequires: tetex-dvipdfm tetex-latex
BuildRequires: libcppunit-devel

%description
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n %libname
Group: System/Libraries
Summary: Shared library of the Dirac Video codec

%description -n %libname
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n %develname
Group: Development/C++
Summary: Development files of the Dirac Video codec
Requires: %libname = %version
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel %mklibname -d %name 0.1

%description -n %develname
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package -n %staticname
Group: Development/C++
Summary: Static libraries of the Dirac Video codec
Requires: %develname = %version
Provides: lib%name-static-devel = %version-%release

%description -n %staticname
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.

%package utils
Group: Video
Summary: Example encoder and decoder for the Dirac video codec

%description utils
Dirac is an open source video codec. It uses a traditional hybrid
video codec architecture, but with the wavelet transform instead of
the usual block transforms.  Motion compensation uses overlapped
blocks to reduce block artefacts that would upset the transform coding
stage.

Dirac can code just about any size of video, from streaming up to HD
and beyond, although certain presets are defined for different
applications and standards.  These cover the parameters that need to
be set for the encoder to work, such as block sizes and temporal
prediction structures, which must otherwise be set by hand.


%prep
%setup -q
%patch -p1
autoconf

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc installed-docs
#gw don't package unit tests
rm -fv %buildroot%_bindir/dirac_unittest

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files utils
%defattr(-,root,root)
%doc README TODO AUTHORS
%_bindir/dirac*
%_bindir/BMPtoRGB
%_bindir/RGB*
%_bindir/UYVYtoRGB
%_bindir/YUV*
%_bindir/create_dirac_testfile.pl

%files -n %libname
%defattr(-,root,root)
%_libdir/libdirac*.so.0*

%files -n %develname
%defattr(-,root,root)
%_includedir/%{name}
%_libdir/libdirac*.so
%doc installed-docs/*
%_libdir/pkgconfig/dirac.pc

%files -n %staticname
%defattr(-,root,root)
%attr(644,root,root)%_libdir/libdirac*.*a
