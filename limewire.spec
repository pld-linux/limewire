Summary:	The Fastest P2P File Sharing Program on the Planet
Summary(pl):	Program do wspó³dzielenia plików metod± P2P
Name:		limewire
Version:	4.8.1
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Applications/Networking
# Source0Download: http://www.limewire.com/LimeWireSoftLinux
Source0:	LimeWireLinux.rpm
# Source0-md5:	49726ec8dd3744977ed68477332f765d
URL:		http://www.limewire.com/
Requires:	bash
Requires:	jre
#BuildArch:	noarch
# Two .so files in package
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

rm -f usr/lib/LimeWire/COPYING # GPL v2
rm -f usr/lib/LimeWire/Limewire.{mandrake,desktop}
rm -f usr/lib/menu/LimeWire
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
%attr(755,root,root) %{_libdir}/libIdleTime.so
%attr(755,root,root) %{_libdir}/libtray.so
%{_libdir}/root
%{_libdir}/*.jar
%{_libdir}/*.png
%{_libdir}/*.gif
%{_libdir}/data.ser
%{_libdir}/update.ver
%{_libdir}/MessagesBundle.properties
%{_libdir}/hashes
%{_libdir}/runLime.sh
%{_libdir}/xml.war
%{_desktopdir}/LimeWire.desktop
%{_iconsdir}/hicolor/*/apps/limewire.png
%{_pixmapsdir}/limewire.png
