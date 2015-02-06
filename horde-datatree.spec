%define prj    Horde_DataTree

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-datatree
Version:       0.0.3
Release:       4
Summary:       DataTree API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Requires(pre): php-pear
Requires:      horde-framework
Requires:      horde-serialize
Requires:      horde-sql
Requires:      horde-util
Requires:      php-gettext
Requires:      php-pear	
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



%changelog
* Mon Jul 26 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-3mdv2011.0
+ Revision: 560541
- Increased release for rebuild

* Thu Mar 18 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-2mdv2010.1
+ Revision: 524827
- increased rel version to 2
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased rel version

* Tue Mar 02 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-1mdv2010.1
+ Revision: 513314
- corrected Group: to Networking/Mail
- replaced PreReq with Requires(pre)
- removed Buildrequires: horde-framework to make it build
- import horde-datatree


