%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-systemd
%global commit 047b31db32f5b6ed2555fedb1bf0cfd02d19e23d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-systemd
Version:                1.0.0
Release:                1%{?alphatag}%{?dist}
Summary:                Puppet Systemd module
License:                Apache-2.0

URL:                    https://github.com/camptocamp/puppet-systemd

Source0:                https://github.com/camptocamp/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 1.0.0-1.047b31dgit
- Pike update 1.0.0 (047b31db32f5b6ed2555fedb1bf0cfd02d19e23d)
