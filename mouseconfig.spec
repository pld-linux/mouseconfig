Summary:     Red Hat Mouse Configuration tool
Summary(fr): L'outil de configuration de la souris de Red Hat.
Summary(de): Red Hat Mauskonfigurations-Tool
Summary(tr): Red Hat fare yap�land�rma arac�
Name:        mouseconfig
Version:     3.0.5
Release:     1
Copyright:   distributable
Group:       Utilities/System
Source:      %{name}-%{version}.tar.gz
Patch0:      mouseconfig-pl.po.patch
Patch1:      mouseconfig-makefile.patch
Excludearch: sparc
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a text based mouse configuration tool.  You can use
it to set the proper mouse type for programs like 'gpm'.  It also
can be used in conjunction with the Red Hat Xconfigurator to setup
the mouse for the X Window System.

%description -l fr
Outil de configuration de la souris en mode texte. Permet de configurer
le type correct de souris pour des programmes comme � gpm �. Sert aussi avec
Xconfigurator de Red Hat pour configurer la souris pour le syst�me X.

%description -l de
Dies ist ein textbasierendes Mauskonfigurations-Tool. Es kann benutzt 
werden, um den richtigen Maustyp f�r Programme wie gpm einzustellen, 
oder aber in Kombination mit dem Red-Hat-XConfigurator zum Einrichten 
der Maus f�r das X-Window-System. 

%description -l tr
Metin tabanl� bir fare yap�land�rma arac�d�r. gpm benzeri programlar i�in uygun
fare tipinin kurulmas�nda kullan�l�r. Ayn� zamanda X Window Sistemi'nin fare
kurulumunda Red Hat Xconfigurator program� ile beraber kullan�labilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make
strip mouseconfig

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%attr(755,root,root) %{_sbindir}/mouseconfig
%{_mandir}/man8/mouseconfig.8
%lang(cz) %{_datadir}/locale/cz/LC_MESSAGES/mouseconfig.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/mouseconfig.mo
%lang(en) %{_datadir}/locale/en*/LC_MESSAGES/mouseconfig.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/mouseconfig.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/mouseconfig.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/mouseconfig.mo
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/mouseconfig.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/mouseconfig.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/mouseconfig.mo

%changelog
* Thu Sep  3 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7-2]
- added mouseconfig-pl.po.patch with polish translation 
  (Konrad Stepie� <konrad@interdata.com.pl>),
- added mouseconfig-makefile.patch with fixing problems on building
  mouseconfig from non root account and for use $RPM_OPT_FLAGS in all
  places during compile,
- added -q %setup parameter,
- mouseconfig is now recompiled against slang 1.2.x, 
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %lang macros for %{_datadir}/locale/*/LC_MESSAGES/mouseconfig.mo
  files,
- removed "RPM_OPT_FLAGS=\"$RPM_OPT_FLAGS\"" make parameter (not necessary),
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, de, tr

* Thu May 07 1998 Erik Troan <ewt@redhat.com>
- uadded/updated translations

* Mon Apr 20 1998 Erik Troan <ewt@redhat.com>
- build rooted
- added de and en_RN translations

* Fri Mar 27 1998 Erik Troan <ewt@redhat.com>
- reworked much of the code to be somewhat readable -- this came from
  poor XFree86 code to begin with, and it never seemed to get any better

* Sun Nov  9 1997 Michael Fulbright <msf@redhat.com>
- fixed --expert mode

* Fri Nov  7 1997 Michael Fulbright <msf@redhat.com>
- fixes some problems with busmice probing

* Wed Nov  5 1997 Michael Fulbright <msf@redhat.com>
- changed SERIAL to serial when reporting probe results
- added a dist to Makefile, so 'make dist' makes a tarball

* Sat Nov  1 1997 Michael Fulbright <msf@redhat.com>
- added man page to file list

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- added query if ps/2 mouse found if they want to emulate 3 buttons

* Mon Oct  6 1997 Michael Fulbright <msf@redhat.com>
- fixed creation of /dev/mouse link for cua devices in interactice mode.
- added man page and --help information

* Thu Oct  2 1997 Michael Fulbright <msf@redhat.com>
- added --expert and probing in interactive mode.

* Tue Sep 30 1997 Michael Fulbright <msf@redhat.com>
- enchanced kickstart behavior, tries to autoprobe devices in this mode.

* Thu Sep 18 1997 Erik Troan <ewt@redhat.com>
- added command line options

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc
