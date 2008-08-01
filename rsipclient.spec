%define	name	rsipclient
%define version 0.20
%define release %mkrel 6

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

