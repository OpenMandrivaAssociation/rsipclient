%define	name	rsipclient
%define version 0.20
%define release %mkrel 7

Summary:	A Python client to contact rsipd server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:          System/Configuration/Networking
URL:		http://openresources.info.ucl.ac.be/rsip/index.php
Source0:	%{name}-%{version}.tar.bz2
Requires:   python
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
Python client version to install on rsipd client machines.
The slpd from http://www.openslp.org is highly recommended as it will allow
easier installation of the client software, but it is not required.


%prep
%setup -q -c -n %{name}-%{version}

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m 755 rsipclient %{buildroot}%{_sbindir}/rsipclient

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/rsipclient



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.20-7mdv2010.0
+ Revision: 433458
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.20-6mdv2009.0
+ Revision: 260341
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.20-5mdv2009.0
+ Revision: 251538
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.20-3mdv2008.1
+ Revision: 126759
- kill re-definition of %%buildroot on Pixel's request


* Fri Sep 30 2005 Michael Scherer <misc@mandriva.org> 0.20-3mdk
- Rebuild
- mkrel

* Wed Sep 15 2004 Michael Scherer <misc@mandrake.org> 0.20-2mdk
- Rebuild

* Fri Sep 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.20-1mdk
- from Laurent Grawet <laurent.grawet@ibelgique.com> :
	- Updated rsipclient to 0.20

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.19-2mdk
- build release

* Wed Sep 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.19-1mdk
- noarch
- from Laurent Grawet <laurent.grawet@ibelgique.com> :
	- Updated rsipclient to 0.19

* Fri Aug 30 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.18-1mdk
- used the spec file provided by Laurent Grawet
- initial cooker contrib
- misc spec file fixes

* Wed Aug 07 2002 Laurent Grawet <laurent.grawet@ibelgique.com> 0.18-1mdk
- Splitted from the "all-in-one" rsipd package

