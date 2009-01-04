# TODO
# - BR: -- Could NOT find marble  (missing:  MARBLE_INCLUDE_DIR MARBLE_LIBRARIES)
#--  libmarblewidget library found....... NO  (optional)
#--  liblensfun library found............ NO  (optional)
#--  digiKam will be compiled without geolocation using Marble widget support.                                                 
#--  digiKam will be compiled without lens auto-correction image editor plugin.           

%define		orgname kdeextragear-graphics
%define		snap	880234
%define		qtver	4.4.1
Summary:	Kipi (KDE Image Plugin Interface)
Summary(pl.UTF-8):	Kipi (KDE Image Plugin Interface)
Name:		kde4-kdeextragear-graphics
Version:	4.1.72
Release:	0.%{snap}.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/unstable/snapshots/%{orgname}-%{snap}.tar.bz2
# Source0-md5:	fa95171348c6891057c2703ab358ef87
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	gphoto2-devel
BuildRequires:	kde4-kdegraphics-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	kde4-libkdcraw >= %{version}
BuildRequires:	kde4-libkexiv2 >= %{version}
BuildRequires:	kde4-libkipi >= %{version}
BuildRequires:	lcms-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kipi (KDE Image Plugin Interface) is an effort to develop a common
plugin structure for Digikam, KimDaBa, Showimg and Gwenview. Its aim
is to share image plugins among graphic applications. Kipi is based on
the old digiKam plugins implementation and is maintened by digiKam
team.

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

%package kipiplugins
Summary:	KDE Image Plugin Interface
Group:		X11/Applications/Graphics

%description kipiplugins
KIPI (KDE Image Plugin Interface) is an effort to develop a common
plugin structure for Digikam, KPhotoAlbum, Showimg and GwenView. Its
aim is to share image plugins among graphic applications. Kipi is
based on the old digiKam plugins implementation.

One of the nicest things about KDE Photo Management Programs like
"digiKam", "KPhotoAlbum", "GwenView" and "ShowImg" is how easily its
functionality can be extended, by using plugins. Plugins can
manipulate image files in almost any way that users can. Their
advantage is that it is much easier to add a capability to the host
application by writing a small plugin than by modifying the host
application core. Many valuable plugins have C++ source code that only
comes to 100-200 lines or so.

Kipi plugins are additional functions for the KDE Images Managment
Host Programs. They can add extra menus and shortcuts, and extend the
host programs features. You can install as many or as few as you like,
from within host programs. .

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
%setup -q -n %{orgname}-%{snap}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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
%find_lang kuickshow	--with-kde
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
%attr(755,root,root) %{_libdir}/libdigikamcore.so
%attr(755,root,root) %{_libdir}/libdigikamcore.so.1
%attr(755,root,root) %{_libdir}/libdigikamcore.so.1.0.0
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
%{_mandir}/man1/digitaglinktree.1*

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

%files kipiplugins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkipiplugins.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so.1
%attr(755,root,root) %{_libdir}/libkipiplugins.so.1.0.0
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_acquireimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_dngconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_flickrexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_galleryexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_gpssync.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_htmlexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_imageviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_jpeglossless.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_metadataedit.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_picasawebexport.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_rawconverter.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_sendimages.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_simpleviewer.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_slideshow.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_timeadjust.so
%{_datadir}/apps/kipiplugin_galleryexport/pics
%{_datadir}/apps/kipiplugin_htmlexport/themes
%{_datadir}/apps/kipiplugin_imageviewer/pics
%{_datadir}/apps/kipiplugin_metadataedit/data
%{_datadir}/apps/kipiplugin_simpleviewerexport
%{_datadir}/apps/kipiplugin_slideshow
%{_datadir}/kde4/services/kipiplugin_acquireimages.desktop
%{_datadir}/kde4/services/kipiplugin_dngconverter.desktop
%{_datadir}/kde4/services/kipiplugin_flickrexport.desktop
%{_datadir}/kde4/services/kipiplugin_galleryexport.desktop
%{_datadir}/kde4/services/kipiplugin_gpssync.desktop
%{_datadir}/kde4/services/kipiplugin_htmlexport.desktop
%{_datadir}/kde4/services/kipiplugin_imageviewer.desktop
%{_datadir}/kde4/services/kipiplugin_jpeglossless.desktop
%{_datadir}/kde4/services/kipiplugin_metadataedit.desktop
%{_datadir}/kde4/services/kipiplugin_picasawebexport.desktop
%{_datadir}/kde4/services/kipiplugin_rawconverter.desktop
%{_datadir}/kde4/services/kipiplugin_sendimages.desktop
%{_datadir}/kde4/services/kipiplugin_simpleviewer.desktop
%{_datadir}/kde4/services/kipiplugin_slideshow.desktop
%{_datadir}/kde4/services/kipiplugin_timeadjust.desktop
%{_iconsdir}/hicolor/*/actions/dngconverter.png
%{_iconsdir}/hicolor/*/actions/rawconverterbatch.png
%{_iconsdir}/hicolor/*/actions/rawconvertersingle.png
%{_iconsdir}/hicolor/*/actions/slideshow.png
%{_iconsdir}/hicolor/*/actions/gpsimagetag.png
%{_iconsdir}/hicolor/*/actions/grayscaleconvert.png
%{_iconsdir}/hicolor/*/actions/ogl.png
%{_iconsdir}/hicolor/*/actions/timeadjust.png
%{_iconsdir}/hicolor/*/actions/metadataedit.png
%{_iconsdir}/oxygen/*/actions/transform-crop-and-resize.png
%{_iconsdir}/oxygen/*/actions/view-object-histogram-linear.png
%{_iconsdir}/oxygen/*/actions/view-object-histogram-logarithmic.png
%{_iconsdir}/oxygen/scalable/actions/transform-crop-and-resize.svgz
%{_iconsdir}/oxygen/scalable/actions/view-object-histogram-linear.svgz
%{_iconsdir}/oxygen/scalable/actions/view-object-histogram-logarithmic.svgz

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
#%{_desktopdir}/kde4/kgraphviewer_part.desktop
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
#%{_datadir}/kde4/services/kgrapheditor.desktop

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
%{_datadir}/kde4/services/kpovmodelerpart.desktop

%files kuickshow -f kuickshow.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kuickshow
%{_desktopdir}/kde4/kuickshow.desktop
%attr(755,root,root) %{_libdir}/libkdeinit4_kuickshow.so
%dir %{_datadir}/apps/kuickshow
%{_datadir}/apps/kuickshow/pics
%{_datadir}/apps/kuickshow/im_palette.pal
%{_iconsdir}/hicolor/*/apps/kuickshow.png

%files skanlite -f skanlite.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skanlite
%{_desktopdir}/kde4/skanlite.desktop
