%define		_snap 20060422
Summary:	The Fastest P2P File Sharing Program on the Planet
Summary(pl):	Program do wspó³dzielenia plików metod± P2P
Name:		limewire
# actually it's not know what is the version in snapshot and the
# release archives aren't available for download and their svn/cvs
# doesn't contain tags for releases.
Version:	4.10.9
Release:	0.2
License:	GPL v2
Group:		Applications/Networking
Source0:	%{name}-%{_snap}.zip
# NoSource0-md5: eec866306c41894e092e97e79df0c825
NoSource:	0
URL:		http://www.limewire.com/
BuildRequires:	jakarta-ant
BuildRequires:	jdk
BuildRequires:	zip
Requires:	bash
Requires:	jre > 1.4.0
Requires:	jakarta-log4j
Requires:	xerces-j
#../lib/jars/jl011.jar:../lib/jars/logicrypto.jar:\
#../lib/jars/mp3sp14.jar:../lib/jars/commons-httpclient.jar:../lib/jars/commons-logging.jar:\
#../lib/jars/i18n.jar:../lib/jars/icu4j.jar:../lib/jars/ProgressTabs.jar:../lib/jars/id3v2.jar:\
#../lib/jars/jcraft.jar:../lib/jars/looks.jar:../lib/jars/daap.jar:../lib/jars/jmdns.jar:\
#../lib/jars/tritonus.jar:../lib/jars/vorbis.jar:../lib/jars/clink.jar:../lib/jars/xml-apis.jar:\
#../lib/jars/linux/jdic.jar
# somehow to notify we need java-sun-jre-X11 or equivalent
%ifarch %{x8664}
Requires:	libmawt.so()(64bit)
%else
Requires:	libmawt.so
%endif
#BuildArch:	noarch
# Two .so files in package. subpackage?
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir %{_prefix}/lib/LimeWire

%description
LimeWire is faster than Ever
- Guaranteed clean install with no bundled software
- Firewall-to-firewall transfers
- Cleaner, updated interface with new icons
- Proxy support

%description -l pl
LimeWire jest szybszy ni¿ kiedykolwiek
- gwarantowana czysta instalacja bez do³±czonego oprogramowania
- przesy³anie danych od firewalla do firewalla
- czysty, uaktualniony interfejs z nowymi ikonami
- obs³uga proxy

%prep
%setup -qc

%build
cd trunk/core
ant
./buildCoreJar.sh

cd ../gui
ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

cd trunk
install lib/jars/other/themes.jar $RPM_BUILD_ROOT%{_libdir}

cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/limewire
#!/bin/sh
cd %{_libdir}
export J2SE_PREEMPTCLOSE=1
exec java \
	-Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog \
	-Djava.library.path=. \
	-jar LimeWire.jar
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc SOURCE README.txt
%attr(755,root,root) %{_bindir}/limewire
%dir %{_libdir}
#%attr(755,root,root) %{_libdir}/libtray.so
#%{_libdir}/root
%{_libdir}/*.jar
#%{_libdir}/*.png
#%{_libdir}/*.gif
#%{_libdir}/data.ser
#%{_libdir}/update.ver
#%{_libdir}/MessagesBundle.properties
#%{_libdir}/log4j.properties
#%{_libdir}/hashes
#%{_libdir}/runLime.sh
#%{_libdir}/xml.war
#%{_desktopdir}/LimeWire.desktop
#%{_iconsdir}/hicolor/*/apps/limewire.png
#%{_pixmapsdir}/limewire.png
