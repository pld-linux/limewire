Summary:	The Fastest P2P File Sharing Program on the Planet
Summary(pl):	Program do wspó³dzielenia plików metod± P2P
Name:		limewire
Version:	4.10.9
Release:	0.1
Epoch:		0
# ??? GPL v2 with missing sources = non-distributable
License:	GPL v2
Group:		Applications/Networking
# Source0Download: http://www.limewire.com/LimeWireSoftLinux
Source0:	LimeWire-free-%{version}-0.rpm
# NoSource0-md5: d19a4f12560a6621268c70a3fcc8a86c
NoSource:	0
URL:		http://www.limewire.com/
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
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -id

rm usr/lib/LimeWire/COPYING # GPL v2
rm usr/lib/LimeWire/Limewire.{mandrake,desktop}
rm usr/lib/menu/LimeWire-free
mv usr/lib/LimeWire/{SOURCE,README.txt} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}
cp -a usr/* $RPM_BUILD_ROOT%{_prefix}

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
%{_libdir}/root
%{_libdir}/*.jar
%{_libdir}/*.png
%{_libdir}/*.gif
%{_libdir}/data.ser
%{_libdir}/update.ver
%{_libdir}/MessagesBundle.properties
%{_libdir}/log4j.properties
%{_libdir}/hashes
%{_libdir}/runLime.sh
%{_libdir}/xml.war
%{_desktopdir}/LimeWire.desktop
%{_iconsdir}/hicolor/*/apps/limewire.png
%{_pixmapsdir}/limewire.png
