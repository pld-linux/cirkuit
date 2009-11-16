Summary:	Cirkuit is a KDE4 GUI for the Circuit macros
Summary(hu.UTF-8):	Cirkuit egy KDE4 felület a Circuit makrókhoz
Name:		cirkuit
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://wwwu.uni-klu.ac.at/magostin/src/%{name}-%{version}.tar.gz
# Source0-md5:	17190f98f03f73c2527026bdbd065552
%define	builddir build
URL:		http://wwwu.uni-klu.ac.at/magostin/cirkuit.html
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	shared-mime-info >= 0.70
Requires:	ghostscript
Requires:	kde4-icons-oxygen
Requires:	m4
Requires:	texlive-dvips
Requires:	texlive-latex
Requires:	texlive-pdftex
Requires:	texlive-psutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cirkuit is a KDE4 GUI for the Circuit macros by Dwight Aplevich, which
is a set of macros for drawing high-quality line diagrams to include
in TeX, LaTeX, or similar documents. Cirkuit builds a live preview of
the source code and can export the resulting images in EPS, PDF, PNG
or PSTricks format.

%description -l hu.UTF-8
Cirkuit egy KDE4 felület (GUI) a Dwight Aplevich-féle circuit
makrókhoz, amely egy makrógyűjtemény nyomdai minőségű vonaldiagramok
rajzolásához, amelyet TeX, LaTeX vagy hasonló dokumentumokba
illeszthetsz. Cirkuit egy előnézetet is készít a forráskódbol és a
kimeneti képet EPS, PDF, PNG vagy PSTricks formátumba is
exportálhatod.

%prep
%setup -q

%build
mkdir %{builddir}
cd %{builddir}
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd %{builddir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*

# maybe should create a kde4-icon-oxygen-svg-dirs package - I don't want to download
# 38.1 MB rpm package and I don't want 50.2 MB of unused icons
%dir %{_iconsdir}/oxygen
%dir %{_iconsdir}/oxygen/scalable
%dir %{_iconsdir}/oxygen/scalable/mimetypes
%{_desktopdir}/kde4/cirkuit.desktop
%{_datadir}/apps/cirkuit/
%{_iconsdir}/hicolor/64x64/apps/cirkuit.png
%{_iconsdir}/hicolor/32x32/apps/cirkuit.png
%{_iconsdir}/hicolor/48x48/apps/cirkuit.png
%{_iconsdir}/oxygen/scalable/mimetypes/application-x-cirkuit.svgz
%{_datadir}/mime/packages/cirkuit.xml
