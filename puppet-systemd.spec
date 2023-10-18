%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global commit e5ae64c0aa2dfa4fa94140e6867c4dcc846e29f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:                   puppet-systemd
Version:                6.0.1
Release:                0.1%{?milestone}%{?alphatag}%{?dist}
Summary:                Puppet Systemd module
License:                Apache-2.0

URL:                    https://github.com/voxpupuli/puppet-systemd

Source0:                https://github.com/voxpupuli/puppet-systemd/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

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
* Wed Oct 18 2023 RDO <dev@lists.rdoproject.org> 6.0.1-0.1.0rc0.e5ae64cgit
- Update to post 6.0.1-rc0 (e5ae64c0aa2dfa4fa94140e6867c4dcc846e29f1)



