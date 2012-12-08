%define name dirac
%define version 1.0.2
%define release %mkrel 6
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary: Video Codec based on Wavelets
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/%name/%{name}-%{version}.tar.gz
Patch: dirac-0.7.0-werror.patch
Patch1: dirac-1.0.2-backports.patch
License: MPLv1.1
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
Obsoletes: %{_lib}dirac0.1 < 1.0.2-4

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
%patch1 -p0

%build
./bootstrap
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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files utils
%defattr(-,root,root)
%doc README TODO AUTHORS
%_bindir/dirac*
%_bindir/BMPtoRGB
%_bindir/RGB*
%_bindir/UYVYtoRGB
%_bindir/UYVYtoYUV422
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2011.0
+ Revision: 663779
- mass rebuild

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 1.0.2-4mdv2011.0
+ Revision: 623254
- add fedora patch to make it build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2010.1
+ Revision: 522454
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2010.0
+ Revision: 413357
- rebuild

* Thu Feb 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-1mdv2009.1
+ Revision: 339734
- update to new version 1.0.2

* Thu Sep 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 285608
- new version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.10.0-2mdv2009.0
+ Revision: 266562
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jun 07 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.10.0-1mdv2009.0
+ Revision: 216675
- new version
- update file list

* Sat Jan 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-1mdv2008.1
+ Revision: 158369
- new version
- split out static libraries

* Wed Jan 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 156995
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 95563
- new version
- new devel name

* Fri May 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.0-1mdv2008.0
+ Revision: 26231
- Import dirac



* Fri May 11 2007 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2008.0
- disable -Werror to make it build
- New version 0.7.0

* Tue Jun 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.6.0-1mdv2007.0
- New release 0.6.0

* Fri Feb 10 2006 Götz Waschk <waschk@mandriva.org> 0.5.4-2mdk
- enable cppunit tests

* Mon Dec 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.4-1mdk
- New release 0.5.4

* Wed Aug 24 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.3-1mdk
- New release 0.5.3

* Wed May 25 2005 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdk
- update file list
- New release 0.5.2

* Sat Feb 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-1mdk
- update file list
- New release 0.5.1

* Thu Dec  2 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5.0-2mdk
- merge libname-devel and dirac-devel packages

* Thu Dec 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5.0-1mdk
- 0.5.5

* Wed Sep 22 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.4.3-1mdk
- New release 0.4.3

* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.2-1mdk
- 0.4.2

* Thu Aug 26 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.4.1-1mdk
- New release 0.4.1

* Wed Aug 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.0-1mdk
- drop patches
- New release 0.4.0

* Fri Jun 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-3mdk
- fix buildrequires

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-2mdk
- drop xparam dependancy
- fix pkgconfig installation
- fix header location

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.1-1mdk
- manually install pkgconfig file
- fix pkgconfig file
- New release 0.3.1

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3.0-1mdk
- initial package
