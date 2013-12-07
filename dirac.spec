%define major	0
%define libdec	%mklibname %{name}_decoder %{major}
%define libenc	%mklibname %{name}_encoder %{major}
%define devname %mklibname -d %{name}

Summary:	Video Codec based on Wavelets
Name:		dirac
Version:	1.0.2
Release:	9
License:	MPLv1.1
Group:		Video
Url:		http://sf.net/projects/dirac
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		dirac-0.7.0-werror.patch
Patch1:		dirac-1.0.2-backports.patch

BuildRequires:	doxygen
BuildRequires:	tetex-dvipdfm
BuildRequires:	tetex-latex
BuildRequires:	pkgconfig(cppunit)

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

%package -n %{libdec}
Summary:	Shared library of the Dirac Video codec
Group:		System/Libraries
Obsoletes:	%{_lib}dirac0 < 1.0.2-7

%description -n %{libdec}
This package contains the shared library for %{name}.

%package -n %{libenc}
Summary:	Shared library of the Dirac Video codec
Group:		System/Libraries
Conflicts:	%{_lib}dirac0 < 1.0.2-7

%description -n %{libenc}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files of the Dirac Video codec
Group:		Development/C++
Requires:	%{libdec} = %{version}
Requires:	%{libenc} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}dirac-static-devel < 1.0.2-7

%description -n %{devname}
This package contains the development files for %{name}.

%package	utils
Summary:	Example encoder and decoder for the Dirac video codec
Group:		Video

%description	utils
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
%apply_patches

%build
./bootstrap
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std
mv %{buildroot}%{_datadir}/doc installed-docs
#gw don't package unit tests
rm -fv %{buildroot}%{_bindir}/dirac_unittest

%files utils
%doc README TODO AUTHORS
%{_bindir}/dirac*
%{_bindir}/BMPtoRGB
%{_bindir}/RGB*
%{_bindir}/UYVYtoRGB
%{_bindir}/UYVYtoYUV422
%{_bindir}/YUV*
%{_bindir}/create_dirac_testfile.pl

%files -n %{libdec}
%{_libdir}/libdirac_decoder.so.%{major}*

%files -n %{libenc}
%{_libdir}/libdirac_encoder.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libdirac*.so
%doc installed-docs/*
%{_libdir}/pkgconfig/dirac.pc

