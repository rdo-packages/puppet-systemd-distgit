%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-systemd
Version:        3.10.1
Release:        0.1%{?milestone}%{?alphatag}%{?dist}
Summary:                Puppet Systemd module
License:                Apache-2.0

URL:                    https://github.com/camptocamp/puppet-systemd

Source0:                https://github.com/camptocamp/puppet-systemd/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Mon Oct 03 2022 RDO <dev@lists.rdoproject.org> 3.10.1-0.1.0rc0.ae5dfe5git
- Update to post 3.10.1 (ae5dfe59ed14b814011b18959bdf526b49577d39)



