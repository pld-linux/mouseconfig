Summary:	Red Hat & PLD Mouse Configuration tool
Summary(fr):	L'outil de configuration de la souris de Red Hat & PLD.
Summary(de):	Red Hat & PLD Mauskonfigurations-Tool
Summary(tr):	Red Hat & PLD fare yapýlandýrma aracý
Name:		mouseconfig
Version:	3.9
Release:	1
Copyright:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		%{name}-%{version}.tar.gz
Patch0:		mouseconfig-pl.po.patch
Patch1:		mouseconfig-kernel23.patch
Excludearch:	sparc
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a text based mouse configuration tool.  You can use
it to set the proper mouse type for programs like 'gpm'.  It also
can be used in conjunction with the Red Hat Xconfigurator to setup
the mouse for the X Window System.

%description -l fr
Outil de configuration de la souris en mode texte. Permet de configurer
le type correct de souris pour des programmes comme « gpm ». Sert aussi avec
Xconfigurator de Red Hat pour configurer la souris pour le système X.

%description -l de
Dies ist ein textbasierendes Mauskonfigurations-Tool. Es kann benutzt 
werden, um den richtigen Maustyp für Programme wie gpm einzustellen, 
oder aber in Kombination mit dem Red-Hat-XConfigurator zum Einrichten 
der Maus für das X-Window-System. 

%description -l tr
Metin tabanlý bir fare yapýlandýrma aracýdýr. gpm benzeri programlar için uygun
fare tipinin kurulmasýnda kullanýlýr. Ayný zamanda X Window Sistemi'nin fare
kurulumunda Red Hat Xconfigurator programý ile beraber kullanýlabilir.

%prep
%setup -q
%patch0 -p1

%build
# First check running Linux release ... 
RELEASE=`uname -r | head -c 3`
if [ "$RELEASE" = "2.3" ]; then
    patch -p1 < $RPM_SOURCE_DIR/%{name}-kernel23.patch
fi

make CPPFLAGS="$RPM_OPT_FLAGS"
strip mouseconfig

%install
rm -rf $RPM_BUILD_ROOT
make \
    PREFIX=$RPM_BUILD_ROOT \
    install

install -d $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/{man8/*,pt_BR/man8/*}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/mouseconfig
%{_mandir}/man8/*
%lang(pt) %{_mandir}/pt_BR/man8/*
