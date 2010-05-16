Summary:	The Fastest P2P File Sharing Program on the Planet
Summary(pl.UTF-8):	Program do współdzielenia plików metodą P2P
Name:		limewire
Version:	4.16.7
Release:	0.1
Epoch:		0
# ??? GPL v2 with missing sources = non-distributable
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www10.limewire.com/download/LimeWireOther.zip
# NoSource0-md5:	435f292e2da91236a54ec999b1941a21
NoSource:	0
URL:		http://www.limewire.com/
BuildRequires:	unzip
Requires:	bash
Requires:	jre > 1.4.0
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

%define		_appdir	%{_datadir}/LimeWire

%description
LimeWire is faster than Ever
- Guaranteed clean install with no bundled software
- Firewall-to-firewall transfers
- Cleaner, updated interface with new icons
- Proxy support

%description -l pl.UTF-8
LimeWire jest szybszy niż kiedykolwiek
- gwarantowana czysta instalacja bez dołączonego oprogramowania
- przesyłanie danych od firewalla do firewalla
- czysty, uaktualniony interfejs z nowymi ikonami
- obsługa proxy

%prep
%setup -q -n LimeWire
%{__sed} -i -e 's,\r$,,' SOURCE README.txt *.js hashes log4j.properties magnet.protocol

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_libdir},%{_bindir}}
cp -a *.jar *.js $RPM_BUILD_ROOT%{_appdir}
cp -a root $RPM_BUILD_ROOT%{_appdir}
cp -a data.ser hashes log4j.properties magnet.protocol $RPM_BUILD_ROOT%{_appdir}
install libjdic.so libtray.so $RPM_BUILD_ROOT%{_libdir}
install runLime.sh $RPM_BUILD_ROOT%{_appdir}

# our improved script
cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/limewire
#!/bin/sh
cd %{_libdir}
exec bash runLime.sh
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc SOURCE README.txt
%attr(755,root,root) %{_bindir}/limewire
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libtray.so
%attr(755,root,root) %{_libdir}/libjdic.so
%{_appdir}/root
%{_appdir}/*.jar
%{_appdir}/*.js
%{_appdir}/*.protocol
%{_appdir}/data.ser
%{_appdir}/log4j.properties
%{_appdir}/hashes
%{_appdir}/runLime.sh
#%{_desktopdir}/LimeWire.desktop
#%{_iconsdir}/hicolor/*/apps/limewire.png
#%{_pixmapsdir}/limewire.png
