%define		orgname kdeextragear-graphics

Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		kde4-kdeextragear-graphics
Version:	804573
Release:	0.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{version}.tar.bz2
# Source0-md5:	32a6ac0fbcbfe1dcf00202e7966c8951
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
# this lib isn't yet in the repository
BuildRequires:	libksane-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDcraw Library is part of the KIPI Project.

%description -l pl.UTF-8
Biblioteka KDcraw jest częścią projektu KIPI.

%package devel
Summary:	Header files for libkdcraw development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkdcraw
Group:		X11/Development/Libraries

%description devel
Header files for libkdcraw development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdcraw.

%package -n digikam
Summary:	digikam
Summary(pl.UTF-8):	digikam
Group:		X11/Libraries
Requires:	QtSql-sqlite3
Requires:	qt4-phonon
Provides:	libkdcraw

%description -n digikam
digikam.

%description -n digikam -l pl.UTF-8
digikam.

%package kcoloredit
Summary:	Color palette editor
Summary(pl.UTF-8):	Edytor palety kolorów
Group:		X11/Applications/Graphics

%description kcoloredit
KColorEdit is a palette files editor. It can be used for editing color
palettes and for color choosing and naming.

%description kcoloredit -l pl.UTF-8
KColorEdit to edytor plików palety kolorów. Może być używany do edycji
palet kolorów oraz wybierania i nazywania kolorów.

%package kfax
Summary:	KDE Fax viewer
Summary(pl.UTF-8):	Przeglądarka faksów dla KDE
Group:		X11/Applications/Graphics

%description kfax
KFax is a Fax file viewer capable of displaying and printing all
common fax file formats. In particular the fax files used by popular
the mgetty/sendfax and hylafax fax send and receive packages can be
displayed. The first (or only) page of a "PC-Research"-style (DigiFAX)
files produced by the ghostscript dfaxhigh or dfaxlow drivers can also
be displayed. (who is still using this format?) Input files using any
common fax encoding such as group 3 (1 and 2 dimensional) and group 4
can be displayed. KFax has built in native postscript printing
capabilities.

%description kfax -l pl.UTF-8
KFax to przeglądarka plików faksowych potrafiąca wyświetlać i drukować
wszystkie popularne formaty plików faksowych. W szczególności można
wyświetlać pliki faksów używane przez pakiety do wysyłania i
odbierania faksów mgetty/sendfax oraz hylafax. Można wyświetlić także
pierwszą (lub jedyną) stronę plików w stylu "PC-Research" (DigiFAX)
stworzonych przez sterowniki dfaxhigh i dfaxlow z ghostscripta. Pliki
wejściowe mogą używać dowolnego popularnego kodowania, takiego jak G3
(1- i 2-wymiarowego) lub G4. KFax ma wbudowaną natywną możliwość
wydruku do postscriptu.

%package kiconedit
Summary:	KDE Icon Editor
Summary(pl.UTF-8):	Edytor ikon dla środowiska KDE
Group:		X11/Applications/Graphics

%description kiconedit
KDE Icon editor.

%description kiconedit -l pl.UTF-8
Edytor ikon dla KDE.

%package kgrab
Summary:	kgrab
Summary(pl.UTF-8):	kgrab
Group:		X11/Applications/Graphics

%description kgrab
kgrab.

%description kgrab -l pl.UTF-8
kgrab.

%package kgraphviewer
Summary:	kgraphviewer
Summary(pl.UTF-8):	kgraphviewer
Group:		X11/Applications/Graphics

%description kgraphviewer
kgraphviewer.

%description kgraphviewer -l pl.UTF-8
kgraphviewer.

%package kphotoalbum
Summary:	kphotoalbum
Summary(pl.UTF-8):	kphotoalbum
Group:		X11/Applications/Graphics

%description kphotoalbum
kphotoalbum.

%description kphotoalbum -l pl.UTF-8
kphotoalbum.

%package kpovmodeler
Summary:	Povary Modeler
Summary(pl.UTF-8):	Modeler Povary
Group:		X11/Applications/Graphics
Requires:	povray

%description kpovmodeler
Modeler for POV-Ray scenes.

%description kpovmodeler -l pl.UTF-8
Modeler do scen POV-Raya.

%package kuickshow
Summary:	Image viewer/browser
Summary(pl.UTF-8):	Przeglądarka obrazków
Group:		X11/Applications/Graphics
Provides:	kuickshow
Obsoletes:	kuickshow

%description kuickshow
KuickShow is a comfortable image browser/viewer. It displays a
filebrowser where you can select images which are then shown. The
following image formats are supported: jpg, gif, tiff, png, bmp, psd,
xpm, xbm, eim. Images can be displayed either in their own window, as
large as the image, or fullscreen.

%description kuickshow -l pl.UTF-8
KuickShow to wygodna przeglądarka obrazków. Wyświetla przeglądarkę
plików, w której można wybierać obrazki do pokazania. Obsługiwane są
następujące formaty obrazków: jpg, gif, tiff, png, bmp, psd, xpm, xbm,
eim. Obrazki mogą być wyświetlane w swoim oknie o rozmiarze obrazka
lub na pełnym ekranie.

%package skanlite
Summary:	skanlite
Summary(pl.UTF-8):	skanlite
Group:		X11/Applications/Graphics

%description skanlite
skanlite.

%description skanlite -l pl.UTF-8
skanlite.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

#%find_lang digikam	--with-kde
%find_lang kcoloredit	--with-kde
%find_lang kgraphviewer	--with-kde
%find_lang kiconedit	--with-kde
%find_lang kpovmodeler	--with-kde
#%find_lang kuickshow	--with-kde
%find_lang skanlite	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -n digikam
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/digikam
%attr(755,root,root) %{_bindir}/digikam-camera
%attr(755,root,root) %{_bindir}/digikamthemedesigner
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%{_includedir}/digikam
%{_includedir}/digikam_export.h
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_adjustcurves.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_adjustlevels.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_blurfx.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_border.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_channelmixer.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_charcoal.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_colorfx.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_core.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_distortionfx.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_emboss.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_filmgrain.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_freerotation.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_hotpixels.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_infrared.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_inpainting.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_inserttext.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_lenscorrection.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_noisereduction.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_oilpaint.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_perspective.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_raindrop.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_restoration.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_sheartool.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_superimpose.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_texture.so
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_whitebalance.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamalbums.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamdates.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamsearch.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamtags.so
%attr(755,root,root) %{_libdir}/libdigikam.so
%attr(755,root,root) %{_libdir}/libdigikam.so.1
%attr(755,root,root) %{_libdir}/libdigikam.so.1.0.0
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.1
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.1.0.0
%{_desktopdir}/kde4/digikam.desktop
%{_desktopdir}/kde4/showfoto.desktop
%{_datadir}/apps/digikam
%{_datadir}/apps/showfoto

%{_iconsdir}/*/*/actions/addimagefolder.*
%{_iconsdir}/*/*/actions/adjustcurves.*
%{_iconsdir}/*/*/actions/adjusthsl.*
%{_iconsdir}/*/*/actions/adjustlevels.*
%{_iconsdir}/*/*/actions/adjustrgb.*
%{_iconsdir}/*/*/actions/albumfoldercomment.*
%{_iconsdir}/*/*/actions/albumfoldernew.*
%{_iconsdir}/*/*/actions/antivignetting.*
%{_iconsdir}/*/*/actions/autocorrection.*
%{_iconsdir}/*/*/actions/blurfx.*
%{_iconsdir}/*/*/actions/blurimage.*
%{_iconsdir}/*/*/actions/bordertool.*
%{_iconsdir}/*/*/actions/bwtonal.*
%{_iconsdir}/*/*/actions/channelmixer.*
%{_iconsdir}/*/*/actions/charcoaltool.*
%{_iconsdir}/*/*/actions/colorfx.*
%{_iconsdir}/*/*/actions/colormanagement.*
%{_iconsdir}/*/*/actions/contrast.*
%{_iconsdir}/*/*/actions/crop.*
%{_iconsdir}/*/*/actions/depth16to8.*
%{_iconsdir}/*/*/actions/depth8to16.*
%{_iconsdir}/*/*/actions/digitalcam.*
%{_iconsdir}/*/*/actions/distortionfx.*
%{_iconsdir}/*/*/actions/editimage.*
%{_iconsdir}/*/*/actions/embosstool.*
%{_iconsdir}/*/*/actions/exifinfo.*
%{_iconsdir}/*/*/actions/filmgrain.*
%{_iconsdir}/*/*/actions/freerotation.*
%{_iconsdir}/*/*/actions/histogram.*
%{_iconsdir}/*/*/actions/hotpixels.*
%{_iconsdir}/*/*/actions/imagecomment.*
%{_iconsdir}/*/*/actions/importfolders2albums.*
%{_iconsdir}/*/*/actions/infrared.*
%{_iconsdir}/*/*/actions/inpainting.*
%{_iconsdir}/*/*/actions/inserttext.*
%{_iconsdir}/*/*/actions/invertimage.*
%{_iconsdir}/*/*/actions/lensdistortion.*
%{_iconsdir}/*/*/actions/noisereduction.*
%{_iconsdir}/*/*/actions/oilpaint.*
%{_iconsdir}/*/*/actions/perspective.*
%{_iconsdir}/*/*/actions/raindrop.*
%{_iconsdir}/*/*/actions/ratiocrop.*
%{_iconsdir}/*/*/actions/redeyes.*
%{_iconsdir}/*/*/actions/resize_image.*
%{_iconsdir}/*/*/actions/restoration.*
%{_iconsdir}/*/*/actions/sharpenimage.*
%{_iconsdir}/*/*/actions/shear.*
%{_iconsdir}/*/*/actions/superimpose.*
%{_iconsdir}/*/*/actions/texture.*
%{_iconsdir}/*/*/actions/viewimage.*
%{_iconsdir}/*/*/actions/whitebalance.*
%{_iconsdir}/*/*/apps/digikam.*
%{_iconsdir}/*/*/apps/showfoto.*
%{_iconsdir}/*/*/actions/flip-horizontal.png
%{_iconsdir}/*/*/actions/flip-vertical.png
%{_iconsdir}/*/*/mimetypes/raw.png
%{_iconsdir}/*/*/actions/digikamimageplugins.png
%{_iconsdir}/*/*/actions/filefind.png
%{_iconsdir}/*/*/actions/lighttable.png
%{_iconsdir}/*/*/actions/video.png
%{_iconsdir}/*/*/actions/lighttableadd.png
%{_iconsdir}/*/*/actions/zoom-select-fit.png
%{_iconsdir}/*/*/apps/digikamimageplugins.png
%{_datadir}/kde4/services/ServiceMenus/digikam-download.desktop
%{_datadir}/kde4/services/ServiceMenus/digikam-gphoto2-camera.desktop
%{_datadir}/kde4/services/ServiceMenus/digikam-mount-and-download.desktop
%{_datadir}/kde4/services/digikamalbums.protocol
%{_datadir}/kde4/services/digikamdates.protocol
%{_datadir}/kde4/services/digikamimageplugin_*.desktop
%{_datadir}/kde4/services/digikamsearch.protocol
%{_datadir}/kde4/services/digikamtags.protocol
%{_datadir}/kde4/servicetypes/digikamimageplugin.desktop
%{_mandir}/digitaglinktree.1*

%files kcoloredit -f kcoloredit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcoloredit
%{_desktopdir}/kde4/kcoloredit.desktop
%{_datadir}/apps/kcoloredit/kcoloreditui.rc
%{_iconsdir}/hicolor/*x*/apps/kcoloredit.png

%files kfax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfax
%{_desktopdir}/kde4/kfax.desktop
%{_datadir}/apps/kfax/pics/kfax.tif
%{_datadir}/apps/kfax/pics/kfaxlogo.xpm
%{_datadir}/apps/kfax/kfaxui.rc
%{_iconsdir}/hicolor/*x*/apps/kfax.png
%{_iconsdir}/hicolor/scalable/apps/kfax.svgz

%files kiconedit -f kiconedit.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiconedit
%{_desktopdir}/kde4/kiconedit.desktop
%{_datadir}/apps/kiconedit
%{_iconsdir}/hicolor/*x*/apps/kiconedit.png

%files kgrab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgrab
%{_desktopdir}/kde4/kgrab.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kgrab.xml
%{_datadir}/apps/kgrab
%{_iconsdir}/hicolor/*x*/apps/kgrab.png
%{_iconsdir}/hicolor/scalable/apps/kgrab.svgz

%files kgraphviewer -f kgraphviewer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kgraphviewerpart.so
%{_datadir}/config.kcfg/kgraphviewer_partsettings.kcfg
%{_datadir}/apps/kgraphviewerpart
%{_desktopdir}/kde4/kgraphviewer_part.desktop
%{_datadir}/kde4/services/kgraphviewer_part.desktop
%attr(755,root,root) %{_bindir}/kgraphviewer
%{_iconsdir}/hicolor/*x*/apps/kgraphviewer.png
%{_datadir}/config.kcfg/kgraphviewersettings.kcfg
%{_datadir}/apps/kgraphviewer
%{_desktopdir}/kde4/kgraphviewer.desktop
%attr(755,root,root) %{_bindir}/kgrapheditor
%{_datadir}/config.kcfg/kgrapheditorsettings.kcfg
%{_datadir}/apps/kgrapheditor
%{_desktopdir}/kde4/kgrapheditor.desktop
%{_datadir}/kde4/services/kgrapheditor.desktop

%files kphotoalbum
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphotoalbum
%{_desktopdir}/kde4/kphotoalbum.desktop
%{_desktopdir}/kde4/kphotoalbum-import.desktop
%{_datadir}/config/kphotoalbumrc
%dir %{_datadir}/apps/kphotoalbum
%{_datadir}/apps/kphotoalbum/tips
%{_datadir}/apps/kphotoalbum/kphotoalbumui.rc
%{_datadir}/apps/kphotoalbum/default-setup
%{_datadir}/apps/kphotoalbum/default-layout.xml
%{_datadir}/apps/kphotoalbum/demo
%{_datadir}/apps/kphotoalbum/pics
%{_iconsdir}/hicolor/*/actions/texttool.png
%{_iconsdir}/hicolor/*/apps/kphotoalbum.png
%{_iconsdir}/hicolor/*/actions/selecttool.png
%{_iconsdir}/hicolor/*/actions/key.png
%{_iconsdir}/hicolor/*/actions/recttool.png
%{_iconsdir}/hicolor/*/actions/ellipsetool.png
%{_iconsdir}/hicolor/*/actions/linetool.png
%{_datadir}/apps/kphotoalbum/themes

%files kpovmodeler -f kpovmodeler.lang
%defattr(644,root,root,755)
%{_datadir}/apps/kpovmodeler
%attr(755,root,root) %{_libdir}/liblkpovmodeler.so
%attr(755,root,root) %{_libdir}/kde4/libkpovmodelerpart.so
%attr(755,root,root) %{_bindir}/kpovmodeler
%attr(755,root,root) %{_libdir}/liblkpovmodeler.so.0
%attr(755,root,root) %{_libdir}/liblkpovmodeler.so.0.0.0
%{_desktopdir}/kde4/kpovmodeler.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kpovmodeler.xml
%{_iconsdir}/hicolor/*/apps/kpovmodeler.png
%{_iconsdir}/oxygen/*/mimetypes/kpovmodeler_doc.png

%files skanlite -f skanlite.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skanlite
%{_desktopdir}/kde4/skanlite.desktop
