Summary:	Red Hat & PLD Mouse Configuration tool
Summary(de):	Red Hat & PLD Mauskonfigurations-Tool
Summary(fr):	L'outil de configuration de la souris de Red Hat & PLD
Summary(pl):	Narzêdzie do konfiguracji myszy
Summary(tr):	Red Hat & PLD fare yapýlandýrma aracý
Name:		mouseconfig
Version:	4.25
Release:	1
License:	distributable
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	dcf2c85f8259736b683412ce5462d38b
Patch1:		%{name}-pl.po.patch
BuildRequires:	kudzu-devel
BuildRequires:	newt-devel
ExcludeArch:	sparc s390 s390x
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
%patch1 -p1

%build
# First check running Linux release ... 
%{__make} \
	CPPFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT \
    mandir=%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/mouseconfig
%{_mandir}/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
