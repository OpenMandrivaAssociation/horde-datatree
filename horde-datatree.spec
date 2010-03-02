%define prj    Horde_DataTree

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-datatree
Version:       0.0.3
Release:       %mkrel 1
Summary:       DataTree API
License:       LGPL
Group:         Productivity/Networking/Web/Servers
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
PreReq:        %{_bindir}/pear
Requires:      horde-framework
Requires:      horde-serialize
Requires:      horde-sql
Requires:      horde-util
Requires:      php-gettext
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde

%description
There is no description for the package available :(


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/DataTree
%{peardir}/Horde/DataTree.php
%{peardir}/Horde/DataTree/null.php
%{peardir}/Horde/DataTree/sql.php

