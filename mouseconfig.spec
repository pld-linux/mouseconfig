Summary:	Red Hat & PLD Mouse Configuration tool
Summary(de):	Red Hat & PLD Mauskonfigurations-Tool
Summary(fr):	L'outil de configuration de la souris de Red Hat & PLD.
Summary(pl):	Narzêdzie do konfiguracji myszy
Summary(tr):	Red Hat & PLD fare yapýlandýrma aracý
Name:		mouseconfig
Version:	3.9
Release:	1
License:	distributable
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-pl.po.patch
Patch1:		%{name}-kernel23.patch
ExcludeArch:	sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a text based mouse configuration tool. You can use it to set
the proper mouse type for programs like 'gpm'. It also can be used in
conjunction with the Red Hat Xconfigurator to setup the mouse for the
X Window System.

%description -l fr
Outil de configuration de la souris en mode texte. Permet de
configurer le type correct de souris pour des programmes comme « gpm
». Sert aussi avec Xconfigurator de Red Hat pour configurer la souris
pour le système X.

%description -l de
Dies ist ein textbasierendes Mauskonfigurations-Tool. Es kann benutzt
werden, um den richtigen Maustyp für Programme wie gpm einzustellen,
oder aber in Kombination mit dem Red-Hat-XConfigurator zum Einrichten
der Maus für das X-Window-System.

%description -l pl
To jest tekstowe narzêdzie do konfiguracji myszy. Mo¿esz u¿yæ go do
ustawienia typu myszki programach typu gpm. Mo¿e byæ tak¿e
wykorzystane w po³±czeniu z redhatowym Xconfiguratorem do ustawienia
myszy dla X Window System.

%description -l tr
Metin tabanlý bir fare yapýlandýrma aracýdýr. gpm benzeri programlar
için uygun fare tipinin kurulmasýnda kullanýlýr. Ayný zamanda X Window
Sistemi'nin fare kurulumunda Red Hat Xconfigurator programý ile
beraber kullanýlabilir.

%prep
%setup -q
%patch0 -p1

%build
# First check running Linux release ... 
RELEASE=`uname -r | head -c 3`
if [ "$RELEASE" = "2.3" ]; then
    patch -p1 < %{PATCH1}
fi

%{__make} CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
    PREFIX=$RPM_BUILD_ROOT \
    install

install -d $RPM_BUILD_ROOT%{_datadir}
mv -f $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/mouseconfig
%{_mandir}/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
