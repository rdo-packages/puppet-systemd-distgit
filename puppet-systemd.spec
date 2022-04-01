%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global commit 65af359246f2ae2dae277797a0133f49ba7979aa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-systemd
Version:                3.8.1
Release:                0.1%{?milestone}%{?alphatag}%{?dist}
Summary:                Puppet Systemd module
License:                Apache-2.0

URL:                    https://github.com/camptocamp/puppet-systemd

Source0:                https://github.com/camptocamp/puppet-systemd/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch:              noarch


Requires:               puppet >= 2.7.0

%description
Puppet module that configures systemd.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/systemd/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/systemd/



%files
%{_datadir}/openstack-puppet/modules/systemd/


%changelog
* Fri Apr 01 2022 RDO <dev@lists.rdoproject.org> 3.8.1-0.1.0rc0.76e91a6git
- Update to post 3.8.1-rc0 (76e91a6ce46d1a13cbf7baa0e28ccf40b2ced52a)



