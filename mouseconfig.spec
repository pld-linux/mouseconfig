Summary:	Red Hat & PLD Mouse Configuration tool
Summary(de):	Red Hat & PLD Mauskonfigurations-Tool
Summary(fr):	L'outil de configuration de la souris de Red Hat & PLD.
Summary(pl):	Narz�dzie do konfiguracji myszy
Summary(tr):	Red Hat & PLD fare yap�land�rma arac�
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
configurer le type correct de souris pour des programmes comme � gpm
�. Sert aussi avec Xconfigurator de Red Hat pour configurer la souris
pour le syst�me X.

%description -l de
Dies ist ein textbasierendes Mauskonfigurations-Tool. Es kann benutzt
werden, um den richtigen Maustyp f�r Programme wie gpm einzustellen,
oder aber in Kombination mit dem Red-Hat-XConfigurator zum Einrichten
der Maus f�r das X-Window-System.

%description -l pl
To jest tekstowe narz�dzie do konfiguracji myszy. Mo�esz u�y� go do
ustawienia typu myszki programach typu gpm. Mo�e by� tak�e
wykorzystane w po��czeniu z redhatowym Xconfiguratorem do ustawienia
myszy dla X Window System.

%description -l tr
Metin tabanl� bir fare yap�land�rma arac�d�r. gpm benzeri programlar
i�in uygun fare tipinin kurulmas�nda kullan�l�r. Ayn� zamanda X Window
Sistemi'nin fare kurulumunda Red Hat Xconfigurator program� ile
beraber kullan�labilir.

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
